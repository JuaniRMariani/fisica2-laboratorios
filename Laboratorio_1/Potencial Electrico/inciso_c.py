import os
import sys
import argparse
import numpy as np

# ensure incisos_common in sibling 'Campo Electrico' is importable
THIS_DIR = os.path.dirname(__file__)
COMMON_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'Campo Electrico'))
if COMMON_DIR not in sys.path:
    sys.path.insert(0, COMMON_DIR)

from incisos_common import generate_charges, compute_1d_along_x, compute_and_plot_2d


def plot_potential_1d(x_vals, V_total, V_individual, out_prefix='plots/potencial'):
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    for i in range(V_individual.shape[0]):
        plt.plot(x_vals, V_individual[i, :], '--', label=f"V(x) carga {i+1}")
    plt.plot(x_vals, V_total, 'k', label="V(x) total")
    plt.axhline(0, color='gray', linestyle=':')
    plt.legend()
    plt.xlabel('x [m]')
    plt.ylabel('V [Volt]')
    plt.title('Potencial sobre el eje x - cargas individuales y superposición')
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_V_vs_x.png", dpi=150)
    plt.close()


def main(arr='two_pos', out='plots/potencial'):
    """Inciso c: genera V(x) y mapa de contorno (equipotenciales).
    Guarda dos archivos: <out>_V_vs_x.png y <out>_equipotentials.png (además el mapa de líneas de campo).
    """
    cargas = generate_charges(arrangement=arr)
    print('Cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')

    # a) y b) calcular V(x,y) y graficar V(x) (individual y superposición)
    x_vals, E_total, V_total, E_individual, V_individual = compute_1d_along_x(cargas)
    plot_potential_1d(x_vals, V_total, V_individual, out_prefix=out)
    print(f'Guardado: {out}_V_vs_x.png')

    # c) mapa de contorno / superficies equipotenciales en 2D
    compute_and_plot_2d(cargas, out_prefix=out)
    print(f'Guardado: {out}_equipotentials.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inciso c: graficar potencial y equipotenciales')
    parser.add_argument('--arr', choices=['two_pos', 'two_neg'], default='two_pos')
    parser.add_argument('--out', default='plots/potencial')
    args = parser.parse_args()
    main(arr=args.arr, out=args.out)
