# Clase DibujarGrilla

La clase `DibujarGrilla` permite dibujar una grilla en imágenes especificadas en un archivo CSV. La grilla está centrada en un punto de referencia de la imagen y tiene celdas de 1mm x 1mm según la escala de píxeles por milímetro proporcionada en el archivo CSV. La clase también permite guardar las imágenes procesadas en un directorio de salida.

## Atributos

- `ruta_csv` (str): Ruta al archivo CSV que contiene los datos de las imágenes.
- `directorio_imagenes` (str): Ruta al directorio que contiene las imágenes de entrada.
- `directorio_salida` (str): Ruta al directorio donde se guardarán las imágenes procesadas.
- `filas_grilla` (int): Número de filas de la grilla (por defecto 5).
- `columnas_grilla` (int): Número de columnas de la grilla (por defecto 8).
- `tamano_celda_mm` (float): Tamaño de cada celda en milímetros (por defecto 1mm).
- `datos` (DataFrame): Datos del archivo CSV que contiene la información de las imágenes.

## Métodos

### `__init__(self, ruta_csv, directorio_imagenes, directorio_salida, filas_grilla=5, columnas_grilla=8, tamano_celda_mm=1)`

Constructor de la clase `DibujadorGrilla`.

#### Parámetros

- `ruta_csv` (str): Ruta al archivo CSV con los datos de las imágenes.
- `directorio_imagenes` (str): Directorio donde se encuentran las imágenes originales.
- `directorio_salida` (str): Directorio donde se guardarán las imágenes procesadas.
- `filas_grilla` (int): Número de filas de la grilla. (Opcional, por defecto 5)
- `columnas_grilla` (int): Número de columnas de la grilla. (Opcional, por defecto 8)
- `tamano_celda_mm` (float): Tamaño de cada celda en milímetros. (Opcional, por defecto 1)

### `cargar_csv(self)`

Carga los datos del archivo CSV en un DataFrame de pandas.

#### Retorno

- `DataFrame`: Los datos del archivo CSV.

### `dibujar_grilla_en_imagen(self, nombre_imagen, pixeles_por_mm, punto_medio_x, punto_medio_y)`

Dibuja la grilla en la imagen especificada, centrada en el punto medio y con el tamaño de las celdas ajustado según los milímetros por píxel.

#### Parámetros

- `nombre_imagen` (str): Nombre del archivo de imagen.
- `pixeles_por_mm` (float): Relación de píxeles por milímetro.
- `punto_medio_x` (int): Coordenada X del punto medio.
- `punto_medio_y` (int): Coordenada Y del punto medio.

### `procesar_imagenes(self)`

Itera sobre todas las filas en el archivo CSV y procesa cada imagen dibujando la grilla en la posición indicada. Las imágenes procesadas se guardan en el directorio de salida especificado.

---


