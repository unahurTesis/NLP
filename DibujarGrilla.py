import cv2
import pandas as pd
import os


class DibujadorGrilla:
    def __init__(self, ruta_csv, directorio_imagenes, directorio_salida, filas_grilla=5, columnas_grilla=8,
                 tamano_celda_mm=1):
        self.ruta_csv = ruta_csv
        self.directorio_imagenes = directorio_imagenes
        self.directorio_salida = directorio_salida
        self.filas_grilla = int(filas_grilla)
        self.columnas_grilla = int(columnas_grilla)
        self.tamano_celda_mm = tamano_celda_mm
        self.datos = self.cargar_csv()

        # Crear el directorio de salida si no existe
        if not os.path.exists(self.directorio_salida):
            os.makedirs(self.directorio_salida)

    def cargar_csv(self):
        return pd.read_csv(self.ruta_csv)

    def dibujar_grilla_en_imagen(self, nombre_imagen, pixeles_por_mm, punto_medio_x, punto_medio_y):
        # Cargar la imagen desde el directorio de imágenes
        ruta_imagen = os.path.join(self.directorio_imagenes, nombre_imagen)
        imagen = cv2.imread(ruta_imagen)

        # Calcular el tamaño de cada celda en píxeles
        tamano_celda_px = int(self.tamano_celda_mm * pixeles_por_mm)

        # Calcular las coordenadas de inicio para centrar la grilla correctamente
        inicio_x = punto_medio_x - (self.columnas_grilla // 2) * tamano_celda_px
        inicio_y = punto_medio_y - self.filas_grilla * tamano_celda_px

        # Dibujar la grilla en la imagen
        for i in range(self.filas_grilla + 1):
            y = inicio_y + i * tamano_celda_px
            cv2.line(
                imagen,
                (inicio_x, y),
                (inicio_x + self.columnas_grilla * tamano_celda_px, y),
                (0, 255, 0),
                1
            )

        for j in range(self.columnas_grilla + 1):
            x = inicio_x + j * tamano_celda_px
            cv2.line(
                imagen,
                (x, inicio_y),
                (x, inicio_y + self.filas_grilla * tamano_celda_px),
                (0, 255, 0),
                1
            )

        # Dibujar el punto de referencia en rojo y añadir una leyenda
        cv2.circle(imagen, (punto_medio_x, punto_medio_y), 2, (0, 0, 255), -1)
        texto = f"Punto ({punto_medio_x}, {punto_medio_y})"
        cv2.putText(
            imagen, texto,
            (punto_medio_x + 5, punto_medio_y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.3,
            (0, 0, 255),
            1
        )

        # Guardar la imagen con la grilla en el directorio de salida
        ruta_salida = os.path.join(self.directorio_salida, f"{nombre_imagen}")
        cv2.imwrite(ruta_salida, imagen)

    def procesar_imagenes(self):
        # Iterar sobre cada fila en el CSV
        for _, fila in self.datos.iterrows():
            nombre_imagen = fila['imagen']
            pixeles_por_mm = fila['mm_por_pixel']
            punto_medio_x = int(fila['punto_medio_x'])
            punto_medio_y = int(fila['punto_medio_y'])
            # Dibujar la grilla en la imagen especificada
            self.dibujar_grilla_en_imagen(nombre_imagen, pixeles_por_mm, punto_medio_x, punto_medio_y)
