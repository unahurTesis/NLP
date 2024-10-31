import numpy as np

from sklearn.model_selection import train_test_split
from tensorflow.keras import models, layers
from tensorflow.keras.optimizers import Adam
# Ruta al archivo de datos guardado
ruta_guardado = 'datos_procesados/datos_para_entrenamiento.npz'

ETA = 0.0001
OPTIMIZER = Adam(learning_rate=ETA)
EPOCAS = 10000
BATCH_SIZE=10

# Cargar el archivo .npz
datos = np.load(ruta_guardado)

# Extraer X e y
X = datos['X']
y = datos['y']

# Aplanar y  forma original (54,8,5) -> (54,40)
y = y.reshape(54, 40)

# Imprimir las formas de X e y
print(f"Forma de X: {X.shape}")
print(f"Forma de y: {y.shape}")

# Separar en entrenamiento y prueba (ej. 80% entrenamiento y 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
model = models.Sequential([
    layers.Input(shape=(6,)),
    layers.Dense(64, activation='tanh'),
    layers.Dense(128, activation='tanh'),
    layers.Dense(40, activation='sigmoid')
])

# Compilar el modelo
model.compile(OPTIMIZER, loss='mse')
model.summary()

# Entrenar el modelo
model.fit(X_train, y_train, epochs=EPOCAS, batch_size=BATCH_SIZE)
model.save('modelo_perceptron.h5')
print("Modelo guardado exitosamente.")
