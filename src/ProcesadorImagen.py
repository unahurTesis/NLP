import csv
import os.path
import cv2
import numpy as np


def calcular_mm_por_pixel(longitud_pixeles, escala_mm):
    if escala_mm == 0:
        raise ValueError('La longitud en pixeles no puede ser cero')
    return longitud_pixeles / escala_mm


def guardar_en_csv(datos, archivo_csv):
    try:
        archivo_existe = os.path.exists(archivo_csv)
        with open(archivo_csv, 'a', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=datos.keys())
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(datos)
        print(f"Datos guardados en {archivo_csv}")
    except Exception as e:
        print(f"Error al guardar datos en el archivo CSV: {e}")


class ProcesadorImagen:

    def __init__(self):
        self.puntos_escala = []
        self.puntos_referencia = []
        self.imagen = None

    def click_mouse_escala(self, evento, x, y, flags, imagen):
        if evento == cv2.EVENT_LBUTTONDOWN:
            self.puntos_escala.append((x, y))
            cv2.circle(imagen, (x, y), 3, (255, 0, 0), -1)
            cv2.imshow('Imagen', imagen)

    def click_mouse_referencia(self, evento, x, y, flags, imagen):
        if evento == cv2.EVENT_LBUTTONDOWN:
            self.puntos_referencia.append((x, y))
            cv2.circle(imagen, (x, y), 3, (155, 255, 0), -1)
            cv2.imshow('Imagen', imagen)

    def obtener_longitud_pixeles(self, imagen):
        self.puntos_escala = []
        imagen_copia = imagen.copy()
        cv2.imshow('Imagen', imagen_copia)
        cv2.setMouseCallback('Imagen', self.click_mouse_escala, imagen_copia)

        while len(self.puntos_escala) < 2:
            if cv2.waitKey(1) & 0xFF == 27:
                print('Operación cancelada por el usuario')
                cv2.destroyAllWindows()
                return None
        cv2.destroyAllWindows()

        if len(self.puntos_escala) == 2:
            return np.sqrt(
                (self.puntos_escala[1][0] - self.puntos_escala[0][0]) ** 2 +
                (self.puntos_escala[1][1] - self.puntos_escala[0][1]) ** 2
                )
        else:
            return None

    def obtener_punto_medio(self, imagen):
        self.puntos_referencia = []
        imagen_copia = imagen.copy()
        cv2.imshow('Imagen', imagen_copia)
        cv2.setMouseCallback('Imagen', self.click_mouse_referencia, imagen_copia)

        while len(self.puntos_referencia) < 2:
            if cv2.waitKey(1) & 0xFF == 27:
                print('Operación cancelada por el usuario')
                cv2.destroyAllWindows()
                return None
        cv2.destroyAllWindows()

        if len(self.puntos_referencia) == 2:
            x1, y1 = self.puntos_referencia[0]
            x2, y2 = self.puntos_referencia[1]
            medio_x = (x1 + x2) // 2
            medio_y = (y1 + y2) // 2
            return medio_x, medio_y
        else:
            return None

    def procesar_imagen_directorio(self, ruta_directorio, escala_mm, archivo_csv='escala.csv'):
        if not os.path.isdir(ruta_directorio):
            print('El directorio no existe')
            return

        for nombre_imagen in os.listdir(ruta_directorio):
            ruta_imagen = os.path.join(ruta_directorio, nombre_imagen)
            if not ruta_imagen.lower().endswith(('png', 'jpg', 'jpeg')):
                print(f'El archivo {nombre_imagen} no es una imagen')
                continue
            print(f'Procesando imagen {nombre_imagen}')
            imagen = cv2.imread(ruta_imagen)
            if imagen is None:
                print(f'No se pudo leer la imagen {nombre_imagen}')
                continue

            # Obtener la longitud de la escala en píxeles
            longitud_pixeles = self.obtener_longitud_pixeles(imagen)
            if longitud_pixeles is None:
                print(f'No se pudo obtener la longitud de la escala para la imagen {nombre_imagen}')
                continue

            # Calculo de milimetros por pixel
            try:
                mm_por_pixel = calcular_mm_por_pixel(longitud_pixeles, escala_mm)
                print(f'La imagen {nombre_imagen} tiene {mm_por_pixel:.3f} mm por pixel')
            except ValueError as e:
                print(f'Error: {e}')
                continue

            # Obtener el punto medio de referencia
            punto_medio = self.obtener_punto_medio(imagen)
            if punto_medio is None:
                print(f'No se pudo obtener el punto medio para la imagen {nombre_imagen}')
                continue

            # Guardar los datos en el CSV
            datos = {
                'imagen': nombre_imagen,
                'pixeles': longitud_pixeles,
                'mm_por_pixel': mm_por_pixel,
                'punto_medio_x': punto_medio[0],
                'punto_medio_y': punto_medio[1]
            }

            guardar_en_csv(datos, archivo_csv)
