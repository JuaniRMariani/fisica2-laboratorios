from incisos_common import generate_charges, compute_1d_along_x, plot_1d

if __name__ == '__main__':
    cargas = generate_charges()
    x_vals, E_total, V_total, E_individual, V_individual = compute_1d_along_x(cargas)
    plot_1d(x_vals, E_total, V_total, E_individual, V_individual, out_prefix='plots/inciso_c')
    print('Inciso c: gráficos guardados con prefijo plots/inciso_c')
