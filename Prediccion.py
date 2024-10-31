import numpy as np
from tensorflow.python.keras.models import load_model

# Ruta del modelo guardado y del archivo de datos
ruta_modelo = 'modelo_perceptron'
ruta_datos = 'datos_procesados/datos_para_entrenamiento.npz'

# Cargar el modelo guardado
model = load_model(ruta_modelo)
print("Modelo cargado exitosamente.")

# Cargar los datos de prueba
datos = np.load(ruta_datos)
X = datos['X']
y_real = datos['y']

# Aplanar y en la misma forma (54,8,5) -> (54,40)
y_real = y_real.reshape(54, 40)

# Realizar predicciones con el modelo
predicciones = model.predict(X)

# Imprimir predicciones y comparar con el valor real
for i, (prediccion, real) in enumerate(zip(predicciones, y_real), 1):
    print(f"Predicción {i}: {prediccion}")
    print(f"Valor Real {i}: {real}")
    print("="*40)

# Guardar las predicciones si es necesario
np.savez('predicciones.npz', predicciones=predicciones)
print("Predicciones guardadas en 'predicciones.npz'.")
