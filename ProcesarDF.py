import pandas as pd
import numpy as np
import ast
import os

def cargar_archivo(ruta_archivo):
    """
    Carga un archivo Excel o CSV según su extensión.
    """
    try:
        extension = os.path.splitext(ruta_archivo)[1].lower()
        if extension in ['.xlsx', '.xls']:
            return pd.read_excel(ruta_archivo)
        elif extension == '.csv':
            return pd.read_csv(ruta_archivo, encoding='utf-8')
        else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        raise
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        raise

def procesar_matrices(df):
    """
    Procesa la columna 'matriz' del DataFrame y la convierte en arrays numpy.
    """
    if 'matriz' not in df.columns:
        raise ValueError("El DataFrame no contiene la columna 'matriz'")

    def convertir_matriz(texto_matriz):
        try:
            # Reemplazar espacios por comas para el formato correcto
            texto_matriz = texto_matriz.replace(' ', ',')
            return np.array(ast.literal_eval(texto_matriz))
        except Exception as e:
            print(f"Error al convertir matriz: {texto_matriz} - {str(e)}")
            return None

    df['matriz_procesada'] = df['matriz'].apply(convertir_matriz)
    df = df.dropna(subset=['matriz_procesada'])  # Eliminar filas con matrices no procesadas
    return df

def procesarDF(ruta_archivo):
    """
    Procesa el DataFrame desde el archivo especificado y retorna X e y.
    """
    try:
        # Cargar datos originales
        print(f"Cargando archivo: {ruta_archivo}")
        df_original = cargar_archivo(ruta_archivo)
        print(f"Datos cargados exitosamente. Forma del DataFrame: {df_original.shape}")

        # Procesar las matrices
        print("Procesando matrices...")
        df_procesado = procesar_matrices(df_original)
        print(f"Matrices procesadas. Filas resultantes: {len(df_procesado)}")

        # Separar los datos en X e y
        X = df_procesado[['vel alambre', 'flujo gas', 'peri voltaje', 'voltaje', 'corriente', 'ubicacion']].to_numpy()
        y = np.array(df_procesado['matriz_procesada'].tolist())

        return X, y

    except Exception as e:
        print(f"Error en la ejecución del programa: {str(e)}")
        raise

# Ruta del archivo Excel o CSV y de salida
ruta_archivo = 'datos/conjunto_final.xlsx'
ruta_guardado = 'datos_procesados/datos_para_entrenamiento.npz'

# Procesar el DataFrame y obtener X e y
X, y = procesarDF(ruta_archivo)

# Crear el directorio si no existe
directorio_guardado = os.path.dirname(ruta_guardado)
if not os.path.exists(directorio_guardado):
    os.makedirs(directorio_guardado)

# Guardar X e y en un archivo .npz
np.savez(ruta_guardado, X=X, y=y)
print(f"Datos de entrenamiento guardados exitosamente en {ruta_guardado}")

