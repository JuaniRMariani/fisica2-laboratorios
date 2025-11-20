"""
Laboratorio 2 - Inciso B: Campo Magnético de Espira Circular

Calcula y visualiza el campo magnético generado por una espira circular
de radio a con corriente I.

Universidad Nacional del Sur - Física II
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from biot_savart import (
    campo_magnetico_espira,
    campo_magnetico_grilla,
    magnitud_campo,
    campo_magnetico_espira_eje,
    MU_0
)

# Configuración del sistema
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 10


def calcular_campo_punto_especifico():
    """
    Calcula el campo magnético en un punto específico para la espira circular.
    """
    print("="*70)
    print("INCISO B: CAMPO MAGNÉTICO DE ESPIRA CIRCULAR")
    print("="*70)
    
    # Parámetros de la espira
    radio = 0.15  # Radio de la espira [m]
    I = 8.0  # Corriente [A]
    
    # Punto específico donde calcular el campo
    punto = np.array([0.1, 0.05, 0.1])  # [m]
    
    print(f"\nParámetros de la espira:")
    print(f"  Radio: a = {radio} m")
    print(f"  Corriente: I = {I} A")
    print(f"  Posición: centro en el origen")
    print(f"  Orientación: plano XY (normal en eje z)")
    
    # Calcular campo magnético
    B = campo_magnetico_espira(punto, radio, I)
    B_magnitud = np.linalg.norm(B)
    
    print(f"\nPunto de evaluación: r = ({punto[0]}, {punto[1]}, {punto[2]}) m")
    print(f"\nCampo magnético en forma vectorial:")
    print(f"  B = ({B[0]:.6e}, {B[1]:.6e}, {B[2]:.6e}) T")
    print(f"  B = {B[0]:.6e} x̂ + {B[1]:.6e} ŷ + {B[2]:.6e} ẑ [T]")
    print(f"\nMagnitud del campo:")
    print(f"  |B| = {B_magnitud:.6e} T")
    print(f"  |B| = {B_magnitud*1e6:.4f} μT")
    
    # Comparar con fórmula en el eje (si el punto está en el eje)
    if abs(punto[0]) < 1e-6 and abs(punto[1]) < 1e-6:
        B_eje = campo_magnetico_espira_eje(punto[2], radio, I)
        print(f"\nComparación con fórmula analítica en el eje:")
        print(f"  B_analítico = {B_eje}")
        print(f"  |B_analítico| = {np.linalg.norm(B_eje):.6e} T")
        print(f"  Error relativo: {abs(B_magnitud - np.linalg.norm(B_eje))/np.linalg.norm(B_eje)*100:.2f}%")
    
    # Análisis del resultado
    print(f"\n" + "-"*70)
    print("ANÁLISIS:")
    print("-"*70)
    
    # Distancia al centro
    distancia_centro = np.linalg.norm(punto)
    print(f"Distancia al centro de la espira: {distancia_centro:.3f} m")
    print(f"Relación distancia/radio: {distancia_centro/radio:.3f}")
    
    return radio, I, punto, B


def graficar_campo_2D_plano_XZ(radio, I):
    """
    Grafica el campo magnético en el plano XZ (y=0).
    Este plano contiene el eje de la espira.
    """
    print(f"\nGenerando gráfico 2D (plano XZ, y=0)...")
    
    # Crear grilla en el plano XZ
    x_range = (-0.4, 0.4)
    z_range = (-0.4, 0.4)
    y_value = 0.0
    
    # Calcular campo en la grilla
    nx, nz = 30, 30
    x = np.linspace(x_range[0], x_range[1], nx)
    z = np.linspace(z_range[0], z_range[1], nz)
    X, Z = np.meshgrid(x, z)
    
    Bx = np.zeros_like(X)
    By = np.zeros_like(Z)
    Bz = np.zeros_like(X)
    
    print("  Calculando campo en grilla XZ...")
    for i in range(nz):
        for j in range(nx):
            punto = np.array([X[i, j], y_value, Z[i, j]])
            B = campo_magnetico_espira(punto, radio, I)
            Bx[i, j] = B[0]
            By[i, j] = B[1]
            Bz[i, j] = B[2]
    
    B_mag = magnitud_campo(Bx, By, Bz)
    
    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Subplot 1: Líneas de campo con mapa de color
    contour = ax1.contourf(X, Z, B_mag*1e6, levels=20, cmap='plasma', alpha=0.7)
    
    # Líneas de campo (streamplot en plano XZ)
    speed = np.sqrt(Bx**2 + Bz**2)
    lw = 2 * speed / (speed.max() + 1e-10)
    
    stream = ax1.streamplot(X, Z, Bx, Bz, color='white', linewidth=lw,
                            density=1.8, arrowsize=1.2, arrowstyle='->')
    
    # Dibujar la espira (círculo en el plano XY visto de lado)
    theta_espira = np.linspace(0, 2*np.pi, 100)
    x_espira = radio * np.cos(theta_espira)
    z_espira = np.zeros_like(theta_espira)  # z=0 para la espira en XY
    ax1.plot(x_espira, z_espira, 'r-', linewidth=4, label=f'Espira (a={radio}m)', alpha=0.9)
    ax1.plot([0], [0], 'ro', markersize=10, label='Centro')
    
    ax1.set_xlabel('x [m]', fontsize=12)
    ax1.set_ylabel('z [m]', fontsize=12)
    ax1.set_title(f'Líneas de Campo Magnético - Espira Circular\n(a={radio}m, I={I}A, plano XZ)', 
                  fontsize=14, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    
    cbar1 = plt.colorbar(contour, ax=ax1)
    cbar1.set_label('|B| [μT]', fontsize=11)
    
    # Subplot 2: Vectores del campo
    skip = 2
    ax2.quiver(X[::skip, ::skip], Z[::skip, ::skip], 
               Bx[::skip, ::skip], Bz[::skip, ::skip],
               B_mag[::skip, ::skip]*1e6, cmap='viridis',
               scale=np.max(B_mag)*25, width=0.004)
    
    # Dibujar la espira
    ax2.plot(x_espira, z_espira, 'r-', linewidth=4, label=f'Espira (a={radio}m)', alpha=0.9)
    ax2.plot([0], [0], 'ro', markersize=10)
    
    ax2.set_xlabel('x [m]', fontsize=12)
    ax2.set_ylabel('z [m]', fontsize=12)
    ax2.set_title(f'Vectores de Campo Magnético\n(Plano XZ, y={y_value}m)', 
                  fontsize=14, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('plots/espira_circular_campo_2D_XZ.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/espira_circular_campo_2D_XZ.png")
    plt.show()


def graficar_campo_2D_plano_XY(radio, I):
    """
    Grafica el campo magnético en el plano XY (z=0.1m).
    Este plano es paralelo a la espira.
    """
    print(f"\nGenerando gráfico 2D (plano XY, z=0.1m)...")
    
    # Crear grilla en el plano XY
    x_range = (-0.4, 0.4)
    y_range = (-0.4, 0.4)
    z_value = 0.1
    
    # Función que calcula el campo para un punto
    def campo_en_punto(punto):
        return campo_magnetico_espira(punto, radio, I)
    
    # Calcular campo en la grilla
    X, Y, Bx, By, Bz = campo_magnetico_grilla(
        campo_en_punto, x_range, y_range, z_value, nx=25, ny=25
    )
    
    B_mag = magnitud_campo(Bx, By, Bz)
    
    # Crear figura
    fig, ax = plt.subplots(1, 1, figsize=(10, 9))
    
    # Mapa de color de magnitud
    contour = ax.contourf(X, Y, B_mag*1e6, levels=20, cmap='coolwarm', alpha=0.7)
    
    # Líneas de campo proyectadas en el plano
    speed = np.sqrt(Bx**2 + By**2)
    lw = 2 * speed / (speed.max() + 1e-10)
    
    stream = ax.streamplot(X, Y, Bx, By, color='black', linewidth=lw,
                          density=1.5, arrowsize=1.2, arrowstyle='->')
    
    # Dibujar la espira (proyección en el plano XY)
    theta_espira = np.linspace(0, 2*np.pi, 100)
    x_espira = radio * np.cos(theta_espira)
    y_espira = radio * np.sin(theta_espira)
    ax.plot(x_espira, y_espira, 'r-', linewidth=4, label=f'Espira (a={radio}m, z=0)', alpha=0.9)
    ax.plot([0], [0], 'ro', markersize=10, label='Centro')
    
    ax.set_xlabel('x [m]', fontsize=12)
    ax.set_ylabel('y [m]', fontsize=12)
    ax.set_title(f'Campo Magnético en Plano Paralelo a Espira\n(a={radio}m, I={I}A, z={z_value}m)', 
                fontsize=14, fontweight='bold')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    cbar = plt.colorbar(contour, ax=ax)
    cbar.set_label('|B| [μT]', fontsize=11)
    
    plt.tight_layout()
    plt.savefig('plots/espira_circular_campo_2D_XY.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/espira_circular_campo_2D_XY.png")
    plt.show()


def graficar_campo_3D(radio, I):
    """
    Grafica el campo magnético en 3D.
    """
    print(f"\nGenerando gráfico 3D...")
    
    # Crear figura 3D
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Grilla de puntos para vectores
    n_points = 10
    x = np.linspace(-0.3, 0.3, n_points)
    y = np.linspace(-0.3, 0.3, n_points)
    z = np.linspace(-0.3, 0.3, n_points)
    
    print("  Calculando campo en grilla 3D...")
    
    for i, xi in enumerate(x[::2]):
        for j, yj in enumerate(y[::2]):
            for k, zk in enumerate(z[::2]):
                punto = np.array([xi, yj, zk])
                
                # Evitar puntos muy cerca de la espira
                dist_to_ring = np.sqrt((np.sqrt(xi**2 + yj**2) - radio)**2 + zk**2)
                if dist_to_ring < 0.03:
                    continue
                
                B = campo_magnetico_espira(punto, radio, I)
                B_mag = np.linalg.norm(B)
                
                # Normalizar para visualización
                if B_mag > 1e-10:
                    B_norm = B / B_mag
                    
                    # Color basado en magnitud
                    color = plt.cm.plasma(min(B_mag*1e6 / 80, 1.0))
                    
                    # Dibujar vector
                    ax.quiver(xi, yj, zk, 
                             B_norm[0], B_norm[1], B_norm[2],
                             length=0.08, color=color, arrow_length_ratio=0.3,
                             linewidth=1.5, alpha=0.7)
    
    # Dibujar la espira
    theta_espira = np.linspace(0, 2*np.pi, 100)
    x_espira = radio * np.cos(theta_espira)
    y_espira = radio * np.sin(theta_espira)
    z_espira = np.zeros_like(theta_espira)
    ax.plot(x_espira, y_espira, z_espira, 'r-', linewidth=5, 
            label=f'Espira (a={radio}m, I={I}A)', alpha=0.9)
    
    # Marcar dirección de corriente con flecha
    idx_arrow = 25
    ax.quiver(x_espira[idx_arrow], y_espira[idx_arrow], z_espira[idx_arrow],
             x_espira[idx_arrow+1]-x_espira[idx_arrow],
             y_espira[idx_arrow+1]-y_espira[idx_arrow], 0,
             color='red', arrow_length_ratio=0.5, linewidth=3)
    
    ax.set_xlabel('x [m]', fontsize=11)
    ax.set_ylabel('y [m]', fontsize=11)
    ax.set_zlabel('z [m]', fontsize=11)
    ax.set_title('Campo Magnético de Espira Circular - Vista 3D', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    # Ajustar vista
    ax.set_xlim([-0.3, 0.3])
    ax.set_ylim([-0.3, 0.3])
    ax.set_zlim([-0.3, 0.3])
    
    plt.tight_layout()
    plt.savefig('plots/espira_circular_campo_3D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/espira_circular_campo_3D.png")
    plt.show()


def analisis_campo_en_eje(radio, I):
    """
    Analiza el campo magnético a lo largo del eje de la espira y compara
    con la fórmula analítica.
    """
    print(f"\nAnalizando campo en el eje de la espira...")
    
    # Posiciones en el eje z
    z_positions = np.linspace(-0.5, 0.5, 100)
    
    B_numerico = []
    B_analitico = []
    
    for z in z_positions:
        # Cálculo numérico
        punto = np.array([0.0, 0.0, z])
        B = campo_magnetico_espira(punto, radio, I)
        B_numerico.append(np.linalg.norm(B))
        
        # Fórmula analítica en el eje
        B_eje = campo_magnetico_espira_eje(z, radio, I)
        B_analitico.append(np.linalg.norm(B_eje))
    
    B_numerico = np.array(B_numerico)
    B_analitico = np.array(B_analitico)
    
    # Graficar
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Subplot 1: Campo vs posición
    ax1.plot(z_positions, B_numerico*1e6, 'b-', linewidth=2.5, 
            label='Biot-Savart (numérico)')
    ax1.plot(z_positions, B_analitico*1e6, 'r--', linewidth=2,
            label='Fórmula analítica')
    ax1.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
    ax1.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=radio, color='green', linestyle='--', alpha=0.3, label=f'z = ±a')
    ax1.axvline(x=-radio, color='green', linestyle='--', alpha=0.3)
    
    ax1.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax1.set_ylabel('|B| [μT]', fontsize=12)
    ax1.set_title(f'Campo Magnético en el Eje de la Espira\n(a={radio}m, I={I}A)', 
                  fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    
    # Subplot 2: Error relativo
    error_relativo = np.abs(B_numerico - B_analitico) / (B_analitico + 1e-15) * 100
    ax2.plot(z_positions, error_relativo, 'g-', linewidth=2.5)
    ax2.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax2.set_ylabel('Error relativo [%]', fontsize=12)
    ax2.set_title('Error: Numérico vs Analítico', 
                  fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim([0, max(5, np.max(error_relativo))])
    
    plt.tight_layout()
    plt.savefig('plots/espira_circular_campo_en_eje.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/espira_circular_campo_en_eje.png")
    plt.show()
    
    # Campo en el centro
    B_centro = campo_magnetico_espira(np.array([0, 0, 0]), radio, I)
    B_centro_teorico = (MU_0 * I) / (2 * radio)
    
    print(f"\nCampo en el centro de la espira (z=0):")
    print(f"  |B| (numérico) = {np.linalg.norm(B_centro):.6e} T")
    print(f"  |B| (teórico)  = {B_centro_teorico:.6e} T")
    print(f"  Error relativo = {abs(np.linalg.norm(B_centro) - B_centro_teorico)/B_centro_teorico*100:.3f}%")


def main():
    """
    Función principal que ejecuta todos los cálculos y visualizaciones.
    """
    # Calcular campo en punto específico
    radio, I, punto, B = calcular_campo_punto_especifico()
    
    # Graficar campo 2D en plano XZ
    graficar_campo_2D_plano_XZ(radio, I)
    
    # Graficar campo 2D en plano XY
    graficar_campo_2D_plano_XY(radio, I)
    
    # Graficar campo 3D
    graficar_campo_3D(radio, I)
    
    # Análisis en el eje
    analisis_campo_en_eje(radio, I)
    
    print("\n" + "="*70)
    print("INCISO B COMPLETADO")
    print("="*70)
    print("\nResumen:")
    print(f"  ✓ Campo calculado en punto ({punto[0]}, {punto[1]}, {punto[2]}) m")
    print(f"  ✓ B = {B} T")
    print(f"  ✓ Gráficos 2D (XZ y XY) y 3D generados")
    print(f"  ✓ Análisis de campo en el eje completado")
    print(f"  ✓ Validación con fórmulas analíticas")
    print(f"  ✓ Resultados guardados en carpeta 'plots/'")


if __name__ == "__main__":
    main()
