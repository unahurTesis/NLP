import tensorflow as tf

from src.Perceptron import preparar_datos, crear_modelo

if __name__ == "__main__":
    RANDOM_STATE = 42  # -> Semilla para la generación de números aleatorios

    # Cargar los datos
    datos = 'datos_procesados/datos_para_entrenamiento.npz'

    # Preparar los datos
    X_train, X_test, y_train, y_test = preparar_datos(datos)

    # Parámetros del modelo
    ETA = 0.0001
    OPTIMIZER = tf.keras.optimizers.Adam(learning_rate=ETA)
    CAPA_ENTRADA = (X_train.shape[1],)
    CAPAS_OCULTAS = [128, 64]
    CAPA_SALIDA = 40
    LOSS = 'mse'
    ACT_OCULTA = 'tanh'
    ACT_SALIDA = 'sigmoid'

    # Entrenamiento
    EPOCAS = 100
    BATCH_SIZE = 10

    modelo = crear_modelo(
        OPTIMIZER,
        capa_entrada=CAPA_ENTRADA,
        capas_ocultas=CAPAS_OCULTAS,
        capa_salida=CAPA_SALIDA,
        loss=LOSS,
        activation_oculta=ACT_OCULTA,
        activation_salida=ACT_SALIDA
    )
