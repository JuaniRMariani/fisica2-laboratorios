# 📑 Índice del Laboratorio 2 - Ley de Biot-Savart

## 📂 Estructura del Proyecto

```
Laboratorio 2/
│
├── 📘 DOCUMENTACIÓN
│   ├── README.md                    ⭐ Documentación completa del laboratorio
│   ├── INICIO_RAPIDO.md            🚀 Guía rápida de inicio
│   ├── RESUMEN_EJECUTIVO.md        📊 Resumen del proyecto
│   ├── DISCUSION_RESULTADOS.md     🔬 Análisis y conclusiones
│   └── INDEX.md                    📑 Este archivo
│
├── 🐍 CÓDIGO FUENTE
│   ├── main.py                     ⭐ Menú interactivo principal
│   ├── biot_savart.py              🔧 Funciones base de Biot-Savart
│   ├── inciso_a.py                 📐 Alambre recto
│   ├── inciso_b.py                 ⭕ Espira circular
│   ├── inciso_c.py                 🔀 Configuración combinada
│   └── helmholtz.py                🧲 Bobinas de Helmholtz
│
├── 📦 CONFIGURACIÓN
│   └── requirements.txt            📋 Dependencias del proyecto
│
└── 📊 RESULTADOS
    └── plots/                      🖼️ Gráficos generados (14 archivos)
```

---

## 🎯 Por Dónde Empezar

### Si es tu primera vez:
1. Lee: [`INICIO_RAPIDO.md`](INICIO_RAPIDO.md) (5 min)
2. Instala dependencias: `pip install -r requirements.txt`
3. Ejecuta: `python main.py`

### Si quieres entender la teoría:
1. Lee: [`README.md`](README.md) - Sección 1 (Ley de Biot-Savart)
2. Revisa la fórmula matemática implementada
3. Explora: `biot_savart.py` (funciones base con docstrings)

### Si quieres ver resultados inmediatamente:
1. Ejecuta: `python main.py`
2. Selecciona opción 5 (Ejecutar todos)
3. Revisa gráficos en carpeta `plots/`

### Si necesitas modificar parámetros:
1. Abre el inciso correspondiente (a, b, c, o helmholtz)
2. Busca la función `calcular_campo_punto_especifico()`
3. Modifica L, I, radio, corriente según necesites
4. Ejecuta el script

---

## 📚 Guía de Lectura Recomendada

### Nivel Básico
```
1. INICIO_RAPIDO.md          (Comenzar a usar el laboratorio)
2. README.md - Sección 1-4   (Teoría fundamental)
3. Ejecutar main.py          (Ver resultados)
```

### Nivel Intermedio
```
1. README.md completo        (Teoría + metodología)
2. biot_savart.py            (Implementación base)
3. inciso_a.py o inciso_b.py (Casos individuales)
4. DISCUSION_RESULTADOS.md   (Análisis de validez)
```

### Nivel Avanzado
```
1. Todos los archivos .py    (Código completo)
2. DISCUSION_RESULTADOS.md   (Análisis exhaustivo)
3. RESUMEN_EJECUTIVO.md      (Visión global)
4. Modificar y experimentar  (Propios casos)
```

---

## 🔍 Búsqueda Rápida por Tema

### Teoría Electromagnética
- **Ley de Biot-Savart:** [`README.md`](README.md) - Sección 1.1
- **Líneas de campo:** [`README.md`](README.md) - Sección 1.2
- **Principio de superposición:** [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md) - Sección 5.3

### Implementación
- **Funciones base:** [`biot_savart.py`](biot_savart.py)
- **Discretización:** `biot_savart.py` - líneas 20-90
- **Cálculo de grillas:** `biot_savart.py` - líneas 180-220

### Configuraciones Específicas
- **Alambre recto:** [`inciso_a.py`](inciso_a.py)
- **Espira circular:** [`inciso_b.py`](inciso_b.py)
- **Combinación:** [`inciso_c.py`](inciso_c.py)
- **Helmholtz:** [`helmholtz.py`](helmholtz.py)

### Validación
- **Comparación numérico/analítico:** [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md) - Sección 1
- **Errores típicos:** [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md) - Sección 1.1
- **Propiedades físicas:** [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md) - Sección 1.2

### Visualización
- **Gráficos 2D:** Todos los incisos - función `graficar_campo_2D()`
- **Gráficos 3D:** Todos los incisos - función `graficar_campo_3D()`
- **Análisis de variación:** `inciso_a.py` - función `analisis_variacion_distancia()`

---

## 🎓 Objetivos de Aprendizaje por Archivo

### [`biot_savart.py`](biot_savart.py)
- ✓ Entender implementación numérica de integrales
- ✓ Comprender discretización de conductores
- ✓ Aplicar producto vectorial en 3D
- ✓ Crear funciones reutilizables

### [`inciso_a.py`](inciso_a.py) - Alambre Recto
- ✓ Campo de conductor rectilíneo
- ✓ Simetría cilíndrica
- ✓ Variación B ∝ 1/ρ
- ✓ Comparación finito vs infinito

### [`inciso_b.py`](inciso_b.py) - Espira Circular
- ✓ Campo de bucle cerrado
- ✓ Campo en el eje de simetría
- ✓ Fórmula analítica B_z(z)
- ✓ Comportamiento dipolar

