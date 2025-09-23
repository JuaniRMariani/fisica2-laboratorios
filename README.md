# Laboratorio 1 — Campo y Potencial Eléctrico (2D)

Breve repositorio con scripts para calcular y graficar el campo eléctrico y el potencial generados por 3 cargas puntuales en 2D.

Contenido principal
- `Campo Electrico/` : módulo compartido `incisos_common.py` y scripts relacionados con líneas de campo y ejercicios del campo.
- `Potencial Electrico/` : scripts separados por inciso:
  - `inciso_c.py`  — genera V(x) y el mapa de contorno (equipotenciales) y guarda imágenes.
  - `inciso_d.py`  — discusión y chequeo numérico: calcula -∇V por diferencias finitas y lo compara con E analítico.
  - `potencial_2d.py` — wrapper que ejecuta `inciso_c` y `inciso_d` (mantiene compatibilidad con ejecuciones antiguas).

Dependencias (recomendado crear un entorno virtual)

Requeridas:
- Python 3.8+
- numpy
- matplotlib

Opcional (mejora algunas utilidades):
- scipy (solo para fsolve; si falta, se usa un método simple propio)

Instalación rápida (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -U pip
pip install numpy matplotlib scipy
```

Ejemplos de uso

Ejecutar el wrapper (genera las figuras y imprime el chequeo numérico):

```powershell
python "Potencial Electrico\potencial_2d.py" --arr two_pos --out plots/potencial
```

Ejecutar sólo el inciso c (gráficos):

```powershell
python "Potencial Electrico\inciso_c.py" --arr two_pos --out plots/potencial_c
```

Ejecutar sólo el inciso d (discusión / chequeo numérico):

```powershell
python "Potencial Electrico\inciso_d.py" --arr two_pos
```

Salida esperada
- Archivos PNG guardados en la carpeta `plots/` (prefijo definido con `--out`), por ejemplo `plots/potencial_equipotentials.png` y `plots/potencial_V_vs_x.png`.
- Mensajes en consola con el chequeo numérico (ángulo entre -∇V y E en puntos de muestra).

Notas
- Evitar puntos muy cercanos a las cargas cuando se haga el chequeo numérico (singularidades).
- `incisos_common.py` contiene las funciones físicas (Coulomb, campo, potencial, utilidades de graficado).

Si querés, puedo:
- añadir un `requirements.txt` y/o tests unitarios mínimos,
- incluir argumentos CLI extra para `inciso_d.py` (puntos de muestreo, h de diferencias finitas) y guardar resultados en CSV.
