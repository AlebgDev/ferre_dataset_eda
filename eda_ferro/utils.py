import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def summarize_data(df):
    """
    Analiza un dataframe de pandas y devuelve un diccionario con informacion relevante
    """
    print("Informacion")
    df.info() # Imprime el tipo de datos de cada columna
    return {
        'shape': df.shape, # Imprime el numero de filas y columnas
        'columns': df.columns, # Imprime el nombre de las columnas
        'describe': df.describe(), # Imprime estadisticas descriptivas
        'nulls': df.isnull().sum(), # Imprime el numero de valores nulos por columna
        'duplicate_rows': df.duplicated().sum(), # Imprime el numero de filas duplicadas
        'unique_values': df.nunique() # Imprime el numero de valores unicos por columna
    }

def plot_correlation(df):
    """
    Genera una matriz de correlación para analizar la relación entre variables numéricas
    """
    if df.select_dtypes(include='number').shape[1] > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Matriz de correlación')
        plt.show()
    
def plot_distribution(df):
    """
    Genera histogramas para analizar la distribución de variables numéricas
    """ 
    
    if 'price' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df['price'], bins=20, kde=True)
        plt.title('Distribución de precios')
        plt.xlabel('Precio')
        plt.ylabel('Frecuencia')
        plt.show()
        
    if 'duration' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df['duration'], bins=20, kde=True)
        plt.title('Distribución de duración')
        plt.xlabel('Duración')
        plt.ylabel('Frecuencia')
        plt.show()
        
    if 'distance' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df['distance'], bins=20, kde=True)
        plt.title('Distribución de distancias')
        plt.xlabel('Distancia')
        plt.ylabel('Frecuencia')
        plt.show()
        
    if 'company' in df.columns:
        plt.figure(figsize=(12, 5))
        sns.countplot(df['company'])
        plt.title('Distribución de compañias')
        plt.xlabel('Compañia')
        plt.ylabel('Frecuencia')
        plt.show()
        
def count_categorical(df, column):
    """
    Cuenta la frecuencia de valores en una columna categórica
    """
    if column in df.columns:
        return df[column].value_counts()
    return None

def plot_boxplot(df, column):
    """
    Genera un boxplot para detectar outliers en una variable numérica
    """
    if column in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot de {column}')
        plt.show()
        
def time_distribution(df):
    """
    Muestra la distribucion de viajes por hora de salida.
    """
    if 'departure' in df.columns and pd.api.types.is_datetime64_any_dtype(df['departure']):
        df['hour'] = df['departure'].dt.hour
        plt.figure(figsize=(10, 5))
        sns.countplot(x=df['hour'])
        plt.title('Distribución de viajes por hora de salida')
        plt.xlabel('Hora de salida')
        plt.ylabel('Frecuencia')
        plt.show()

def price_duration(df):
    """
    Muestra la relación entre precio y duración de los viajes
    """
    if 'price' in df.columns and 'duration' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=df['duration'], y=df['price'])
        plt.title('Relación entre precio y duración')
        plt.xlabel('Duración')
        plt.ylabel('Precio')
        plt.show()
        