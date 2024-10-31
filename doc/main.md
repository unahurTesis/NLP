# ___Ejecución del Proyecto___: 

---
##  Procesador de Escala de Imágenes

## Pasos para la Ejecución

### 1. Importar la Clase
Primero, importamos la clase `ProcesadorEscala` desde el archivo correspondiente.

```python
from ProcesadorImagen import ProcesadorImagen
````
### 2. Crear una Instancia ```ProcesadorEscala``` para poder utilizar sus métodos.

```python
procesador = ProcesadorImagen()
```

### 3. Definimos las variables necesarias para el procesamiento de las imágenes.

* ___ruta_img___: Directorio que contiene las imágenes.
* ___escala_mm___: Longitud de la escala en milímetros en cada imagen.
* ___ruta_csv___: Nombre de la ruta donde ser guarda el CSV (por defecto, ``'datos/escala.csv'``).

### 4. Llamamos al método ```procesar_imagenes_directorio``` para procesar todas las imágenes en el directorio.
Se abre una ventana con las imagenes del directorio y se seleccionan dos puntos para calcular la escala en milímetros por píxel. 
Se debe seleccionar dos puntos en la imagen haciendo clic en ellos.
Luego, se procesan todas las imágenes del directorio y se guarda la escala en el archivo CSV.

```python
procesador.procesar_imagenes_directorio(ruta_img, escala_mm, ruta_csv)
```

----

## Dibujador de Grilla en Imágenes

## Verificación de los datos
1 - Verificar que el archivo CSV contenga los datos necesarios para dibujar la grilla en las imágenes.
```csv
imagen,pixeles,mm_por_pixel,punto_medio_x,punto_medio_y
Cordon1_Seccion1.jpg,122.0,40.6667,424,222
Cordon1_Seccion3.jpg,117.0,39.0057,413,169
```

* ___imagen___: Nombre de la imagen.
* ___pixeles___: Número de pixeles de referencia (no se usa directamente).
* ___mm_por_pixel___: Escala de milímetros por píxel para ajustar el tamaño de la grilla.
* ___punto_medio_x___: Coordenada X del punto medio de la grilla.
* ___punto_medio_y___: Coordenada Y del punto medio de la grilla.

2 - Asegurarse de que las imágenes estén en el directorio especificado, y que los
nombres coincidan con los de la columna con los del archivo CSV.

## Ejecución del Código

Ejecutar el siguiente código en el archivo `main.py` para dibujar la grilla en las imágenes.

1 - Importar la clase `DibujadorGrilla` desde el archivo correspondiente.

```python
from DibujadorGrilla import DibujadorGrilla
```

2 - Definir las rutas de los archivos y directorios necesarios.

```python
ruta_csv = 'datos/conjunto.csv'
directorio_imagenes = 'imagenes/seleccionadas'
directorio_salida = 'imagenes/grillas'
```

3 - Crear una instancia de la clase `DibujadorGrilla` con los parámetros necesarios.

```python
dibujador = DibujadorGrilla(ruta_csv, directorio_imagenes, directorio_salida)
```

4 - Llamar al método `procesar_imagenes` para dibujar la grilla en las imágenes.

```python
dibujador.procesar_imagenes()
```

## Salida esperada
* Las imágenes procesadas, con una grilla de 8x5 celdas centrada en el punto medio, se guardarán en el directorio especificado `(directorio_salida)`.
* Cada imagen tendrá un punto rojo en el punto de referencia y una leyenda indicando sus coordenadas.

### Ejemplo de Imagen Procesada


---

## Selector de puntos en la imagen

































