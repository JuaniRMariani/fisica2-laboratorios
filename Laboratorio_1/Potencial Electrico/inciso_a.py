"""Inciso a) - Calcular numéricamente V(x,y) generado por el conjunto de 3 cargas.

Este script solo calcula la malla de potencial y la guarda en un archivo .npz
y genera un heatmap PNG para inspección rápida.
"""
import numpy as np
import os
import sys
import argparse
import matplotlib.pyplot as plt

# make sure incisos_common (in sibling 'Campo Electrico') is importable
THIS_DIR = os.path.dirname(__file__)
COMMON_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'Campo Electrico'))
if COMMON_DIR not in sys.path:
    sys.path.insert(0, COMMON_DIR)

from incisos_common import generate_charges, potencial


def compute_potential_grid(cargas, x_min=-3, x_max=3, y_min=-3, y_max=3, n=200):
    x = np.linspace(x_min, x_max, n)
    y = np.linspace(y_min, y_max, n)
    X, Y = np.meshgrid(x, y)
    V = np.zeros_like(X)

    # calcular potencial punto a punto
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            V[i, j] = potencial(X[i, j], Y[i, j], cargas)

    return X, Y, V


def save_grid(X, Y, V, out_prefix='plots/inciso_a'):
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)
    np.savez(f"{out_prefix}_grid.npz", X=X, Y=Y, V=V)

    # guardar heatmap rápido
    plt.figure(figsize=(6, 5))
    im = plt.imshow(V, origin='lower', extent=(X.min(), X.max(), Y.min(), Y.max()), cmap='coolwarm')
    plt.colorbar(im, label='V [Volt]')
    plt.title('Potencial V(x,y) - heatmap')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_heatmap.png", dpi=150)
    plt.close()


def main(arr='two_pos', out='plots/inciso_a', x_min=-3, x_max=3, y_min=-3, y_max=3, n=200):
    cargas = generate_charges(arrangement=arr)
    print('Cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')

    X, Y, V = compute_potential_grid(cargas, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, n=n)
    save_grid(X, Y, V, out_prefix=out)
    print(f'Guardado grid y heatmap en prefijo: {out} (n={n})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inciso a) Calcular V(x,y) de 3 cargas')
    parser.add_argument('--arr', choices=['two_pos', 'two_neg'], default='two_pos')
    parser.add_argument('--out', default='plots/inciso_a')
    parser.add_argument('--n', type=int, default=200, help='resolución de la malla (n x n)')
    parser.add_argument('--xmin', type=float, default=-3.0)
    parser.add_argument('--xmax', type=float, default=3.0)
    parser.add_argument('--ymin', type=float, default=-3.0)
    parser.add_argument('--ymax', type=float, default=3.0)
    args = parser.parse_args()
    main(arr=args.arr, out=args.out, x_min=args.xmin, x_max=args.xmax, y_min=args.ymin, y_max=args.ymax, n=args.n)
