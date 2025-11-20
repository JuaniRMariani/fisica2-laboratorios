"""
Laboratorio 2 - Inciso A: Campo Magnético de Alambre Recto

Calcula y visualiza el campo magnético generado por un alambre recto
de longitud L con corriente I.

Universidad Nacional del Sur - Física II
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from biot_savart import (
    campo_magnetico_alambre_recto,
    campo_magnetico_grilla,
    magnitud_campo,
    MU_0
)

# Configuración del sistema
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 10


def calcular_campo_punto_especifico():
    """
    Calcula el campo magnético en un punto específico para el alambre recto.
    """
    print("="*70)
    print("INCISO A: CAMPO MAGNÉTICO DE ALAMBRE RECTO")
    print("="*70)
    
    # Parámetros del alambre
    L = 2.0  # Longitud del alambre [m]
    I = 10.0  # Corriente [A]
    
    # Punto específico donde calcular el campo
    punto = np.array([0.2, 0.15, 0.0])  # [m]
    
    print(f"\nParámetros del alambre:")
    print(f"  Longitud: L = {L} m")
    print(f"  Corriente: I = {I} A")
    print(f"  Posición: centro en el origen")
    print(f"  Dirección: eje z")
    
    # Calcular campo magnético
    B = campo_magnetico_alambre_recto(punto, L, I)
    B_magnitud = np.linalg.norm(B)
    
    print(f"\nPunto de evaluación: r = ({punto[0]}, {punto[1]}, {punto[2]}) m")
    print(f"\nCampo magnético en forma vectorial:")
    print(f"  B = ({B[0]:.6e}, {B[1]:.6e}, {B[2]:.6e}) T")
    print(f"  B = {B[0]:.6e} x̂ + {B[1]:.6e} ŷ + {B[2]:.6e} ẑ [T]")
    print(f"\nMagnitud del campo:")
    print(f"  |B| = {B_magnitud:.6e} T")
    print(f"  |B| = {B_magnitud*1e6:.4f} μT")
    
    # Análisis del resultado
    print(f"\n" + "-"*70)
    print("ANÁLISIS:")
    print("-"*70)
    
    # Distancia perpendicular al alambre
    rho = np.sqrt(punto[0]**2 + punto[1]**2)
    print(f"Distancia perpendicular al alambre: ρ = {rho:.3f} m")
    
    # Campo de alambre infinito (para comparación)
    B_infinito = (MU_0 * I) / (2 * np.pi * rho)
    print(f"Campo de alambre infinito (comparación): {B_infinito:.6e} T")
    print(f"Relación B_finito/B_infinito: {B_magnitud/B_infinito:.3f}")
    
    return L, I, punto, B


def graficar_campo_2D(L, I):
    """
    Grafica el campo magnético en el plano XY (z=0).
    """
    print(f"\nGenerando gráfico 2D (plano XY, z=0)...")
    
    # Crear grilla en el plano XY
    x_range = (-0.5, 0.5)
    y_range = (-0.5, 0.5)
    z_value = 0.0
    
    # Función que calcula el campo para un punto
    def campo_en_punto(punto):
        return campo_magnetico_alambre_recto(punto, L, I)
    
    # Calcular campo en la grilla
    X, Y, Bx, By, Bz = campo_magnetico_grilla(
        campo_en_punto, x_range, y_range, z_value, nx=25, ny=25
    )
    
    # Magnitud del campo
    B_mag = magnitud_campo(Bx, By, Bz)
    
    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Subplot 1: Líneas de campo con mapa de color
    levels = np.linspace(0, np.max(B_mag)*0.8, 20)
    contour = ax1.contourf(X, Y, B_mag*1e6, levels=20, cmap='viridis', alpha=0.7)
    
    # Líneas de campo (streamplot)
    # Normalizar para mejor visualización
    speed = np.sqrt(Bx**2 + By**2)
    lw = 2 * speed / speed.max()
    
    stream = ax1.streamplot(X, Y, Bx, By, color='white', linewidth=lw,
                            density=1.5, arrowsize=1.2, arrowstyle='->')
    
    # Marcar la posición del alambre (sección transversal)
    # Círculo que representa el corte del alambre perpendicular a z
    circle = plt.Circle((0, 0), 0.02, color='red', alpha=0.9, zorder=10, 
                        label='Alambre (⊙ perpendicular)')
    ax1.add_patch(circle)
    ax1.plot([0], [0], 'w+', markersize=8, markeredgewidth=2, zorder=11)
    
    ax1.set_xlabel('x [m]', fontsize=12)
    ax1.set_ylabel('y [m]', fontsize=12)
    ax1.set_title(f'Líneas de Campo Magnético - Alambre Recto\n(L={L}m, I={I}A, plano z={z_value}m)', 
                  fontsize=14, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    
    cbar1 = plt.colorbar(contour, ax=ax1)
    cbar1.set_label('|B| [μT]', fontsize=11)
    
    # Subplot 2: Vectores del campo
    # Submuestrear para mejor visualización
    skip = 2
    ax2.quiver(X[::skip, ::skip], Y[::skip, ::skip], 
               Bx[::skip, ::skip], By[::skip, ::skip],
               B_mag[::skip, ::skip]*1e6, cmap='plasma', 
               scale=np.max(B_mag)*30, width=0.004)
    
    # Marcar el alambre (sección transversal)
    circle2 = plt.Circle((0, 0), 0.02, color='red', alpha=0.9, zorder=10,
                         label='Alambre (⊙ perpendicular)')
    ax2.add_patch(circle2)
    ax2.plot([0], [0], 'w+', markersize=8, markeredgewidth=2, zorder=11)
    
    ax2.set_xlabel('x [m]', fontsize=12)
    ax2.set_ylabel('y [m]', fontsize=12)
    ax2.set_title(f'Vectores de Campo Magnético\n(Plano XY, z={z_value}m)', 
                  fontsize=14, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('plots/alambre_recto_campo_2D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_recto_campo_2D.png")
    plt.show()


def graficar_campo_3D(L, I):
    """
    Grafica el campo magnético en 3D.
    """
    print(f"\nGenerando gráfico 3D...")
    
    # Crear grilla 3D
    n_points = 12
    x = np.linspace(-0.4, 0.4, n_points)
    y = np.linspace(-0.4, 0.4, n_points)
    z = np.linspace(-0.8, 0.8, n_points)
    
    # Crear figura 3D
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Calcular campo en puntos seleccionados
    print("  Calculando campo en grilla 3D...")
    
    # Usar menos puntos para visualización 3D
    for i, xi in enumerate(x[::2]):
        for j, yj in enumerate(y[::2]):
            for k, zk in enumerate(z[::2]):
                punto = np.array([xi, yj, zk])
                
                # Evitar puntos muy cerca del alambre
                if np.sqrt(xi**2 + yj**2) < 0.05:
                    continue
                
                B = campo_magnetico_alambre_recto(punto, L, I)
                B_mag = np.linalg.norm(B)
                
                # Normalizar para visualización
                if B_mag > 1e-10:
                    B_norm = B / B_mag
                    
                    # Color basado en magnitud
                    color = plt.cm.plasma(min(B_mag*1e6 / 100, 1.0))
                    
                    # Dibujar vector
                    ax.quiver(xi, yj, zk, 
                             B_norm[0], B_norm[1], B_norm[2],
                             length=0.1, color=color, arrow_length_ratio=0.3,
                             linewidth=1.5, alpha=0.7)
    
    # Dibujar el alambre
    z_alambre = np.linspace(-L/2, L/2, 100)
    x_alambre = np.zeros_like(z_alambre)
    y_alambre = np.zeros_like(z_alambre)
    ax.plot(x_alambre, y_alambre, z_alambre, 'r-', linewidth=5, 
            label=f'Alambre (L={L}m, I={I}A)', alpha=0.9)
    
    ax.set_xlabel('x [m]', fontsize=11)
    ax.set_ylabel('y [m]', fontsize=11)
    ax.set_zlabel('z [m]', fontsize=11)
    ax.set_title('Campo Magnético de Alambre Recto - Vista 3D', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    # Ajustar vista
    ax.set_xlim([-0.4, 0.4])
    ax.set_ylim([-0.4, 0.4])
    ax.set_zlim([-0.8, 0.8])
    
    plt.tight_layout()
    plt.savefig('plots/alambre_recto_campo_3D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_recto_campo_3D.png")
    plt.show()


def analisis_variacion_distancia(L, I):
    """
    Analiza cómo varía la magnitud del campo con la distancia.
    """
    print(f"\nAnalizando variación del campo con la distancia...")
    
    # Distancias perpendiculares al alambre
    distancias = np.logspace(-2, 0, 50)  # De 1 cm a 1 m
    
    B_magnitudes = []
    B_teoria_infinito = []
    
    for d in distancias:
        punto = np.array([d, 0.0, 0.0])
        B = campo_magnetico_alambre_recto(punto, L, I)
        B_magnitudes.append(np.linalg.norm(B))
        
        # Teoría alambre infinito: B = μ₀I/(2πρ)
        B_inf = (MU_0 * I) / (2 * np.pi * d)
        B_teoria_infinito.append(B_inf)
    
    B_magnitudes = np.array(B_magnitudes)
    B_teoria_infinito = np.array(B_teoria_infinito)
    
    # Graficar
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Subplot 1: Escala log-log
    ax1.loglog(distancias, B_magnitudes*1e6, 'b-', linewidth=2.5, 
               label='Biot-Savart (alambre finito)')
    ax1.loglog(distancias, B_teoria_infinito*1e6, 'r--', linewidth=2,
               label='Teoría (alambre infinito)')
    ax1.set_xlabel('Distancia perpendicular ρ [m]', fontsize=12)
    ax1.set_ylabel('|B| [μT]', fontsize=12)
    ax1.set_title('Variación del Campo con la Distancia\n(Escala log-log)', 
                  fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, which='both')
    ax1.legend(fontsize=11)
    
    # Subplot 2: Error relativo
    error_relativo = np.abs(B_magnitudes - B_teoria_infinito) / B_teoria_infinito * 100
    ax2.semilogx(distancias, error_relativo, 'g-', linewidth=2.5)
    ax2.set_xlabel('Distancia perpendicular ρ [m]', fontsize=12)
    ax2.set_ylabel('Error relativo [%]', fontsize=12)
    ax2.set_title('Error Relativo: Finito vs Infinito', 
                  fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=5, color='r', linestyle='--', alpha=0.5, label='5% error')
    ax2.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('plots/alambre_recto_variacion_distancia.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/alambre_recto_variacion_distancia.png")
    plt.show()
    
    print(f"\nObservaciones:")
    print(f"  - El campo decrece aproximadamente como 1/ρ")
    print(f"  - Para distancias pequeñas (ρ << L), el comportamiento es similar al infinito")
    print(f"  - El error es < 5% cuando ρ < {distancias[np.where(error_relativo < 5)[0][-1]]:.3f} m")


def main():
    """
    Función principal que ejecuta todos los cálculos y visualizaciones.
    """
    # Calcular campo en punto específico
    L, I, punto, B = calcular_campo_punto_especifico()
    
    # Graficar campo 2D
    graficar_campo_2D(L, I)
    
    # Graficar campo 3D
    graficar_campo_3D(L, I)
    
    # Análisis de variación con distancia
    analisis_variacion_distancia(L, I)
    
    print("\n" + "="*70)
    print("INCISO A COMPLETADO")
    print("="*70)
    print("\nResumen:")
    print(f"  ✓ Campo calculado en punto ({punto[0]}, {punto[1]}, {punto[2]}) m")
    print(f"  ✓ B = {B} T")
    print(f"  ✓ Gráficos 2D y 3D generados")
    print(f"  ✓ Análisis de variación con distancia completado")
    print(f"  ✓ Resultados guardados en carpeta 'plots/'")
    

if __name__ == "__main__":
    main()
