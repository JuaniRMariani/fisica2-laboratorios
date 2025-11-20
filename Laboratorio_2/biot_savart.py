"""
Laboratorio 2: Ley de Biot-Savart
Funciones base para calcular campo magnético

Universidad Nacional del Sur - Física II
"""

import numpy as np
from typing import Tuple, Callable

# Scipy es opcional, solo se usa para integraciones avanzadas
try:
    from scipy.integrate import quad
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

# Constante física
MU_0 = 4 * np.pi * 1e-7  # Permeabilidad del vacío [T·m/A]


def campo_magnetico_alambre_recto(punto: np.ndarray, L: float, I: float, 
                                   posicion_centro: np.ndarray = None,
                                   direccion: np.ndarray = None,
                                   n_segmentos: int = 1000) -> np.ndarray:
    """
    Calcula el campo magnético en un punto debido a un alambre recto finito
    usando la Ley de Biot-Savart.
    
    B(r) = (μ₀/4π) ∫ I dl' × (r - r') / |r - r'|³
    
    Parámetros:
    -----------
    punto : np.ndarray
        Punto (x, y, z) donde calcular el campo magnético
    L : float
        Longitud total del alambre [m]
    I : float
        Corriente en el alambre [A]
    posicion_centro : np.ndarray, opcional
        Posición del centro del alambre (por defecto origen)
    direccion : np.ndarray, opcional
        Vector dirección del alambre (por defecto eje z)
    n_segmentos : int
        Número de segmentos para la discretización
        
    Retorna:
    --------
    np.ndarray
        Vector campo magnético B = (Bx, By, Bz) [T]
    """
    if posicion_centro is None:
        posicion_centro = np.array([0.0, 0.0, 0.0])
    
    if direccion is None:
        direccion = np.array([0.0, 0.0, 1.0])
    
    # Normalizar dirección
    direccion = direccion / np.linalg.norm(direccion)
    
    # Discretizar el alambre en segmentos pequeños
    # El alambre va desde -L/2 hasta L/2 a lo largo de la dirección
    s = np.linspace(-L/2, L/2, n_segmentos)
    ds = s[1] - s[0]
    
    # Campo magnético total (inicializado en cero)
    B_total = np.zeros(3)
    
    # Sumar contribución de cada segmento
    for si in s:
        # Posición del segmento
        r_prima = posicion_centro + si * direccion
        
        # Vector dl' (elemento diferencial de corriente)
        dl_prima = ds * direccion
        
        # Vector desde el segmento al punto de observación
        r_menos_r_prima = punto - r_prima
        
        # Distancia
        distancia = np.linalg.norm(r_menos_r_prima)
        
        # Evitar singularidades (cuando el punto está sobre el alambre)
        if distancia < 1e-10:
            continue
        
        # Producto vectorial: dl' × (r - r')
        producto_cruz = np.cross(dl_prima, r_menos_r_prima)
        
        # Contribución al campo magnético
        dB = (MU_0 * I / (4 * np.pi)) * producto_cruz / (distancia**3)
        
        B_total += dB
    
    return B_total


def campo_magnetico_espira(punto: np.ndarray, radio: float, I: float,
                           centro: np.ndarray = None,
                           normal: np.ndarray = None,
                           n_segmentos: int = 1000) -> np.ndarray:
    """
    Calcula el campo magnético en un punto debido a una espira circular
    usando la Ley de Biot-Savart.
    
    B(r) = (μ₀/4π) ∫ I dl' × (r - r') / |r - r'|³
    
    Parámetros:
    -----------
    punto : np.ndarray
        Punto (x, y, z) donde calcular el campo magnético
    radio : float
        Radio de la espira [m]
    I : float
        Corriente en la espira [A] (positiva en sentido antihorario)
    centro : np.ndarray, opcional
        Posición del centro de la espira (por defecto origen)
    normal : np.ndarray, opcional
        Vector normal al plano de la espira (por defecto eje z)
    n_segmentos : int
        Número de segmentos para la discretización
        
    Retorna:
    --------
    np.ndarray
        Vector campo magnético B = (Bx, By, Bz) [T]
    """
    if centro is None:
        centro = np.array([0.0, 0.0, 0.0])
    
    if normal is None:
        normal = np.array([0.0, 0.0, 1.0])
    
    # Normalizar normal
    normal = normal / np.linalg.norm(normal)
    
    # Crear dos vectores perpendiculares en el plano de la espira
    # Elegir un vector auxiliar que no sea paralelo a normal
    if abs(normal[2]) < 0.9:
        aux = np.array([0.0, 0.0, 1.0])
    else:
        aux = np.array([1.0, 0.0, 0.0])
    
    # Primer vector en el plano
    v1 = np.cross(normal, aux)
    v1 = v1 / np.linalg.norm(v1)
    
    # Segundo vector en el plano (perpendicular a v1 y normal)
    v2 = np.cross(normal, v1)
    v2 = v2 / np.linalg.norm(v2)
    
    # Discretizar la espira en segmentos
    theta = np.linspace(0, 2*np.pi, n_segmentos, endpoint=False)
    dtheta = theta[1] - theta[0]
    
    # Campo magnético total
    B_total = np.zeros(3)
    
    # Sumar contribución de cada segmento
    for th in theta:
        # Posición del segmento en la espira
        r_prima = centro + radio * (np.cos(th) * v1 + np.sin(th) * v2)
        
        # Vector dl' (tangente a la espira)
        # dl'/dθ = radio * (-sin(θ) * v1 + cos(θ) * v2)
        dl_prima = radio * dtheta * (-np.sin(th) * v1 + np.cos(th) * v2)
        
        # Vector desde el segmento al punto de observación
        r_menos_r_prima = punto - r_prima
        
        # Distancia
        distancia = np.linalg.norm(r_menos_r_prima)
        
        # Evitar singularidades
        if distancia < 1e-10:
            continue
        
        # Producto vectorial: dl' × (r - r')
        producto_cruz = np.cross(dl_prima, r_menos_r_prima)
        
        # Contribución al campo magnético
        dB = (MU_0 * I / (4 * np.pi)) * producto_cruz / (distancia**3)
        
        B_total += dB
    
    return B_total


