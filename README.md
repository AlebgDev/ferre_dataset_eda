# 📊 Análisis Exploratorio de Datos (EDA) - RENFE

## 📌 Descripción del Proyecto
Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre un conjunto de datos de viajes en tren de **RENFE**. 
El objetivo principal es comprender la estructura de los datos, identificar patrones en los viajes y analizar la relación entre las diferentes variables del dataset.

## 📂 Estructura del Proyecto
```
📁 eda_ferro_project
│── 📂 data
│   └── thegurus-opendata-renfe-trips.csv  # Dataset con los datos de los viajes de RENFE
│── 📂 eda_ferro
│   ├── load_csv.py       # Funciones para cargar los datos
│   ├── utils.py          # Funciones para el análisis de datos y visualizaciones
│── 📜 EDA_Analysis_RENFE.ipynb  # Jupyter Notebook con el análisis completo
│── 📜 README.md          # Archivo con la descripción del proyecto
```

## 🚀 Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes librerías de Python:
```bash
pip install pandas matplotlib seaborn notebook
```

## 🛠️ Instalación con Entorno Virtual
Si deseas ejecutar el proyecto en un **entorno virtual**, sigue estos pasos:

1. **Crear un entorno virtual**
   ```bash
   python -m venv env
   ```

2. **Activar el entorno virtual**
   - En **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - En **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Ejecución del Proyecto
Para abrir y ejecutar el Jupyter Notebook, sigue estos pasos:
1. Abre una terminal y navega a la carpeta donde está el proyecto:
   ```bash
   cd eda_ferro_project
   ```
2. Inicia Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Abre el archivo **`EDA_Analysis_RENFE.ipynb`** y ejecuta las celdas una por una.

## 📊 Análisis y Conclusiones
### 🔍 **1. Distribución de Precios**
- Los precios de los billetes están mayormente concentrados entre **20€ y 80€**.
- Existen outliers con precios significativamente más altos.

### 🔍 **2. Distribución de la Duración de los Viajes**
- La mayoría de los viajes duran alrededor de **3 horas**.
- Hay muy pocos viajes de **larga duración** (más de 5 horas), lo que indica que el dataset representa mayormente viajes de media distancia.

### 🔍 **3. Relación entre Precio y Duración del Viaje**
- La correlación entre precio y duración es **baja (-0.19)**, lo que sugiere que la duración no es el principal factor en la determinación del precio.
- Factores como la **compañía de tren, tipo de tren y clase de billete** podrían influir más en el precio.

### 🔍 **4. Análisis de Datos Duplicados y Nulos**
- Se encontraron **valores nulos** en las columnas `price`, `fare` y `vehicle_class`, lo que indica que algunas informaciones sobre los billetes no siempre están disponibles.
- Se detectaron **algunas filas duplicadas**, que pueden ser registros redundantes o errores en la recopilación de datos.

### ❓ **Preguntas de Análisis**
1. **¿Cuál es el rango de precios más común en los billetes de tren?**  
   - La mayoría de los precios están entre **20€ y 80€**.
2. **¿Existen diferencias en los precios según la compañía de trenes?**  
   - Se requiere un análisis adicional para comparar precios entre compañías.
3. **¿En qué horario hay más trenes?**  
   - Se puede analizar la distribución de horarios para ver los picos de frecuencia.
4. **¿El precio está relacionado con la duración del viaje?**  
   - Hay una correlación baja (-0.19), lo que indica que otros factores influyen más en el precio.
5. **¿Cuál es la ruta más frecuente en este conjunto de datos?**  
   - Se puede analizar con `df.groupby(['origin', 'destination']).size().sort_values(ascending=False)`.

---

## 📌 Conclusión Final
Este EDA nos ha permitido comprender la distribución de precios, la duración de los viajes y las relaciones entre variables. Se han identificado **tendencias clave**, como el hecho de que la mayoría de los viajes duran alrededor de 3 horas y que la duración del viaje no es un factor determinante en el precio. Además, se detectaron algunos valores nulos y duplicados que podrían requerir limpieza en futuros análisis.

---
**Autor:** Bryan Garcia (AlebgDev)
