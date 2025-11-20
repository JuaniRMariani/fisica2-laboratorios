from incisos_common import generate_charges

if __name__ == '__main__':
    cargas = generate_charges(arrangement='two_pos')
    print('Configuración de 3 cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')