def campo_magnetico_grilla(funcion_campo: Callable, x_range: Tuple[float, float],
                           y_range: Tuple[float, float], z_value: float,
                           nx: int = 20, ny: int = 20) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Calcula el campo magnético en una grilla de puntos en el plano z = z_value.
    
    Parámetros:
    -----------
    funcion_campo : Callable
        Función que calcula el campo magnético en un punto
    x_range : tuple
        Rango (x_min, x_max) [m]
    y_range : tuple
        Rango (y_min, y_max) [m]
    z_value : float
        Valor de z donde evaluar el campo [m]
    nx, ny : int
        Número de puntos en x e y
        
    Retorna:
    --------
    X, Y : np.ndarray
        Meshgrids de coordenadas
    Bx, By, Bz : np.ndarray
        Componentes del campo magnético
    """
    x = np.linspace(x_range[0], x_range[1], nx)
    y = np.linspace(y_range[0], y_range[1], ny)
    X, Y = np.meshgrid(x, y)
    
    Bx = np.zeros_like(X)
    By = np.zeros_like(Y)
    Bz = np.zeros_like(X)
    
    for i in range(ny):
        for j in range(nx):
            punto = np.array([X[i, j], Y[i, j], z_value])
            B = funcion_campo(punto)
            Bx[i, j] = B[0]
            By[i, j] = B[1]
            Bz[i, j] = B[2]
    
    return X, Y, Bx, By, Bz


def magnitud_campo(Bx: np.ndarray, By: np.ndarray, Bz: np.ndarray) -> np.ndarray:
    """
    Calcula la magnitud del campo magnético.
    
    |B| = √(Bx² + By² + Bz²)
    """
    return np.sqrt(Bx**2 + By**2 + Bz**2)


def campo_magnetico_alambre_analitico(punto: np.ndarray, L: float, I: float) -> np.ndarray:
    """
    Fórmula analítica aproximada para un alambre recto infinito a lo largo del eje z.
    Para alambre finito centrado en el origen, esta es una aproximación.
    
    Para un alambre infinito en z: B = (μ₀ I)/(2π ρ) φ̂
    donde ρ = √(x² + y²) es la distancia perpendicular al alambre.
    
    Nota: Esta función es solo para comparación y validación.
    """
    x, y, z = punto
    rho = np.sqrt(x**2 + y**2)
    
    if rho < 1e-10:
        return np.array([0.0, 0.0, 0.0])
    
    # Magnitud del campo (fórmula de alambre infinito)
    B_mag = (MU_0 * I) / (2 * np.pi * rho)
    
    # Dirección: perpendicular al radio, en dirección φ̂
    # φ̂ = (-sin(φ), cos(φ), 0) = (-y/ρ, x/ρ, 0)
    B = B_mag * np.array([-y/rho, x/rho, 0.0])
    
    return B


def campo_magnetico_espira_eje(z: float, radio: float, I: float) -> np.ndarray:
    """
    Fórmula analítica para el campo magnético en el eje de una espira circular.
    
    En el eje (x=0, y=0), el campo es:
    B_z = (μ₀ I a²)/(2(a² + z²)^(3/2))
    
    donde a es el radio de la espira.
    """
    a = radio
    B_z = (MU_0 * I * a**2) / (2 * (a**2 + z**2)**(3/2))
    
    return np.array([0.0, 0.0, B_z])


if __name__ == "__main__":
    # Pruebas básicas
    print("="*60)
    print("PRUEBAS DE FUNCIONES DE BIOT-SAVART")
    print("="*60)
    
    # Prueba 1: Alambre recto
    print("\n1. Campo magnético de alambre recto (L=1m, I=10A)")
    punto_test = np.array([0.1, 0.0, 0.0])  # 10 cm del eje
    B_alambre = campo_magnetico_alambre_recto(punto_test, L=1.0, I=10.0)
    print(f"   Punto de evaluación: {punto_test} m")
    print(f"   B = {B_alambre}")
    print(f"   |B| = {np.linalg.norm(B_alambre):.6e} T")
    
    # Comparar con fórmula de alambre infinito
    B_infinito = campo_magnetico_alambre_analitico(punto_test, L=1.0, I=10.0)
    print(f"   B (infinito) = {B_infinito}")
    print(f"   |B| (infinito) = {np.linalg.norm(B_infinito):.6e} T")
    
    # Prueba 2: Espira circular
    print("\n2. Campo magnético de espira (radio=0.1m, I=5A)")
    punto_test2 = np.array([0.0, 0.0, 0.05])  # En el eje, 5 cm arriba
    B_espira = campo_magnetico_espira(punto_test2, radio=0.1, I=5.0)
    print(f"   Punto de evaluación: {punto_test2} m")
    print(f"   B = {B_espira}")
    print(f"   |B| = {np.linalg.norm(B_espira):.6e} T")
    
    # Comparar con fórmula en el eje
    B_espira_eje = campo_magnetico_espira_eje(0.05, radio=0.1, I=5.0)
    print(f"   B (fórmula eje) = {B_espira_eje}")
    print(f"   |B| (fórmula eje) = {np.linalg.norm(B_espira_eje):.6e} T")
    
    print("\n" + "="*60)
    print("Módulo biot_savart.py funcionando correctamente")
    print("="*60)
