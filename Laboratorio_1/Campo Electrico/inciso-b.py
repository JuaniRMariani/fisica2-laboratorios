from incisos_common import campo, potencial, generate_charges

if __name__ == '__main__':
    cargas = generate_charges()
    pts = [(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.5, 0.5)]
    print('Evaluación de campo y potencial en puntos de ejemplo:')
    for x, y in pts:
        Ex, Ey = campo(x, y, cargas)
        V = potencial(x, y, cargas)
        print(f'Punto ({x:.2f}, {y:.2f}) -> Ex={Ex:.3e} N/C, Ey={Ey:.3e} N/C, V={V:.3e} V')
