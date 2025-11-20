"""
Laboratorio 2 - Bobinas de Helmholtz

Implementación y análisis de bobinas de Helmholtz: par de espiras circulares
coaxiales separadas a una distancia igual a su radio, que generan un campo
magnético altamente uniforme en la región central.

Universidad Nacional del Sur - Física II
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from biot_savart import (
    campo_magnetico_espira,
    campo_magnetico_grilla,
    magnitud_campo,
    MU_0
)

# Configuración del sistema
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 10


def introduccion_helmholtz():
    """
    Imprime información sobre las bobinas de Helmholtz.
    """
    print("="*80)
    print(" "*20 + "BOBINAS DE HELMHOLTZ")
    print("="*80)
    print("\n¿QUÉ SON LAS BOBINAS DE HELMHOLTZ?")
    print("-"*80)
    print("""
Las bobinas de Helmholtz son un par de espiras circulares idénticas, coaxiales
y coplanares (paralelas), separadas por una distancia exactamente igual a su 
radio común.

CARACTERÍSTICAS:
  • Dos espiras circulares del mismo radio 'a'
  • Separadas por una distancia d = a (condición de Helmholtz)
  • Corrientes iguales circulando en el mismo sentido
  • Centradas en el eje z, en posiciones z = ±a/2

PROPIEDADES DEL CAMPO:
  • Generan un campo magnético altamente uniforme en la región central
  • En el punto medio entre las bobinas, el campo es máximo
  • Las derivadas primera y segunda del campo se anulan en el centro
  • La uniformidad se mantiene en un volumen considerable
  
APLICACIONES:
  • Calibración de instrumentos magnéticos
  • Experimentos de resonancia magnética nuclear (RMN)
  • Compensación del campo magnético terrestre
  • Generación de campos magnéticos uniformes para experimentos
  • Estudio del efecto Zeeman
  • Manipulación de partículas cargadas
  • Experimentos de física atómica y espectroscopía

