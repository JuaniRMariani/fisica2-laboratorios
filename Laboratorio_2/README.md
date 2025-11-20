# Laboratorio Computacional 2: Ley de Biot-Savart

## Cálculo del Campo Magnético

**Asignatura:** Física II - IS  
**Universidad Nacional del Sur**

---

## Objetivos

El objetivo de este laboratorio computacional es:
- Aplicar la **Ley de Biot-Savart** para calcular el campo magnético generado por configuraciones de corriente estacionarias rectilíneas y espiras.
- Analizar y visualizar el campo magnético calculado mediante algoritmos computacionales.
- Aplicar el **principio de superposición** para configuraciones combinadas.

---

## 1. Ley de Biot-Savart

### 1.1 Campo Magnético de configuraciones finitas

La Ley de Biot-Savart describe el campo magnético generado por una corriente estacionaria en un conductor. Matemáticamente, el campo magnético en un punto **r** del espacio debido a un elemento de corriente **I** que circula por un pequeño segmento **dl'** de un conductor se expresa como:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int \frac{I \, d\mathbf{l'} \times (\mathbf{r} - \mathbf{r'})}{|\mathbf{r} - \mathbf{r'}|^3}$$

donde:
- **B(r)**: campo magnético en la posición **r**
- **μ₀**: permeabilidad del vacío (4π × 10⁻⁷ T·m/A)
- **r'**: posición del elemento de corriente **dl'**
- **I**: corriente eléctrica
- **dl'**: diferencial de longitud en la dirección de la corriente
- **|r - r'|**: distancia entre el punto de cálculo y el elemento de corriente

### 1.2 Líneas de Campo Magnético

Las líneas de campo magnético son representaciones visuales que muestran la dirección y magnitud del campo **B**:

- Son curvas tangentes al vector **B** en cada punto
- Su densidad es proporcional a la magnitud del campo
- No se cruzan entre sí
- Para corrientes cerradas, las líneas son siempre cerradas

---

## 2. Resolución del Campo Magnético

### 2.1 Metodología

El laboratorio se desarrolla en los siguientes pasos:

1. **Funciones Base** (`biot_savart.py`):
   - Función para calcular campo magnético de un alambre recto de longitud L con corriente I₁
   - Función para calcular campo magnético de una espira de radio a con corriente I₂

2. **Alambre Recto Individual** (`inciso_a.py`):
   - Graficar campo magnético en 3D
   - Graficar campo magnético en 2D (plano seleccionado)
   - Calcular campo en punto específico (x₁, y₁, z₁)

3. **Espira Circular Individual** (`inciso_b.py`):
   - Graficar campo magnético en 3D
   - Graficar campo magnético en 2D (plano seleccionado)
   - Calcular campo en punto específico (x₁, y₁, z₁)

4. **Configuración Combinada** (`inciso_c.py`):
   - Alambre recto en el eje de la espira
   - Aplicar principio de superposición
   - Visualizaciones 3D y 2D

5. **Bobinas de Helmholtz** (`helmholtz.py`):
   - Implementación de par de espiras separadas a distancia específica
   - Análisis de región de campo uniforme
   - Aplicaciones prácticas

---

## 3. Estructura del Proyecto

```
Laboratorio 2/
├── README.md                 # Este archivo
├── biot_savart.py           # Funciones base de Biot-Savart
├── inciso_a.py              # Alambre recto
├── inciso_b.py              # Espira circular
├── inciso_c.py              # Configuración combinada
├── helmholtz.py             # Bobinas de Helmholtz
└── plots/                   # Gráficos generados
```

---

## 4. Dependencias

```bash
# Instalar dependencias necesarias
pip install numpy matplotlib scipy
```

**Paquetes requeridos:**
- `numpy`: Cálculos numéricos y arrays
- `matplotlib`: Visualización y gráficos
- `scipy`: Funciones científicas (opcional)

---

## 5. Cómo Ejecutar