### [`inciso_c.py`](inciso_c.py) - Combinado
- ✓ Principio de superposición
- ✓ Suma vectorial de campos
- ✓ Análisis de contribuciones
- ✓ Configuraciones complejas

### [`helmholtz.py`](helmholtz.py) - Bobinas
- ✓ Campo magnético uniforme
- ✓ Condición d = a
- ✓ Aplicaciones prácticas
- ✓ Región de uniformidad

---

## 🛠️ Tareas Comunes

### Ejecutar todo el laboratorio
```bash
python main.py
# Seleccionar opción 5
```

### Ejecutar un inciso específico
```bash
python inciso_a.py    # Alambre recto
python inciso_b.py    # Espira circular
python inciso_c.py    # Combinado
python helmholtz.py   # Helmholtz
```

### Probar funciones base
```bash
python biot_savart.py
```

### Ver resultados sin ejecutar
```bash
# Revisar carpeta plots/
ls plots/
# o en Windows:
dir plots
```

### Instalar/actualizar dependencias
```bash
pip install -r requirements.txt --upgrade
```

### Modificar parámetros
1. Abrir archivo del inciso
2. Buscar función `calcular_campo_punto_especifico()`
3. Modificar valores de L, I, radio, corriente
4. Guardar y ejecutar

---

## 📊 Resultados Esperados

### Gráficos Generados (14 archivos)

**Inciso A - Alambre Recto:**
1. `inciso_a_campo_2D.png` - Campo en plano XY
2. `inciso_a_campo_3D.png` - Vista 3D
3. `inciso_a_variacion_distancia.png` - B vs distancia

**Inciso B - Espira Circular:**
4. `inciso_b_campo_2D_XZ.png` - Campo en plano XZ
5. `inciso_b_campo_2D_XY.png` - Campo en plano XY
6. `inciso_b_campo_3D.png` - Vista 3D
7. `inciso_b_campo_en_eje.png` - Campo en eje z

**Inciso C - Combinado:**
8. `inciso_c_comparacion_2D.png` - Comparación 3 paneles
9. `inciso_c_campo_3D.png` - Vista 3D combinada
10. `inciso_c_campo_eje_z.png` - Campo en eje z

**Helmholtz:**
11. `helmholtz_campo_eje.png` - Campo en eje
12. `helmholtz_campo_2D_central.png` - Plano central
13. `helmholtz_3D.png` - Vista 3D
14. `helmholtz_comparacion_separaciones.png` - Comparativa

### Salida en Consola

Cada script imprime:
- Parámetros de configuración
- Campo magnético en punto específico (forma vectorial)
- Magnitud del campo |B|
- Análisis comparativo con fórmulas analíticas
- Observaciones y validaciones

---

## ❓ FAQ - Preguntas Frecuentes

### ¿Cómo ejecuto el laboratorio?
```bash
python main.py
```

### ¿Qué necesito instalar?
```bash
pip install numpy matplotlib scipy
```

### ¿Dónde están los resultados?
En la carpeta `plots/` se guardan todos los gráficos.

### ¿Puedo modificar parámetros?
Sí, edita las variables en cada archivo `.py` en la función principal.

### ¿Cómo funciona Biot-Savart?
Lee [`README.md`](README.md) - Sección 1.1 para la teoría completa.

### ¿Son correctos los resultados?
Sí, validados con error < 2%. Ver [`DISCUSION_RESULTADOS.md`](DISCUSION_RESULTADOS.md).

### ¿Qué son las bobinas de Helmholtz?
Lee [`helmholtz.py`](helmholtz.py) - función `introduccion_helmholtz()`.

### ¿Puedo usar el código para otros casos?
Sí, las funciones en `biot_savart.py` son totalmente reutilizables.

---

## 🎯 Checklist de Uso

### Primera Ejecución
- [ ] Leer `INICIO_RAPIDO.md`
- [ ] Instalar dependencias
- [ ] Ejecutar `python main.py`
- [ ] Revisar gráficos en `plots/`

### Estudio de Teoría
- [ ] Leer sección 1 del `README.md`
- [ ] Entender ecuación de Biot-Savart
- [ ] Revisar código en `biot_savart.py`
- [ ] Comparar con libros de texto

### Análisis de Resultados
- [ ] Ejecutar todos los incisos
- [ ] Leer `DISCUSION_RESULTADOS.md`
- [ ] Verificar validación con fórmulas
- [ ] Entender limitaciones

### Experimentación
- [ ] Modificar parámetros
- [ ] Ejecutar casos propios
- [ ] Comparar resultados
- [ ] Documentar observaciones

---

## 📖 Referencias Bibliográficas

Incluidas en [`README.md`](README.md) - Sección 8:
- Griffiths - Introduction to Electrodynamics
- Jackson - Classical Electrodynamics
- Reitz, Milford & Christy - Foundations
- Serway & Jewett - Physics for Scientists

---

## 🏆 Autor

**Juan Cruz Mariani**  
Universidad Nacional del Sur  
Física II - Ingeniería en Sistemas  
2025

---

## 📞 Soporte

Para preguntas o problemas:
1. Revisar este índice
2. Leer `INICIO_RAPIDO.md`
3. Consultar `DISCUSION_RESULTADOS.md`
4. Revisar código con comentarios

---

**¡Disfruta explorando el fascinante mundo del magnetismo!** 🧲

---

*Última actualización: Noviembre 2025*
