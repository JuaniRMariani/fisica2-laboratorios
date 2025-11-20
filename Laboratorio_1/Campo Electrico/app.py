

"""Laboratorio 1 - Campo y potencial de 3 cargas puntuales (incisos a-e).

Este script implementa:
a) Generación de 3 cargas sobre el eje x: dos del mismo signo y la tercera del signo opuesto,
   con magnitudes distintas.
b) Cálculo numérico del campo eléctrico E(x,y) por superposición.
c) Gráficas de E(x) para cada carga individual y la superposición total.
d) Detección numérica de puntos de equilibrio sobre el eje x (y marcados en las gráficas).
e) Gráfica de líneas de campo y equipotenciales en 2D, con marcadores de equilibrio.

Uso:
    python app.py --arr two_pos --out plots/lab1
"""

import numpy as np
import argparse
from incisos_common import (
    generate_charges,
    compute_1d_along_x,
    plot_1d,
    compute_and_plot_2d,
    E_en_x_factory,
    _simple_fsolve,
    fsolve,
)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Laboratorio 1: campo y potencial de 3 cargas')
    parser.add_argument('--arr', choices=['two_pos', 'two_neg'], default='two_pos')
    parser.add_argument('--out', type=str, default='plots/lab1')
    args = parser.parse_args()

    cargas = generate_charges(arrangement=args.arr)

    print('Cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')

    x_vals, E_total, V_total, E_individual, V_individual = compute_1d_along_x(cargas)

    # buscar puntos de equilibrio sobre eje x (varios guesses)
    E_en_x = E_en_x_factory(cargas)
    puntos_eq = []
    guesses = list(np.linspace(-2.5, 2.5, 13))
    for guess in guesses:
        try:
            if fsolve is not None:
                root = float(fsolve(E_en_x, guess)[0])
            else:
                root = float(_simple_fsolve(E_en_x, guess)[0])
            if -3 < root < 3 and not any(np.isclose(root, r, atol=1e-3) for r in puntos_eq):
                puntos_eq.append(root)
        except Exception:
            pass
    puntos_eq = sorted(puntos_eq)
    print('Puntos de equilibrio sobre eje x:', puntos_eq)

    # graficar 1D y 2D con marcadores de equilibrio
    plot_1d(x_vals, E_total, V_total, E_individual, V_individual, out_prefix=args.out, puntos_eq=puntos_eq)
    compute_and_plot_2d(cargas, out_prefix=args.out, puntos_eq=puntos_eq)

    # Indico cuáles incisos están resueltos
    print('\nResumen de incisos:')
    print('a) Generación de configuración de 3 cargas: Hecho')
    print('b) Cálculo numérico de E(x,y) por superposición: Hecho (función campo)')
    print('c) Gráficas E(x) individuales y total: Hecho (plots _E_vs_x)')
    print('d) Detección numérica de puntos de equilibrio sobre eje x: Hecho (mostrados y marcados)')
    print('e) Gráfico de líneas de campo y equipotenciales: Hecho (plots _field_lines, _equipotentials)')

    print('\nFiguras guardadas con prefijo:', args.out)

