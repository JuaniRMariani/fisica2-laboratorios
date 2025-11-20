"""
Laboratorio 2 - Inciso C: Configuración Combinada (Alambre + Espira)

Calcula y visualiza el campo magnético total generado por un alambre recto
en el eje de una espira circular, aplicando el principio de superposición.

Universidad Nacional del Sur - Física II
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from biot_savart import (
    campo_magnetico_alambre_recto,
    campo_magnetico_espira,
    campo_magnetico_grilla,
    magnitud_campo,
    MU_0
)

# Configuración del sistema
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 10


def campo_combinado(punto, L_alambre, I_alambre, radio_espira, I_espira):
    """
    Calcula el campo magnético total usando el principio de superposición.
    
    B_total = B_alambre + B_espira
    
    Parámetros:
    -----------
    punto : np.ndarray
        Punto donde calcular el campo
    L_alambre : float
        Longitud del alambre [m]
    I_alambre : float
        Corriente en el alambre [A]
    radio_espira : float
        Radio de la espira [m]
    I_espira : float
        Corriente en la espira [A]
        
    Retorna:
    --------
    B_total, B_alambre, B_espira : np.ndarray
        Campos magnéticos total y de cada componente
    """
    # Campo del alambre (en el eje z)
    B_alambre = campo_magnetico_alambre_recto(punto, L_alambre, I_alambre)
    
    # Campo de la espira (en el plano XY)
    B_espira = campo_magnetico_espira(punto, radio_espira, I_espira)
    
    # Principio de superposición
    B_total = B_alambre + B_espira
    
    return B_total, B_alambre, B_espira


def calcular_campo_punto_especifico():
    """
    Calcula el campo magnético en un punto específico para la configuración combinada.
    """
    print("="*70)
    print("INCISO C: CONFIGURACIÓN COMBINADA (ALAMBRE + ESPIRA)")
    print("="*70)
    
    # Parámetros del sistema
    L_alambre = 2.0  # Longitud del alambre [m]
    I_alambre = 10.0  # Corriente en alambre [A]
    radio_espira = 0.2  # Radio de la espira [m]
    I_espira = 8.0  # Corriente en espira [A]
    
    print(f"\nParámetros del sistema:")
    print(f"  Alambre:")
    print(f"    - Longitud: L = {L_alambre} m")
    print(f"    - Corriente: I₁ = {I_alambre} A")
    print(f"    - Posición: eje z, centrado en origen")
    print(f"  Espira:")
    print(f"    - Radio: a = {radio_espira} m")
    print(f"    - Corriente: I₂ = {I_espira} A")
    print(f"    - Posición: plano XY, centrada en origen")
    print(f"    - El alambre pasa por el eje de la espira")
    
    # Punto específico donde calcular el campo
    punto = np.array([0.15, 0.1, 0.25])  # [m]
    
    # Calcular campos
    B_total, B_alambre, B_espira = campo_combinado(
        punto, L_alambre, I_alambre, radio_espira, I_espira
    )
    
    print(f"\nPunto de evaluación: r = ({punto[0]}, {punto[1]}, {punto[2]}) m")
    
    print(f"\n" + "-"*70)
    print("CAMPO DEL ALAMBRE:")
    print("-"*70)
    print(f"  B_alambre = ({B_alambre[0]:.6e}, {B_alambre[1]:.6e}, {B_alambre[2]:.6e}) T")
    print(f"  |B_alambre| = {np.linalg.norm(B_alambre):.6e} T = {np.linalg.norm(B_alambre)*1e6:.4f} μT")
    
    print(f"\n" + "-"*70)
    print("CAMPO DE LA ESPIRA:")
    print("-"*70)
    print(f"  B_espira = ({B_espira[0]:.6e}, {B_espira[1]:.6e}, {B_espira[2]:.6e}) T")
    print(f"  |B_espira| = {np.linalg.norm(B_espira):.6e} T = {np.linalg.norm(B_espira)*1e6:.4f} μT")
    
    print(f"\n" + "-"*70)
    print("CAMPO TOTAL (SUPERPOSICIÓN):")
    print("-"*70)
    print(f"  B_total = B_alambre + B_espira")
    print(f"  B_total = ({B_total[0]:.6e}, {B_total[1]:.6e}, {B_total[2]:.6e}) T")
    print(f"  B_total = {B_total[0]:.6e} x̂ + {B_total[1]:.6e} ŷ + {B_total[2]:.6e} ẑ [T]")
    print(f"  |B_total| = {np.linalg.norm(B_total):.6e} T = {np.linalg.norm(B_total)*1e6:.4f} μT")
    
    # Análisis de contribuciones
    print(f"\n" + "-"*70)
    print("ANÁLISIS DE CONTRIBUCIONES:")
    print("-"*70)
    contrib_alambre = np.linalg.norm(B_alambre) / np.linalg.norm(B_total) * 100
    contrib_espira = np.linalg.norm(B_espira) / np.linalg.norm(B_total) * 100
    print(f"  Contribución del alambre: {contrib_alambre:.2f}%")
    print(f"  Contribución de la espira: {contrib_espira:.2f}%")
    
    # Ángulo entre los campos
    if np.linalg.norm(B_alambre) > 1e-15 and np.linalg.norm(B_espira) > 1e-15:
        cos_angulo = np.dot(B_alambre, B_espira) / (np.linalg.norm(B_alambre) * np.linalg.norm(B_espira))
        angulo = np.arccos(np.clip(cos_angulo, -1, 1)) * 180 / np.pi
        print(f"  Ángulo entre B_alambre y B_espira: {angulo:.2f}°")
    
    return L_alambre, I_alambre, radio_espira, I_espira, punto, B_total


def graficar_campo_2D_comparacion(L_alambre, I_alambre, radio_espira, I_espira):
    """
    Grafica comparación de campos individuales y combinado en el plano XZ (y=0).
    Muestra la magnitud total del campo 3D con vectores proyectados en el plano.
    """
    print(f"\nGenerando gráficos 2D de comparación (plano XZ)...")
    
    # Crear grilla en el plano XZ
    nx, nz = 35, 35
    x = np.linspace(-0.5, 0.5, nx)
    z = np.linspace(-0.5, 0.5, nz)
    X, Z = np.meshgrid(x, z)
    y_value = 0.0
    
    # Inicializar arrays para almacenar las 3 componentes
    B_alambre_x = np.zeros_like(X)
    B_alambre_y = np.zeros_like(X)
    B_alambre_z = np.zeros_like(X)
    B_espira_x = np.zeros_like(X)
    B_espira_y = np.zeros_like(X)
    B_espira_z = np.zeros_like(X)
    B_total_x = np.zeros_like(X)
    B_total_y = np.zeros_like(X)
    B_total_z = np.zeros_like(X)
    
    print("  Calculando campos en grilla XZ...")
    for i in range(nz):
        for j in range(nx):
            punto = np.array([X[i, j], y_value, Z[i, j]])
            
            # Campos individuales
            B_a = campo_magnetico_alambre_recto(punto, L_alambre, I_alambre)
            B_e = campo_magnetico_espira(punto, radio_espira, I_espira)
            B_t = B_a + B_e
            
            # Alambre: guardamos todas las componentes
            B_alambre_x[i, j] = B_a[0]
            B_alambre_y[i, j] = B_a[1]
            B_alambre_z[i, j] = B_a[2]
            
            # Espira: guardamos todas las componentes
            B_espira_x[i, j] = B_e[0]
            B_espira_y[i, j] = B_e[1]
            B_espira_z[i, j] = B_e[2]
            
            # Total
            B_total_x[i, j] = B_t[0]
            B_total_y[i, j] = B_t[1]
            B_total_z[i, j] = B_t[2]
    
    # Magnitudes TOTALES en 3D (no solo en el plano)
    B_alambre_mag = np.sqrt(B_alambre_x**2 + B_alambre_y**2 + B_alambre_z**2)
    B_espira_mag = np.sqrt(B_espira_x**2 + B_espira_y**2 + B_espira_z**2)
    B_total_mag = np.sqrt(B_total_x**2 + B_total_y**2 + B_total_z**2)
    
    # Crear figura con 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    
    # --- Subplot 1: Campo del Alambre ---
    ax1 = axes[0]
    # Mostrar magnitud total 3D
    contour1 = ax1.contourf(X, Z, B_alambre_mag*1e6, levels=15, cmap='Blues', alpha=0.7)
    
    # Usar quiver (flechas) en lugar de streamplot para mejor visualización
    # Submuestrear la grilla para no saturar de flechas
    skip = 3
    X_sub = X[::skip, ::skip]
    Z_sub = Z[::skip, ::skip]
    Bx_sub = B_alambre_x[::skip, ::skip]
    Bz_sub = B_alambre_z[::skip, ::skip]
    
    # Normalizar las flechas por la magnitud del campo
    B_mag_sub = np.sqrt(Bx_sub**2 + Bz_sub**2)
    # Evitar divisiones por cero
    B_mag_sub_safe = np.where(B_mag_sub > 1e-12, B_mag_sub, 1e-12)
    
    # Quiver con flechas proporcionales a la magnitud
    ax1.quiver(X_sub, Z_sub, Bx_sub/B_mag_sub_safe, Bz_sub/B_mag_sub_safe,
               B_mag_sub*1e6, cmap='Blues', scale=25, width=0.004, 
               headwidth=4, headlength=5, alpha=0.9)
    
    # Dibujar alambre (línea vertical en x=0)
    ax1.plot([0, 0], [-0.5, 0.5], 'r-', linewidth=4, alpha=0.8, label='Alambre (eje Z)')
    ax1.set_xlabel('x [m]', fontsize=11)
    ax1.set_ylabel('z [m]', fontsize=11)
    ax1.set_title(f'Campo del Alambre (plano XZ, y=0)\n(I₁={I_alambre}A, L={L_alambre}m)', 
                  fontsize=12, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    cbar1 = plt.colorbar(contour1, ax=ax1)
    cbar1.set_label('|B| [μT]', fontsize=10)
    
    # --- Subplot 2: Campo de la Espira ---
    ax2 = axes[1]
    contour2 = ax2.contourf(X, Z, B_espira_mag*1e6, levels=15, cmap='Reds', alpha=0.7)
    # Para la espira, las líneas en plano XZ muestran componentes x,z
    speed2 = np.sqrt(B_espira_x**2 + B_espira_z**2)
    lw2 = 2 * speed2 / (speed2.max() + 1e-10)
    ax2.streamplot(X, Z, B_espira_x, B_espira_z, color='darkred', 
                   linewidth=lw2, density=1.8, arrowsize=1.2)
    
    # Dibujar espira (vista de perfil: dos puntos en z=0)
    ax2.plot([-radio_espira, radio_espira], [0, 0], 'bo', markersize=10, 
             label=f'Espira (a={radio_espira}m)')
    ax2.plot([-radio_espira, radio_espira], [0, 0], 'b-', linewidth=3, alpha=0.5)
    ax2.set_xlabel('x [m]', fontsize=11)
    ax2.set_ylabel('z [m]', fontsize=11)
    ax2.set_title(f'Campo de la Espira (plano XZ, y=0)\n(I₂={I_espira}A, a={radio_espira}m)', 
                  fontsize=12, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    cbar2 = plt.colorbar(contour2, ax=ax2)
    cbar2.set_label('|B| [μT]', fontsize=10)
    
    # --- Subplot 3: Campo Total (Superposición) ---
    ax3 = axes[2]
    contour3 = ax3.contourf(X, Z, B_total_mag*1e6, levels=15, cmap='viridis', alpha=0.7)
    
    # Usar quiver para flechas (consistente con alambre)
    skip = 3
    X_sub3 = X[::skip, ::skip]
    Z_sub3 = Z[::skip, ::skip]
    Bx_sub3 = B_total_x[::skip, ::skip]
    Bz_sub3 = B_total_z[::skip, ::skip]
    
    B_mag_sub3 = np.sqrt(Bx_sub3**2 + Bz_sub3**2)
    B_mag_sub3_safe = np.where(B_mag_sub3 > 1e-12, B_mag_sub3, 1e-12)
    
    ax3.quiver(X_sub3, Z_sub3, Bx_sub3/B_mag_sub3_safe, Bz_sub3/B_mag_sub3_safe,
               B_mag_sub3*1e6, cmap='plasma', scale=25, width=0.004,
               headwidth=4, headlength=5, alpha=0.9)
    
    # Dibujar ambos elementos
    ax3.plot([0, 0], [-0.5, 0.5], 'r-', linewidth=4, alpha=0.8, label='Alambre')
    ax3.plot([-radio_espira, radio_espira], [0, 0], 'co', markersize=10, label='Espira')
    ax3.plot([-radio_espira, radio_espira], [0, 0], 'c-', linewidth=3, alpha=0.5)
    ax3.set_xlabel('x [m]', fontsize=11)
    ax3.set_ylabel('z [m]', fontsize=11)
    ax3.set_title('Campo Total (Superposición, plano XZ, y=0)\nB = B_alambre + B_espira', 
                  fontsize=12, fontweight='bold')
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    cbar3 = plt.colorbar(contour3, ax=ax3)
    cbar3.set_label('|B| [μT]', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('plots/alambre_espira_combinados_comparacion_2D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_espira_combinados_comparacion_2D.png")
    plt.show()


def graficar_campo_3D_combinado(L_alambre, I_alambre, radio_espira, I_espira):
    """
    Grafica el campo magnético combinado en 3D.
    """
    print(f"\nGenerando gráfico 3D de configuración combinada...")
    
    # Crear figura 3D
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Grilla de puntos
    n_points = 10
    x = np.linspace(-0.4, 0.4, n_points)
    y = np.linspace(-0.4, 0.4, n_points)
    z = np.linspace(-0.6, 0.6, n_points)
    
    print("  Calculando campo combinado en grilla 3D...")
    
    for xi in x[::2]:
        for yj in y[::2]:
            for zk in z[::2]:
                punto = np.array([xi, yj, zk])
                
                # Evitar puntos muy cerca de los conductores
                dist_alambre = np.sqrt(xi**2 + yj**2)
                dist_espira = np.sqrt((np.sqrt(xi**2 + yj**2) - radio_espira)**2 + zk**2)
                
                if dist_alambre < 0.05 or dist_espira < 0.03:
                    continue
                
                B_total, _, _ = campo_combinado(punto, L_alambre, I_alambre, 
                                               radio_espira, I_espira)
                B_mag = np.linalg.norm(B_total)
                
                if B_mag > 1e-10:
                    B_norm = B_total / B_mag
                    
                    # Color basado en magnitud
                    color = plt.cm.plasma(min(B_mag*1e6 / 100, 1.0))
                    
                    # Dibujar vector
                    ax.quiver(xi, yj, zk, 
                             B_norm[0], B_norm[1], B_norm[2],
                             length=0.1, color=color, arrow_length_ratio=0.3,
                             linewidth=1.5, alpha=0.7)
    
    # Dibujar el alambre
    z_alambre = np.linspace(-L_alambre/2, L_alambre/2, 100)
    x_alambre = np.zeros_like(z_alambre)
    y_alambre = np.zeros_like(z_alambre)
    ax.plot(x_alambre, y_alambre, z_alambre, 'r-', linewidth=5, 
            label=f'Alambre (I₁={I_alambre}A)', alpha=0.9)
    
    # Dibujar la espira
    theta = np.linspace(0, 2*np.pi, 100)
    x_espira = radio_espira * np.cos(theta)
    y_espira = radio_espira * np.sin(theta)
    z_espira = np.zeros_like(theta)
    ax.plot(x_espira, y_espira, z_espira, 'b-', linewidth=5, 
            label=f'Espira (I₂={I_espira}A)', alpha=0.9)
    
    ax.set_xlabel('x [m]', fontsize=11)
    ax.set_ylabel('y [m]', fontsize=11)
    ax.set_zlabel('z [m]', fontsize=11)
    ax.set_title('Campo Magnético Combinado - Vista 3D\n(Alambre en eje de Espira)', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    ax.set_xlim([-0.4, 0.4])
    ax.set_ylim([-0.4, 0.4])
    ax.set_zlim([-0.6, 0.6])
    
    plt.tight_layout()
    plt.savefig('plots/alambre_espira_combinados_campo_3D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_espira_combinados_campo_3D.png")
    plt.show()


def analisis_campo_en_eje_z(L_alambre, I_alambre, radio_espira, I_espira):
    """
    Analiza el campo magnético a lo largo del eje z.
    """
    print(f"\nAnalizando campo a lo largo del eje z...")
    
    z_positions = np.linspace(-0.8, 0.8, 150)
    
    B_total_mag = []
    B_alambre_mag = []
    B_espira_mag = []
    
    for z in z_positions:
        punto = np.array([0.0, 0.0, z])
        B_t, B_a, B_e = campo_combinado(punto, L_alambre, I_alambre, 
                                        radio_espira, I_espira)
        B_total_mag.append(np.linalg.norm(B_t))
        B_alambre_mag.append(np.linalg.norm(B_a))
        B_espira_mag.append(np.linalg.norm(B_e))
    
    B_total_mag = np.array(B_total_mag)
    B_alambre_mag = np.array(B_alambre_mag)
    B_espira_mag = np.array(B_espira_mag)
    
    # Graficar
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    
    ax.plot(z_positions, B_total_mag*1e6, 'g-', linewidth=3, 
            label='Campo Total (superposición)')
    ax.plot(z_positions, B_alambre_mag*1e6, 'r--', linewidth=2, 
            label='Campo del Alambre', alpha=0.7)
    ax.plot(z_positions, B_espira_mag*1e6, 'b--', linewidth=2, 
            label='Campo de la Espira', alpha=0.7)
    
    # Marcar posición de la espira
    ax.axvline(x=0, color='gray', linestyle=':', alpha=0.5, label='Plano de la espira')
    ax.axvline(x=radio_espira, color='cyan', linestyle=':', alpha=0.3)
    ax.axvline(x=-radio_espira, color='cyan', linestyle=':', alpha=0.3)
    
    ax.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax.set_ylabel('|B| [μT]', fontsize=12)
    ax.set_title(f'Campo Magnético en el Eje z\n(Alambre + Espira)', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('plots/alambre_espira_combinados_campo_eje_z.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_espira_combinados_campo_eje_z.png")
    plt.show()
    
    # Punto de máximo campo
    idx_max = np.argmax(B_total_mag)
    print(f"\nCampo máximo en el eje z:")
    print(f"  Posición: z = {z_positions[idx_max]:.3f} m")
    print(f"  |B_total| = {B_total_mag[idx_max]*1e6:.2f} μT")


def main():
    """
    Función principal que ejecuta todos los cálculos y visualizaciones.
    """
    # Calcular campo en punto específico
    L_alambre, I_alambre, radio_espira, I_espira, punto, B_total = \
        calcular_campo_punto_especifico()
    
    # Gráficos 2D comparativos
    graficar_campo_2D_comparacion(L_alambre, I_alambre, radio_espira, I_espira)
    
    # Gráfico 3D combinado
    graficar_campo_3D_combinado(L_alambre, I_alambre, radio_espira, I_espira)
    
    # Análisis en eje z
    analisis_campo_en_eje_z(L_alambre, I_alambre, radio_espira, I_espira)
    
    print("\n" + "="*70)
    print("INCISO C COMPLETADO")
    print("="*70)
    print("\nResumen:")
    print(f"  ✓ Principio de superposición aplicado correctamente")
    print(f"  ✓ Campo total = Campo alambre + Campo espira")
    print(f"  ✓ Campo calculado en punto ({punto[0]}, {punto[1]}, {punto[2]}) m")
    print(f"  ✓ |B_total| = {np.linalg.norm(B_total)*1e6:.4f} μT")
    print(f"  ✓ Gráficos comparativos 2D y 3D generados")
    print(f"  ✓ Análisis en eje z completado")
    print(f"  ✓ Resultados guardados en carpeta 'plots/'")


if __name__ == "__main__":
    main()
