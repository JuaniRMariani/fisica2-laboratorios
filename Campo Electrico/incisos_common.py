"""Funciones comunes usadas por los scripts de los incisos (a-e).
Contiene generación de cargas, cálculo de campo/potencial, utilidades de graficado
y un fallback simple para fsolve si scipy no está instalado.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import os

try:
    from scipy.optimize import fsolve
except Exception:
    fsolve = None

# Constante de Coulomb
k = 8.9875517923e9


def generate_charges(arrangement='two_pos'):
    """Genera 3 cargas sobre el eje x (y=0) con magnitudes distintas.
    Devuelve lista de tuplas (q, x, y).
    """
    positions = [-1.0, 0.5, 2.0]
    mags = [1e-6, 2e-6, 3e-6]
    random.shuffle(mags)

    if arrangement == 'two_pos':
        signs = [1, 1, -1]
    else:
        signs = [-1, -1, 1]

    cargas = [(s * m, x, 0.0) for s, m, x in zip(signs, mags, positions)]
    return cargas


def campo(x, y, cargas):
    """Devuelve (Ex, Ey) en el punto (x,y) por superposición de cargas puntuales."""
    Ex, Ey = 0.0, 0.0
    for q, xq, yq in cargas:
        dx, dy = x - xq, y - yq
        r = np.hypot(dx, dy)
        if r != 0.0:
            Ex += k * q * dx / r**3
            Ey += k * q * dy / r**3
    return Ex, Ey


def potencial(x, y, cargas):
    """Potencial escalar en (x,y) por superposición."""
    V = 0.0
    for q, xq, yq in cargas:
        dx, dy = x - xq, y - yq
        r = np.hypot(dx, dy)
        if r != 0.0:
            V += k * q / r
    return V


def compute_1d_along_x(cargas, x_min=-3, x_max=3, n=400):
    x_vals = np.linspace(x_min, x_max, n)
    E_total = np.zeros_like(x_vals)
    V_total = np.zeros_like(x_vals)
    E_individual = np.zeros((len(cargas), n))
    V_individual = np.zeros((len(cargas), n))

    for idx, x in enumerate(x_vals):
        Ex_tot, _ = campo(x, 0.0, cargas)
        E_total[idx] = Ex_tot
        V_total[idx] = potencial(x, 0.0, cargas)
        for i, (q, xq, yq) in enumerate(cargas):
            dx = x - xq
            r = abs(dx)
            if r != 0.0:
                E_individual[i, idx] = k * q * dx / r**3
                V_individual[i, idx] = k * q / r
            else:
                E_individual[i, idx] = np.nan
                V_individual[i, idx] = np.nan

    return x_vals, E_total, V_total, E_individual, V_individual


def plot_1d(x_vals, E_total, V_total, E_individual, V_individual, out_prefix='plots/inciso_c', puntos_eq=None):
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)

    plt.figure(figsize=(8, 5))
    for i in range(E_individual.shape[0]):
        plt.plot(x_vals, E_individual[i, :], '--', label=f"E(x) carga {i+1}")
    plt.plot(x_vals, E_total, 'k', label="E(x) total")
    plt.axhline(0, color="gray", linestyle=":")
    if puntos_eq:
        xs = list(puntos_eq)
        ys = [0.0] * len(xs)
        plt.scatter(xs, ys, c='green', marker='x', s=80, label='Equilibrio')
    plt.legend()
    plt.xlabel("x [m]")
    plt.ylabel("E_x [N/C]")
    plt.title("Campo eléctrico sobre el eje x (contribuciones y total)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_E_vs_x.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    for i in range(V_individual.shape[0]):
        plt.plot(x_vals, V_individual[i, :], '--', label=f"V(x) carga {i+1}")
    plt.plot(x_vals, V_total, 'k', label="V(x) total")
    if puntos_eq:
        for rx in puntos_eq:
            plt.axvline(rx, color='green', linestyle=':', alpha=0.7)
    plt.legend()
    plt.xlabel("x [m]")
    plt.ylabel("V [Volt]")
    plt.title("Potencial sobre el eje x")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_V_vs_x.png", dpi=150)
    plt.close()


def compute_and_plot_2d(cargas, x_min=-3, x_max=3, y_min=-3, y_max=3, n=200, out_prefix='plots/inciso_e', puntos_eq=None):
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)
    x = np.linspace(x_min, x_max, n)
    y = np.linspace(y_min, y_max, n)
    X, Y = np.meshgrid(x, y)

    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    V = np.zeros_like(X)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Ex[i, j], Ey[i, j] = campo(X[i, j], Y[i, j], cargas)
            V[i, j] = potencial(X[i, j], Y[i, j], cargas)

    plt.figure(figsize=(8, 6))
    speed = np.hypot(Ex, Ey)
    plt.streamplot(X, Y, Ex, Ey, color=np.log(speed + 1e-12), cmap="inferno", density=1.2)
    for q, xq, yq in cargas:
        plt.scatter(xq, yq, c='red' if q > 0 else 'blue', s=100)
        plt.text(xq, yq + 0.08, f"{q:.1e} C", ha='center')
    if puntos_eq:
        for rx in puntos_eq:
            plt.scatter(rx, 0.0, c='green', marker='x', s=100)
    plt.title("Líneas de campo eléctrico")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.colorbar(label="log|E|")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_field_lines.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 6))
    cont = plt.contour(X, Y, V, levels=30, cmap="coolwarm")
    plt.clabel(cont, inline=True, fontsize=8)
    for q, xq, yq in cargas:
        plt.scatter(xq, yq, c='red' if q > 0 else 'blue', s=100)
    if puntos_eq:
        for rx in puntos_eq:
            plt.scatter(rx, 0.0, c='green', marker='x', s=100)
    plt.title("Superficies equipotenciales")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_equipotentials.png", dpi=150)
    plt.close()


def E_en_x_factory(cargas):
    def E_en_x(x):
        Ex, _ = campo(x, 0.0, cargas)
        return Ex
    return E_en_x


def _simple_fsolve(func, x0, maxiter=200, tol=1e-6):
    x0 = float(x0)
    dx = 1e-3 if abs(x0) < 1.0 else 1e-2
    x1 = x0
    x2 = x0 + dx
    f1 = func(x1)
    f2 = func(x2)
    for _ in range(maxiter):
        if abs(f2 - f1) < 1e-14:
            break
        x3 = x2 - f2 * (x2 - x1) / (f2 - f1)
        if abs(x3 - x2) < tol:
            return np.array([x3])
        x1, f1 = x2, f2
        x2 = x3
        f2 = func(x2)
    raise RuntimeError("simple_fsolve no convergió")
