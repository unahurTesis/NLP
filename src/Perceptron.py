import numpy as np
import tensorflow as tf
from keras import Sequential
from sklearn.model_selection import train_test_split

ruta_guardado = 'datos_procesados/datos_para_entrenamiento.npz'


def preparar_datos(ruta, random_state=42):
    datos = np.load(ruta)
    X = datos['X']
    y = datos['y']

    # Aplanar y en la misma forma (54,8,5) -> (54,40)
    y = y.reshape(54, 40)
    # Separar los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    print("Datos preparados exitosamente.")
    print(f"X_train: {X_train.shape}")
    print(f"X_test: {X_test.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"y_test: {y_test.shape}")

    return X_train, X_test, y_train, y_test


def crear_modelo(
        optimizer,
        capa_entrada,
        capas_ocultas,
        capa_salida, loss,
        activation_oculta,
        activation_salida):
    # Crear el modelo
    model = Sequential()
    # Capa de entrada
    model.add(tf.keras.layers.Input(shape=capa_entrada))
    # Capas ocultas
    for capa in capas_ocultas:
        model.add(tf.keras.layers.Dense(capa, activation=activation_oculta))
    # Capa de salida
    model.add(tf.keras.layers.Dense(capa_salida, activation=activation_salida))
    # Compilar el modelo
    model.compile(optimizer=optimizer, loss=loss, metrics=['mean_squared_error'])
    # Resumen del modelo
    model.summary()
    print("Modelo creado exitosamente.")

    return model
