import numpy as np
from incisos_common import generate_charges, E_en_x_factory, _simple_fsolve, compute_1d_along_x, plot_1d

if __name__ == '__main__':
    cargas = generate_charges()
    x_vals, E_total, V_total, E_individual, V_individual = compute_1d_along_x(cargas)

    E_en_x = E_en_x_factory(cargas)
    puntos_eq = []
    guesses = list(np.linspace(-2.5, 2.5, 13))
    for guess in guesses:
        try:
            from incisos_common import fsolve
            if fsolve is not None:
                root = float(fsolve(E_en_x, guess)[0])
            else:
                root = float(_simple_fsolve(E_en_x, guess)[0])
            if -3 < root < 3 and not any(np.isclose(root, r, atol=1e-3) for r in puntos_eq):
                puntos_eq.append(root)
        except Exception:
            pass
    puntos_eq = sorted(puntos_eq)
    print('Puntos de equilibrio (numéricos):', puntos_eq)
    plot_1d(x_vals, E_total, V_total, E_individual, V_individual, out_prefix='plots/inciso_d', puntos_eq=puntos_eq)
    print('Inciso d: gráfico guardado con prefijo plots/inciso_d')
