# Clase ProcesadorImagen

La clase `ProcesadorImagen` permite procesar imágenes en un directorio para calcular la longitud en píxeles de una escala, 
convertir esa longitud a milímetros por píxel, y guardar los datos en un archivo CSV. 
También se puede obtener el punto medio entre dos puntos de referencia en la imagen.

## Dependencias
- `cv2` (OpenCV)
- `numpy`
- `csv`
- `os` `os.path`

## Atributos
- `puntos_escala`: Lista que almacena los puntos seleccionados para medir la escala.
- `puntos_referencia`: Lista que almacena los puntos seleccionados para calcular el punto medio.
- `imagen`: Imagen actual en la que se seleccionan los puntos.

## Métodos

### `click_mouse_escala(evento, x, y, flags, imagen)`
Maneja los eventos de clic del mouse en una imagen.

- **Parámetros**:
  - `evento`: Tipo de evento de clic del mouse.
  - `x`, `y`: Coordenadas del clic.
  - `flags`: Bandera para el evento (sin uso en esta implementación).
  - `imagen`: La imagen donde se realiza el clic.
- **Función**: Dibuja un círculo en el punto seleccionado y almacena las coordenadas en la lista `puntos`.

### `click_mouse_referencia(evento, x, y, flags, imagen)`
Maneja los eventos de clic para definir puntos de referencia.

Parámetros:
evento: Tipo de evento de clic.
x, y: Coordenadas del clic.
flags: Bandera para el evento.
imagen: Imagen donde se realiza el clic.
Función: Almacena el punto en puntos_referencia, dibuja un círculo en el punto, y muestra la imagen actualizada.

### `obtener_longitud_pixeles(imagen)`
Obtiene la longitud en píxeles entre dos puntos seleccionados manualmente en una imagen.

- **Parámetros**:
  - `imagen`: Imagen en la que se realiza la selección de puntos.
- **Retorna**: La distancia en píxeles entre los dos puntos seleccionados o `None` si no se seleccionan dos puntos.

### `obtener_punto_medio(imagen)`
Calcula el punto medio entre dos puntos de referencia seleccionados.

Parámetros:
- imagen: Imagen donde se seleccionan los puntos de referencia.
- Retorna: Coordenadas (medio_x, medio_y) del punto medio o None si no se seleccionan dos puntos.

__Nota__: Presionar "Esc" cancela la selección.

### `calcular_mm_por_pixel(longitud_pixeles, escala_mm)`
Calcula la relación entre milímetros y píxeles en función de una escala dada.

- **Parámetros**:
  - `longitud_pixeles`: Longitud en píxeles entre los puntos seleccionados.
  - `escala_mm`: Longitud de la escala en milímetros.
- **Retorna**: La cantidad de milímetros por píxel.
- **Excepciones**: Lanza un `ValueError` si `escala_mm` es igual a 0.

### `guardar_en_csv(datos, archivo_csv)`
Guarda los datos de longitud y escala en un archivo CSV.

- **Parámetros**:
  - `datos`: Diccionario con las claves `imagen`, `pixeles`, y `mm_por_pixel`, `punto_medio_x`,`punto_medio_y`.
  
  - `archivo_csv`: Nombre del archivo CSV donde se almacenan los datos.
- **Función**: Agrega una fila al archivo CSV o crea el archivo si no existe.

### `procesar_imagenes_directorio(ruta_directorio, escala_mm, archivo_csv='escala.csv')`
Procesa todas las imágenes en un directorio y guarda la escala en milímetros por píxel en un archivo CSV.

- **Parámetros**:
  - `ruta_directorio`: Directorio que contiene las imágenes.
  - `escala_mm`: Longitud de la escala en milímetros en cada imagen.
  - `archivo_csv`: Nombre del archivo CSV (por defecto, 'escala.csv').
- **Función**: Recorre todas las imágenes del directorio, calcula la escala en milímetros por píxel y guarda los datos en el archivo CSV.

---

## Ejemplo de Uso

En `main.py`, puedes crear una instancia de la clase y llamar al método `procesar_imagenes_directorio` para procesar todas las imágenes en un directorio específico.

```python
from src.ProcesadorImagen import ProcesadorImagen

# Crear una instancia de ProcesadorEscala
procesador = ProcesadorImagen()

# Llamar al método para procesar el directorio de imágenes
procesador.procesar_imagenes_directorio(ruta_directorio='ruta/a/tu/directorio', escala_mm=10,
                                        archivo_csv='resultados.csv')
```

## Notas
- Cambiar el valor de la ``escala_mm`` según la longitud de la escala en milímetros en las imágenes.
- El directorio ``ruta_directorio`` debe contener imágenes válidas para el procesamiento (``.jpg``, ``.jpge``).