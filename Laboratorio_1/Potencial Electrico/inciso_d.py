import os
import sys
import argparse
import numpy as np

# ensure incisos_common in sibling 'Campo Electrico' is importable
THIS_DIR = os.path.dirname(__file__)
COMMON_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'Campo Electrico'))
if COMMON_DIR not in sys.path:
    sys.path.insert(0, COMMON_DIR)

from incisos_common import generate_charges, campo, potencial


def gradV_numeric(x, y, cargas, h=1e-6):
    """Calcula gradiente de V en (x,y) por diferencias centradas."""
    Vx_plus = potencial(x + h, y, cargas)
    Vx_minus = potencial(x - h, y, cargas)
    Vy_plus = potencial(x, y + h, cargas)
    Vy_minus = potencial(x, y - h, cargas)
    dVdx = (Vx_plus - Vx_minus) / (2 * h)
    dVdy = (Vy_plus - Vy_minus) / (2 * h)
    return np.array([dVdx, dVdy])


def compare_directions(cargas, points, h=1e-6):
    """Para cada punto, compara la dirección de -gradV con la dirección del campo calculado por 'campo'.
    Devuelve lista de tuplas (point, angle_deg, mag_field, mag_grad)
    donde angle_deg es el ángulo entre -∇V y E (debería ser cercano a 0 si son paralelos y en sentido opuesto).
    """
    results = []
    for x, y in points:
        Ex, Ey = campo(x, y, cargas)
        grad = gradV_numeric(x, y, cargas, h=h)
        minus_grad = -grad
        E_vec = np.array([Ex, Ey])
        magE = np.linalg.norm(E_vec)
        magG = np.linalg.norm(minus_grad)
        if magE == 0 or magG == 0:
            angle = np.nan
        else:
            cosang = np.dot(E_vec, minus_grad) / (magE * magG)
            cosang = np.clip(cosang, -1.0, 1.0)
            angle = np.degrees(np.arccos(cosang))
        results.append(((x, y), angle, magE, magG))
    return results


def main(arr='two_pos', out='plots/potencial', sample_points=None):
    cargas = generate_charges(arrangement=arr)
    print('Cargas (q [C], x [m], y [m]):')
    for q, xq, yq in cargas:
        print(f'  {q:.3e} , {xq:.3f} , {yq:.3f}')

    if sample_points is None:
        # elegir algunos puntos de muestra alejados de las cargas
        sample_points = [(-2.0, 0.5), (-0.5, 0.2), (0.8, -0.3), (1.5, 0.4)]

    res = compare_directions(cargas, sample_points)
    print('\nChequeo numérico: comparación entre -∇V (numérico) y E (analítico)')
    for (x, y), angle, magE, magG in res:
        ang_str = f"{angle:.3f}°" if not np.isnan(angle) else 'nan'
        print(f"Punto ({x:.3f}, {y:.3f}): ángulo entre -∇V y E = {ang_str}, |E|={magE:.3e}, | -∇V |={magG:.3e}")

    print('\nDiscusión:')
    print(' - Teóricamente E = -∇V. El chequeo numérico calcula -∇V por diferencias finitas y compara su dirección con E.')
    print(' - Un ángulo cercano a 0° indica buena concordancia de direcciones; magnitudes pueden diferir por errores numéricos.')
    print(' - Evitar puntos muy cerca de las cargas donde V y E son singulares; allí las diferencias finitas pierden precisión.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inciso d: discusión y chequeo numérico entre -∇V y E')
    parser.add_argument('--arr', choices=['two_pos', 'two_neg'], default='two_pos')
    parser.add_argument('--out', default='plots/potencial')
    args = parser.parse_args()
    main(arr=args.arr, out=args.out)