### Opción 1: Menú Interactivo (Recomendado)

```bash
cd "Laboratorio 2"
python main.py
```

El menú interactivo permite:
- Ejecutar cada inciso individualmente
- Ejecutar todos los análisis secuencialmente
- Probar las funciones base
- Ver resultados organizadamente

### Opción 2: Ejecutar Scripts Individuales

```bash
# Alambre recto
python inciso_a.py

# Espira circular
python inciso_b.py

# Configuración combinada
python inciso_c.py

# Bobinas de Helmholtz
python helmholtz.py

# Probar funciones base
python biot_savart.py
```

### Opción 3: Importar como Módulo

```python
from biot_savart import campo_magnetico_alambre_recto, campo_magnetico_espira
import numpy as np

# Calcular campo de un alambre
punto = np.array([0.1, 0.0, 0.0])
B = campo_magnetico_alambre_recto(punto, L=1.0, I=10.0)
print(f"Campo magnético: {B} T")
```

---

## 6. Resultados Esperados

Cada script genera:
- **Cálculos numéricos** con resultados en consola
- **Gráficos 2D y 3D** guardados en `plots/`
- **Análisis comparativos** con fórmulas analíticas
- **Validaciones** de precisión y consistencia

**Gráficos generados:**

```
plots/
├── inciso_a_campo_2D.png              # Campo de alambre (plano XY)
├── inciso_a_campo_3D.png              # Campo de alambre (3D)
├── inciso_a_variacion_distancia.png   # Análisis vs distancia
├── inciso_b_campo_2D_XZ.png           # Campo de espira (plano XZ)
├── inciso_b_campo_2D_XY.png           # Campo de espira (plano XY)
├── inciso_b_campo_3D.png              # Campo de espira (3D)
├── inciso_b_campo_en_eje.png          # Análisis en eje
├── inciso_c_comparacion_2D.png        # Comparación combinada
├── inciso_c_campo_3D.png              # Campo combinado (3D)
├── inciso_c_campo_eje_z.png           # Análisis en eje z
├── helmholtz_campo_eje.png            # Helmholtz en eje
├── helmholtz_campo_2D_central.png     # Helmholtz plano central
├── helmholtz_3D.png                   # Helmholtz (3D)
└── helmholtz_comparacion_separaciones.png
```

---

## 7. Discusión de Resultados

Se analizarán los siguientes aspectos:

- ¿Cómo varía la magnitud del campo magnético con la distancia al conductor?
- ¿Son las líneas de campo magnético las esperadas?
- ¿Qué puede decir de la validez de los resultados obtenidos a partir de la Ley de Biot-Savart?

**Ver análisis completo en:** [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md)

### Conclusiones Principales

✅ **Validez:** Los resultados numéricos coinciden con fórmulas analíticas (error < 2%)  
✅ **Decaimiento:** El campo decrece como 1/ρ (alambre) o más rápido (espira)  
✅ **Líneas de campo:** Totalmente consistentes con la teoría electromagnética  
✅ **Superposición:** El principio se verifica correctamente  
✅ **Helmholtz:** Región de campo uniforme verificada experimentalmente

---

## 8. Referencias

- Griffiths, D. J. (2017). *Introduction to Electrodynamics* (4th ed.). Cambridge University Press.
- Jackson, J. D. (1999). *Classical Electrodynamics* (3rd ed.). Wiley.
- Reitz, J. R., Milford, F. J., & Christy, R. W. (2008). *Foundations of Electromagnetic Theory*. Addison-Wesley.
- Serway, R. A., & Jewett, J. W. (2018). *Physics for Scientists and Engineers*. Cengage Learning.

### Recursos Online

- [HyperPhysics - Magnetic Field](http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/magfie.html)
- [MIT OpenCourseWare - Physics II: Electricity and Magnetism](https://ocw.mit.edu/courses/physics/)

---

## Autor

**Juan Cruz Mariani**  
Universidad Nacional del Sur
