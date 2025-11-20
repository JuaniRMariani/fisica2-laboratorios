# Inicio Rápido - Laboratorio 2

## 🚀 Comenzar en 3 pasos

### 1️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:
```bash
pip install numpy matplotlib scipy
```

### 2️⃣ Ejecutar el laboratorio

**Opción recomendada - Menú interactivo:**
```bash
python main.py
```

**Ejecutar todo automáticamente:**
```python
# En Python/IPython:
import inciso_a, inciso_b, inciso_c, helmholtz

inciso_a.main()
inciso_b.main()
inciso_c.main()
helmholtz.main()
```

### 3️⃣ Ver resultados

Los gráficos se guardan automáticamente en la carpeta `plots/`

---

## 📋 Resumen de Archivos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Menú interactivo principal ⭐ |
| `biot_savart.py` | Funciones base de Biot-Savart |
| `inciso_a.py` | Alambre recto |
| `inciso_b.py` | Espira circular |
| `inciso_c.py` | Configuración combinada |
| `helmholtz.py` | Bobinas de Helmholtz |
| `README.md` | Documentación completa |
| `DISCUSION_RESULTADOS.md` | Análisis de resultados |

---

## 💡 Ejemplos Rápidos

### Calcular campo de un alambre

```python
from biot_savart import campo_magnetico_alambre_recto
import numpy as np

punto = np.array([0.1, 0.0, 0.0])  # Posición [m]
B = campo_magnetico_alambre_recto(punto, L=2.0, I=10.0)

print(f"Campo magnético: {B}")
print(f"Magnitud: {np.linalg.norm(B):.6e} T")
```

### Calcular campo de una espira

```python
from biot_savart import campo_magnetico_espira
import numpy as np

punto = np.array([0.0, 0.0, 0.1])  # En el eje
B = campo_magnetico_espira(punto, radio=0.15, I=8.0)

print(f"Campo magnético: {B}")
print(f"Magnitud: {np.linalg.norm(B)*1e6:.2f} μT")
```

### Bobinas de Helmholtz

```python
from helmholtz import campo_helmholtz, campo_helmholtz_analitico_centro
import numpy as np

radio = 0.2
corriente = 5.0

# Campo en el centro
B_centro = campo_helmholtz_analitico_centro(radio, corriente)
print(f"Campo central: {B_centro*1e6:.2f} μT")

# Campo en cualquier punto
punto = np.array([0.05, 0.03, 0.0])
B_total, B1, B2 = campo_helmholtz(punto, radio, corriente)
print(f"Campo en {punto}: {np.linalg.norm(B_total)*1e6:.2f} μT")
```

---

## 🎯 Verificación Rápida

Ejecuta las pruebas de las funciones base:

```bash
python biot_savart.py
```

Deberías ver algo como:
```
======================================================================
PRUEBAS DE FUNCIONES DE BIOT-SAVART
======================================================================

1. Campo magnético de alambre recto (L=1m, I=10A)
   |B| = 2.000000e-05 T

2. Campo magnético de espira (radio=0.1m, I=5A)
   |B| = 2.793522e-05 T
```

---

## ⚠️ Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'numpy'"

**Solución:**
```bash
pip install numpy matplotlib scipy
```

### Los gráficos no se muestran

**Solución:** Asegúrate de que matplotlib esté configurado correctamente:
```python
import matplotlib
matplotlib.use('TkAgg')  # O 'Qt5Agg'
import matplotlib.pyplot as plt
```

### Cálculos muy lentos

**Solución:** Reduce el número de segmentos en las funciones:
```python
# En lugar de n_segmentos=1000
campo_magnetico_alambre_recto(punto, L, I, n_segmentos=500)
```

---

## 📊 Parámetros Típicos

### Valores por defecto en los scripts

| Configuración | L/radio [m] | Corriente [A] | Puntos grilla |
|---------------|-------------|---------------|---------------|
| Alambre recto | L = 2.0 | I = 10.0 | 25×25 |
| Espira | a = 0.15 | I = 8.0 | 25×25 |
| Combinada | L=2.0, a=0.2 | I₁=10, I₂=8 | 30×30 |
| Helmholtz | a = 0.2 | I = 5.0 | 30×30 |

---

## 🔬 Para Modificar Parámetros

Edita las variables en cada script:

```python
# En inciso_a.py, función calcular_campo_punto_especifico():
L = 2.0      # ← Cambia la longitud del alambre
I = 10.0     # ← Cambia la corriente
punto = np.array([0.2, 0.15, 0.0])  # ← Cambia el punto de evaluación
```

---

## 📖 Más Información

- **README.md:** Documentación completa del laboratorio
- **DISCUSION_RESULTADOS.md:** Análisis detallado de resultados y validación

---

**¡Listo para comenzar!** 🎉

Ejecuta `python main.py` y selecciona la opción que desees explorar.
