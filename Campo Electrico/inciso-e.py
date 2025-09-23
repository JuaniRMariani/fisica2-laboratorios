from incisos_common import generate_charges, compute_and_plot_2d

if __name__ == '__main__':
    cargas = generate_charges()
    compute_and_plot_2d(cargas, out_prefix='plots/inciso_e')
    print('Inciso e: figuras guardadas con prefijo plots/inciso_e')
