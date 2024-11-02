# Documentación de SelectorDePuntosEnImagen
## Descripción

La clase `SelectorDePuntosEnImagen` permite seleccionar puntos en una grilla superpuesta sobre imágenes. 
La selección se guarda en una matriz que representa cada celda de la grilla, y los resultados se almacenan en un archivo CSV.

## Funcionalidades
+ Cargar datos desde un archivo CSV para cada imagen (incluyendo el punto medio y la escala en mm por píxel).
+ Superponer una grilla sobre la imagen y seleccionar puntos con clics del mouse.
+ Guardar la selección de puntos en un archivo CSV.

## Parámetros
### `__init__`
Inicializa la clase con los siguientes parámetros:

* `ruta_imagenes` `(str)`: Ruta a la carpeta donde se encuentran las imágenes.
* `archivo_csv` ``(str)``: Ruta al archivo CSV que contiene los datos de las imágenes y en el cual se guardarán los resultados.
* ``columnas`` ``(int, opcional)``: Número de columnas en la grilla. Predeterminado es 8.
* ``filas`` ``(int, opcional)``: Número de filas en la grilla. Predeterminado es 5.
* ``tamano_celda_mm`` ``(float, opcional)``: Tamaño de cada celda en milímetros. Predeterminado es 1 mm.

## Métodos
``cargar_datos_csv``
Carga los datos del archivo CSV, ignorando duplicados. Si el archivo no existe, muestra un mensaje indicando que se creará un nuevo archivo.

+ Retorno: (list): Lista de diccionarios con los datos de cada imagen.

### ``procesar_imagenes``
Procesa cada imagen especificada en el archivo CSV:

+ Verifica si la imagen ya ha sido procesada.
+ Carga la imagen y verifica que exista.
+ Calcula el tamaño de las celdas en píxeles basado en el tamaño en milímetros y la escala mm/píxel.
+ Llama a seleccionar_puntos para permitir al usuario seleccionar los puntos en la grilla.
+ Guarda el resultado en resultados_matriz.

### ``seleccionar_puntos``
Permite al usuario seleccionar puntos en la imagen:

+ Clic izquierdo: marca el punto.
+ Clic derecho: desmarca el punto.
+ Tecla q: finaliza la selección para la imagen.
+ Tecla r: reinicia la selección actual.

### ``mostrar_seleccion``

Muestra la selección de puntos superpuesta en la imagen en tiempo real. Dibuja un círculo rojo sobre las celdas seleccionadas.

### ``guardar_csv``
Guarda los resultados en el archivo CSV especificado, incluyendo la matriz de selección.

## Ejemplo de Ejecución
```python
Copiar código
from SelectorDePuntosEnImagen import SelectorDePuntosEnImagen

if __name__ == "__main__":
    procesador = SelectorDePuntosEnImagen(
        ruta_imagenes="imagenes/grillas",
        archivo_csv="datos/conjunto.csv",
        columnas=8,
        filas=5
    )

    # Procesar imágenes
    procesador.procesar_imagenes()

    # Guardar resultados
    procesador.guardar_csv()
```
Este código crea una instancia de SelectorDePuntosEnImagen, procesa todas las imágenes en la carpeta especificada y guarda los resultados de selección en un archivo CSV.

## Instrucciones para el Usuario
+ Para seleccionar puntos: Usa clic izquierdo en la imagen para marcar (1) y clic derecho para desmarcar (0).
+ Para finalizar la selección de una imagen: Presiona la tecla q.
+ Para reiniciar la selección actual: Presiona la tecla r.