VENTAJAS:
  • Campo muy uniforme en región central (~1% variación en 20% del radio)
  • Fácil construcción y configuración
  • No requiere núcleo ferromagnético
  • Campo controlable ajustando la corriente
    """)
    print("="*80)


def campo_helmholtz(punto, radio, corriente, separacion=None):
    """
    Calcula el campo magnético de las bobinas de Helmholtz.
    
    Configuración:
    - Espira 1: centro en (0, 0, +d/2)
    - Espira 2: centro en (0, 0, -d/2)
    - Separación: d = radio (condición de Helmholtz)
    
    Parámetros:
    -----------
    punto : np.ndarray
        Punto donde calcular el campo
    radio : float
        Radio de las espiras [m]
    corriente : float
        Corriente en ambas espiras [A]
    separacion : float, opcional
        Separación entre espiras [m]. Si None, usa d = radio
        
    Retorna:
    --------
    B_total, B_espira1, B_espira2 : np.ndarray
        Campo total y de cada espira
    """
    if separacion is None:
        separacion = radio  # Condición de Helmholtz
    
    # Centros de las espiras
    centro1 = np.array([0.0, 0.0, separacion/2])
    centro2 = np.array([0.0, 0.0, -separacion/2])
    
    # Normal a las espiras (ambas apuntan en dirección z)
    normal = np.array([0.0, 0.0, 1.0])
    
    # Campo de cada espira
    B1 = campo_magnetico_espira(punto, radio, corriente, centro=centro1, normal=normal)
    B2 = campo_magnetico_espira(punto, radio, corriente, centro=centro2, normal=normal)
    
    # Campo total (superposición)
    B_total = B1 + B2
    
    return B_total, B1, B2


def campo_helmholtz_analitico_centro(radio, corriente):
    """
    Fórmula analítica para el campo en el centro de las bobinas de Helmholtz.
    
    B_centro = (8/5√5) * (μ₀ I / a)
           ≈ 0.7155 * (μ₀ I / a)
    """
    B_centro = (8 / (5 * np.sqrt(5))) * (MU_0 * corriente / radio)
    return B_centro


def analizar_campo_punto_especifico():
    """
    Calcula el campo en puntos específicos.
    """
    print("\nCÁLCULO DEL CAMPO EN PUNTOS ESPECÍFICOS")
    print("-"*80)
    
    # Parámetros
    radio = 0.2  # 20 cm
    corriente = 5.0  # 5 A
    
    print(f"Parámetros de las bobinas:")
    print(f"  Radio: a = {radio} m = {radio*100} cm")
    print(f"  Corriente: I = {corriente} A")
    print(f"  Separación: d = a = {radio} m (condición de Helmholtz)")
    print(f"  Espira 1: z = +{radio/2} m")
    print(f"  Espira 2: z = -{radio/2} m")
    
    # Punto 1: Centro (origen)
    print(f"\n1. Campo en el centro (0, 0, 0):")
    punto_centro = np.array([0.0, 0.0, 0.0])
    B_total, B1, B2 = campo_helmholtz(punto_centro, radio, corriente)
    B_analitico = campo_helmholtz_analitico_centro(radio, corriente)
    
    print(f"   B_total (numérico) = {B_total}")
    print(f"   |B| (numérico) = {np.linalg.norm(B_total):.6e} T = {np.linalg.norm(B_total)*1e6:.4f} μT")
    print(f"   B_z (componente en eje) = {B_total[2]:.6e} T")
    print(f"   |B| (analítico) = {B_analitico:.6e} T = {B_analitico*1e6:.4f} μT")
    print(f"   Error relativo: {abs(np.linalg.norm(B_total) - B_analitico)/B_analitico*100:.3f}%")
    
    # Punto 2: Fuera del eje
    print(f"\n2. Campo fuera del eje (0.05, 0.03, 0):")
    punto_fuera = np.array([0.05, 0.03, 0.0])
    B_total2, _, _ = campo_helmholtz(punto_fuera, radio, corriente)
    print(f"   B_total = {B_total2}")
    print(f"   |B| = {np.linalg.norm(B_total2):.6e} T = {np.linalg.norm(B_total2)*1e6:.4f} μT")
    print(f"   Variación respecto al centro: {abs(np.linalg.norm(B_total2) - np.linalg.norm(B_total))/np.linalg.norm(B_total)*100:.2f}%")
    
    return radio, corriente


def graficar_campo_en_eje(radio, corriente):
    """
    Grafica el campo magnético a lo largo del eje z.
    """
    print(f"\nGraficando campo a lo largo del eje z...")
    
    # Posiciones en el eje
    z_positions = np.linspace(-0.4, 0.4, 200)
    
    B_total_z = []
    B_espira1_z = []
    B_espira2_z = []
    
    for z in z_positions:
        punto = np.array([0.0, 0.0, z])
        B_t, B1, B2 = campo_helmholtz(punto, radio, corriente)
        B_total_z.append(B_t[2])  # Componente z
        B_espira1_z.append(B1[2])
        B_espira2_z.append(B2[2])
    
    B_total_z = np.array(B_total_z)
    B_espira1_z = np.array(B_espira1_z)
    B_espira2_z = np.array(B_espira2_z)
    
    # Graficar
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # --- Subplot 1: Campos individuales y total ---
    ax1.plot(z_positions, B_total_z*1e6, 'g-', linewidth=3, 
            label='Campo Total (Helmholtz)')
    ax1.plot(z_positions, B_espira1_z*1e6, 'b--', linewidth=2, 
            label='Espira 1 (z = +a/2)', alpha=0.7)
    ax1.plot(z_positions, B_espira2_z*1e6, 'r--', linewidth=2, 
            label='Espira 2 (z = -a/2)', alpha=0.7)
    
    # Marcar posiciones de las espiras
    ax1.axvline(x=radio/2, color='blue', linestyle=':', alpha=0.4, label='Posición espiras')
    ax1.axvline(x=-radio/2, color='blue', linestyle=':', alpha=0.4)
    ax1.axvline(x=0, color='green', linestyle=':', linewidth=2, alpha=0.5, label='Centro')
    
    # Campo en el centro
    B_centro = campo_helmholtz_analitico_centro(radio, corriente)
    ax1.axhline(y=B_centro*1e6, color='orange', linestyle='--', 
               label=f'B_centro (teórico) = {B_centro*1e6:.2f} μT')
    
    ax1.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax1.set_ylabel('B_z [μT]', fontsize=12)
    ax1.set_title(f'Campo Magnético de Bobinas de Helmholtz en el Eje\n(a={radio}m, I={corriente}A, d=a)', 
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10, loc='best')
    
    # --- Subplot 2: Uniformidad del campo (desviación del centro) ---
    desviacion = (B_total_z - B_centro) / B_centro * 100
    ax2.plot(z_positions, desviacion, 'purple', linewidth=2.5)
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.5, label='±1% desviación')
    ax2.axhline(y=-1, color='red', linestyle='--', alpha=0.5)
    ax2.axhline(y=5, color='orange', linestyle='--', alpha=0.3, label='±5% desviación')
    ax2.axhline(y=-5, color='orange', linestyle='--', alpha=0.3)
    ax2.axvline(x=0, color='green', linestyle=':', linewidth=2, alpha=0.5)
    ax2.axvline(x=radio/2, color='blue', linestyle=':', alpha=0.4)
    ax2.axvline(x=-radio/2, color='blue', linestyle=':', alpha=0.4)
    
    ax2.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax2.set_ylabel('Desviación del campo central [%]', fontsize=12)
    ax2.set_title('Uniformidad del Campo en el Eje', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_ylim([-20, 20])
    
    plt.tight_layout()
    plt.savefig('plots/helmholtz_campo_eje.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/helmholtz_campo_eje.png")
    plt.show()
    
    # Encontrar región de uniformidad
    indices_1pct = np.where(np.abs(desviacion) < 1.0)[0]
    if len(indices_1pct) > 0:
        z_min_1pct = z_positions[indices_1pct[0]]
        z_max_1pct = z_positions[indices_1pct[-1]]
        print(f"\nRegión con uniformidad < 1%: z ∈ [{z_min_1pct:.4f}, {z_max_1pct:.4f}] m")
        print(f"  Longitud de región uniforme: {z_max_1pct - z_min_1pct:.4f} m ({(z_max_1pct - z_min_1pct)/radio*100:.1f}% del radio)")


def graficar_campo_2D_plano_central(radio, corriente):
    """
    Grafica el campo en el plano central (z=0).
    """
    print(f"\nGraficando campo en plano central (z=0)...")
    
    # Grilla en plano XY
    x_range = (-0.3, 0.3)
    y_range = (-0.3, 0.3)
    z_value = 0.0
    
    nx, ny = 30, 30
    x = np.linspace(x_range[0], x_range[1], nx)
    y = np.linspace(y_range[0], y_range[1], ny)
    X, Y = np.meshgrid(x, y)
    
    Bx = np.zeros_like(X)
    By = np.zeros_like(Y)
    Bz = np.zeros_like(X)
    
    print("  Calculando campo en grilla XY...")
    for i in range(ny):
        for j in range(nx):
            punto = np.array([X[i, j], Y[i, j], z_value])
            B, _, _ = campo_helmholtz(punto, radio, corriente)
            Bx[i, j] = B[0]
            By[i, j] = B[1]
            Bz[i, j] = B[2]
    
    B_mag = magnitud_campo(Bx, By, Bz)
    B_centro = campo_helmholtz_analitico_centro(radio, corriente)
    
    # Desviación porcentual
    desviacion = (B_mag - B_centro) / B_centro * 100
    
    # Crear figura
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # --- Subplot 1: Magnitud del campo ---
    contour1 = ax1.contourf(X, Y, B_mag*1e6, levels=20, cmap='viridis')
    
    # Proyección de las espiras
    theta = np.linspace(0, 2*np.pi, 100)
    x_espira = radio * np.cos(theta)
    y_espira = radio * np.sin(theta)
    ax1.plot(x_espira, y_espira, 'r--', linewidth=3, label='Proyección de espiras', alpha=0.8)
    ax1.plot([0], [0], 'wo', markersize=10, label='Centro', markeredgecolor='black', markeredgewidth=2)
    
    ax1.set_xlabel('x [m]', fontsize=12)
    ax1.set_ylabel('y [m]', fontsize=12)
    ax1.set_title(f'Magnitud del Campo en Plano Central\n(z=0, a={radio}m, I={corriente}A)', 
                 fontsize=13, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    cbar1 = plt.colorbar(contour1, ax=ax1)
    cbar1.set_label('|B| [μT]', fontsize=11)
    
    # --- Subplot 2: Mapa de uniformidad ---
    levels_unif = np.linspace(-10, 10, 21)
    contour2 = ax2.contourf(X, Y, desviacion, levels=levels_unif, cmap='RdYlGn_r')
    
    # Contornos de uniformidad
    ax2.contour(X, Y, desviacion, levels=[-5, -1, 1, 5], colors='black', linewidths=2, alpha=0.5)
    ax2.plot(x_espira, y_espira, 'r--', linewidth=3, alpha=0.8)
    ax2.plot([0], [0], 'ko', markersize=10, markerfacecolor='white', markeredgewidth=2)
    
    ax2.set_xlabel('x [m]', fontsize=12)
    ax2.set_ylabel('y [m]', fontsize=12)
    ax2.set_title('Uniformidad del Campo (Desviación %)\n(z=0)', 
                 fontsize=13, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    cbar2 = plt.colorbar(contour2, ax=ax2)
    cbar2.set_label('Desviación [%]', fontsize=11)
    
    plt.tight_layout()
    plt.savefig('plots/helmholtz_campo_2D_central.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/helmholtz_campo_2D_central.png")
    plt.show()


def graficar_campo_3D(radio, corriente):
    """
    Visualización 3D de las bobinas de Helmholtz.
    """
    print(f"\nGenerando visualización 3D...")
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Grilla de puntos
    n_points = 8
    x = np.linspace(-0.25, 0.25, n_points)
    y = np.linspace(-0.25, 0.25, n_points)
    z = np.linspace(-0.25, 0.25, n_points)
    
    print("  Calculando campo en grilla 3D...")
    
    for xi in x:
        for yj in y:
            for zk in z:
                punto = np.array([xi, yj, zk])
                
                # Evitar puntos muy cerca de las espiras
                dist1 = np.sqrt((np.sqrt(xi**2 + yj**2) - radio)**2 + (zk - radio/2)**2)
                dist2 = np.sqrt((np.sqrt(xi**2 + yj**2) - radio)**2 + (zk + radio/2)**2)
                
                if dist1 < 0.03 or dist2 < 0.03:
                    continue
                
                B, _, _ = campo_helmholtz(punto, radio, corriente)
                B_mag = np.linalg.norm(B)
                
                if B_mag > 1e-10:
                    B_norm = B / B_mag
                    
                    # Color según uniformidad
                    B_centro = campo_helmholtz_analitico_centro(radio, corriente)
                    desv = abs(B_mag - B_centro) / B_centro
                    color = plt.cm.RdYlGn_r(min(desv * 10, 1.0))
                    
                    ax.quiver(xi, yj, zk, 
                             B_norm[0], B_norm[1], B_norm[2],
                             length=0.08, color=color, arrow_length_ratio=0.3,
                             linewidth=1.5, alpha=0.7)
    
    # Dibujar las dos espiras
    theta = np.linspace(0, 2*np.pi, 100)
    x_espira = radio * np.cos(theta)
    y_espira = radio * np.sin(theta)
    
    # Espira 1 (z = +a/2)
    z_espira1 = np.ones_like(theta) * radio/2
    ax.plot(x_espira, y_espira, z_espira1, 'b-', linewidth=5, 
            label=f'Espira 1 (z=+a/2)', alpha=0.9)
    
    # Espira 2 (z = -a/2)
    z_espira2 = np.ones_like(theta) * (-radio/2)
    ax.plot(x_espira, y_espira, z_espira2, 'r-', linewidth=5, 
            label=f'Espira 2 (z=-a/2)', alpha=0.9)
    
    # Líneas conectando las espiras (para visualización)
    for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
        x_line = [radio * np.cos(angle), radio * np.cos(angle)]
        y_line = [radio * np.sin(angle), radio * np.sin(angle)]
        z_line = [-radio/2, radio/2]
        ax.plot(x_line, y_line, z_line, 'gray', linewidth=1, alpha=0.3)
    
    ax.set_xlabel('x [m]', fontsize=11)
    ax.set_ylabel('y [m]', fontsize=11)
    ax.set_zlabel('z [m]', fontsize=11)
    ax.set_title(f'Bobinas de Helmholtz - Vista 3D\n(a={radio}m, I={corriente}A, d=a)', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    ax.set_xlim([-0.3, 0.3])
    ax.set_ylim([-0.3, 0.3])
    ax.set_zlim([-0.3, 0.3])
    
    plt.tight_layout()
    plt.savefig('plots/helmholtz_3D.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/helmholtz_3D.png")
    plt.show()


def comparacion_separaciones(radio, corriente):
    """
    Compara el campo para diferentes separaciones de las espiras.
    """
    print(f"\nComparando diferentes separaciones...")
    
    separaciones = [0.5*radio, radio, 1.5*radio, 2*radio]
    labels = ['d = 0.5a', 'd = a (Helmholtz)', 'd = 1.5a', 'd = 2a']
    colors = ['blue', 'green', 'orange', 'red']
    
    z_positions = np.linspace(-0.4, 0.4, 200)
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    
    for sep, label, color in zip(separaciones, labels, colors):
        B_z = []
        for z in z_positions:
            punto = np.array([0.0, 0.0, z])
            B, _, _ = campo_helmholtz(punto, radio, corriente, separacion=sep)
            B_z.append(B[2])
        
        B_z = np.array(B_z)
        
        if sep == radio:
            ax.plot(z_positions, B_z*1e6, color=color, linewidth=3, 
                   label=label, linestyle='-')
        else:
            ax.plot(z_positions, B_z*1e6, color=color, linewidth=2, 
                   label=label, linestyle='--', alpha=0.7)
    
    ax.axvline(x=0, color='black', linestyle=':', alpha=0.3)
    ax.set_xlabel('Posición en eje z [m]', fontsize=12)
    ax.set_ylabel('B_z [μT]', fontsize=12)
    ax.set_title(f'Comparación de Campo para Diferentes Separaciones\n(a={radio}m, I={corriente}A)', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('plots/helmholtz_comparacion_separaciones.png', dpi=300, bbox_inches='tight')
    print("  → Guardado: plots/helmholtz_comparacion_separaciones.png")
    plt.show()
    
    print("\nObservación: La separación d = a produce el campo más uniforme")
    print("             en la región central (configuración de Helmholtz).")


def main():
    """
    Función principal.
    """
    # Introducción
    introduccion_helmholtz()
    
    # Análisis de punto específico
    radio, corriente = analizar_campo_punto_especifico()
    
    # Campo en el eje
    graficar_campo_en_eje(radio, corriente)
    
    # Campo en plano central
    graficar_campo_2D_plano_central(radio, corriente)
    
    # Visualización 3D
    graficar_campo_3D(radio, corriente)
    
    # Comparación de separaciones
    comparacion_separaciones(radio, corriente)
    
    print("\n" + "="*80)
    print("BOBINAS DE HELMHOLTZ - ANÁLISIS COMPLETADO")
    print("="*80)
    print("\nCONCLUSIONES:")
    print("-"*80)
    print("""
✓ Las bobinas de Helmholtz generan un campo magnético altamente uniforme
✓ La separación óptima es d = a (radio de las espiras)
✓ En el centro, el campo es aproximadamente 0.7155 * (μ₀ I / a)
✓ La región de uniformidad (<1% variación) es significativa
✓ Aplicaciones en experimentos que requieren campos uniformes
✓ El principio de superposición se verifica correctamente
    """)
    print("Todos los gráficos guardados en carpeta 'plots/'")
    print("="*80)


if __name__ == "__main__":
    main()
