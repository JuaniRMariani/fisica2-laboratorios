"""Inciso b) Graficar V(x) como función de x: individual y superposición total."""
import argparse
import os
import sys
import matplotlib.pyplot as plt

# ensure sibling folder 'Campo Electrico' (where incisos_common.py lives) is importable
THIS_DIR = os.path.dirname(__file__)
COMMON_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'Campo Electrico'))
if COMMON_DIR not in sys.path:
    sys.path.insert(0, COMMON_DIR)

from incisos_common import generate_charges, compute_1d_along_x


def plot_Vx(x_vals, V_total, V_individual, out_prefix='plots/potencial_b'):
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)

    # Figura: V(x) individual (dashed) y total (línea negra)
    plt.figure(figsize=(8, 5))
    for i in range(V_individual.shape[0]):
        plt.plot(x_vals, V_individual[i, :], '--', label=f"V(x) carga {i+1}")
    plt.plot(x_vals, V_total, 'k', linewidth=1.5, label='V(x) total')
    plt.xlabel('x [m]')
    plt.ylabel('V [Volt]')
    plt.title('Potencial V(x) - individual y superposición')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_V_vs_x.png", dpi=150)
    plt.close()


def main(arr='two_pos', out='plots/potencial_b'):
    cargas = generate_charges(arrangement=arr)
    print('Cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')

    x_vals, E_total, V_total, E_individual, V_individual = compute_1d_along_x(cargas)

    plot_Vx(x_vals, V_total, V_individual, out_prefix=out)
    print(f'Figura guardada: {out}_V_vs_x.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inciso b) Graficar V(x) individual y total')
    parser.add_argument('--arr', choices=['two_pos', 'two_neg'], default='two_pos')
    parser.add_argument('--out', default='plots/potencial_b')
    args = parser.parse_args()
    main(arr=args.arr, out=args.out)
