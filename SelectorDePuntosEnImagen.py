import cv2
import csv
import numpy as np
import os
from collections import OrderedDict

class SelectorDePuntosEnImagen:
    def __init__(self, ruta_imagenes, archivo_csv, directorio_guardado, color_numeros=(125, 0, 0), columnas=8, filas=5, tamano_celda_mm=1):
        self.ruta_imagenes = ruta_imagenes
        self.archivo_csv = archivo_csv
        self.directorio_guardado = directorio_guardado
        self.color_numeros = color_numeros
        self.columnas = columnas
        self.filas = filas
        self.tamano_celda_mm = tamano_celda_mm
        self.datos_csv = self.cargar_datos_csv()
        self.resultados_matriz = {}
        self.current_matriz = None

    def cargar_datos_csv(self):
        datos = []
        try:
            with open(self.archivo_csv, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                datos_unicos = OrderedDict()
                for row in reader:
                    datos_unicos[row['imagen']] = row
                datos = list(datos_unicos.values())
        except FileNotFoundError:
            print(f"No se encontró el archivo {self.archivo_csv}. Se creará uno nuevo.")
        return datos

    def procesar_imagenes(self):
        for fila_datos in self.datos_csv:
            nombre_imagen = fila_datos['imagen']
            if nombre_imagen in self.resultados_matriz:
                print(f"Imagen {nombre_imagen} ya procesada, saltando...")
                continue

            ruta_imagen = os.path.normpath(os.path.join(self.ruta_imagenes, nombre_imagen))
            print(f"\nProcesando imagen: {ruta_imagen}")

            imagen = cv2.imread(ruta_imagen)
            if imagen is None:
                print(f"Advertencia: No se pudo cargar la imagen en {ruta_imagen}")
                continue

            punto_medio_x = int(fila_datos['punto_medio_x'])
            punto_medio_y = int(fila_datos['punto_medio_y'])
            mm_por_pixel = float(fila_datos['mm_por_pixel'])

            # Calcular tamaño en píxeles de cada celda basándonos en mm_por_pixel
            ancho_celda = int(self.tamano_celda_mm * mm_por_pixel)
            alto_celda = int(self.tamano_celda_mm * mm_por_pixel)

            # Calcular posición inicial de la grilla centrada en el punto medio
            inicio_x = punto_medio_x - (self.columnas // 2) * ancho_celda
            inicio_y = punto_medio_y - self.filas * alto_celda

            # Matriz de selección de puntos
            self.current_matriz = np.zeros((self.filas, self.columnas), dtype=int)

            print("\nInstrucciones:")
            print("- Haz clic izquierdo en las celdas para marcarlas (1)")
            print("- Haz clic derecho en las celdas para desmarcarlas (0)")
            print("- Presiona 'q' para finalizar con esta imagen")
            print("- Presiona 'r' para reiniciar la matriz actual")

            # Seleccionar puntos sin dibujar grilla adicional
            self.seleccionar_puntos(imagen, inicio_x, inicio_y, ancho_celda, alto_celda)

            # Guardar resultados
            self.resultados_matriz[nombre_imagen] = {
                'imagen': nombre_imagen,
                'punto_medio_x': fila_datos['punto_medio_x'],
                'punto_medio_y': fila_datos['punto_medio_y'],
                'mm_por_pixel': fila_datos.get('mm_por_pixel', '1.0'),
                'matriz': self.current_matriz.tolist()
            }

            # Guardar imagen con la matriz de ceros y unos
            self.guardar_imagen_con_matriz(imagen, nombre_imagen, inicio_x, inicio_y, ancho_celda, alto_celda)

    def seleccionar_puntos(self, imagen, inicio_x, inicio_y, ancho_celda, alto_celda):
        ventana = "Seleccionar Puntos"

        def marcar_punto(event, x, y, flags, param):
            if event in [cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONDOWN]:
                # Calcular la posición en la grilla
                col = int((x - inicio_x) / ancho_celda)
                fila = int((y - inicio_y) / alto_celda)

                # Verificar que el clic esté dentro de la grilla
                if 0 <= fila < self.filas and 0 <= col < self.columnas:
                    # Marcar o desmarcar el punto
                    valor = 1 if event == cv2.EVENT_LBUTTONDOWN else 0
                    self.current_matriz[fila, col] = valor
                    print(f"{'Marcado' if valor == 1 else 'Desmarcado'} punto en fila {fila}, columna {col}")

        cv2.namedWindow(ventana)
        cv2.setMouseCallback(ventana, marcar_punto)

        while True:
            img_mostrar = imagen.copy()
            self.mostrar_seleccion(img_mostrar, inicio_x, inicio_y, ancho_celda, alto_celda)
            cv2.imshow(ventana, img_mostrar)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.current_matriz = np.zeros((self.filas, self.columnas), dtype=int)
                print("Matriz reiniciada")

        cv2.destroyAllWindows()

    def mostrar_seleccion(self, imagen, inicio_x, inicio_y, ancho_celda, alto_celda):
        # Mostrar selección sobre la grilla existente
        for fila in range(self.filas):
            for col in range(self.columnas):
                # Dibujar un 1 o un 0 según el valor en la matriz
                valor = self.current_matriz[fila, col]
                x = inicio_x + col * ancho_celda + ancho_celda // 2 - 10
                y = inicio_y + fila * alto_celda + alto_celda // 2 + 10
                cv2.putText(imagen, str(valor), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.color_numeros, 1)


    def guardar_imagen_con_matriz(self, imagen_original, nombre_imagen, inicio_x, inicio_y, ancho_celda, alto_celda):
        # Crear una copia de la imagen original
        imagen_matriz = imagen_original.copy()

        # Dibujar la matriz de ceros y unos sobre la imagen
        for fila in range(self.filas):
            for col in range(self.columnas):
                valor = self.current_matriz[fila, col]
                # Definir la posición de la celda
                x = inicio_x + col * ancho_celda + ancho_celda // 2 - 10
                y = inicio_y + fila * alto_celda + alto_celda // 2 + 10

                # Colocar el texto en la imagen
                cv2.putText(imagen_matriz, str(valor), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.color_numeros, 1)

        # Guardar la imagen en el directorio especificado
        if not os.path.exists(self.directorio_guardado):
            os.makedirs(self.directorio_guardado)
        nombre_archivo_guardado = os.path.join(self.directorio_guardado, nombre_imagen)
        cv2.imwrite(nombre_archivo_guardado, imagen_matriz)
        print(f"Imagen guardada con la matriz de ceros y unos en {nombre_archivo_guardado}")

    def asignar_matriz_manual(self, nombre_imagen, matriz_manual):
        """
        Asigna una matriz manualmente y genera una imagen con la matriz dada.

        :param nombre_imagen: Nombre de la imagen a procesar.
        :param matriz_manual: Matriz 2D de ceros y unos que se utilizará para la imagen.
        """
        # Verificar que la matriz manual tenga el tamaño correcto
        if len(matriz_manual) != self.filas or any(len(fila) != self.columnas for fila in matriz_manual):
            print("La matriz manual no tiene el tamaño correcto.")
            return

        # Cargar la imagen
        ruta_imagen = os.path.join(self.ruta_imagenes, nombre_imagen)
        imagen = cv2.imread(ruta_imagen)
        if imagen is None:
            print(f"No se pudo cargar la imagen en {ruta_imagen}")
            return

        # Obtener los datos de la imagen desde el CSV
        fila_datos = next((fila for fila in self.datos_csv if fila['imagen'] == nombre_imagen), None)
        if fila_datos is None:
            print(f"No se encontraron datos para la imagen {nombre_imagen} en el archivo CSV.")
            return

        # Extraer el punto medio y mm_por_pixel desde el CSV
        punto_medio_x = int(fila_datos['punto_medio_x'])
        punto_medio_y = int(fila_datos['punto_medio_y'])
        mm_por_pixel = float(fila_datos['mm_por_pixel'])

        # Calcular tamaño en píxeles de cada celda
        ancho_celda = int(self.tamano_celda_mm * mm_por_pixel)
        alto_celda = int(self.tamano_celda_mm * mm_por_pixel)

        # Calcular posición inicial de la grilla centrada en el punto medio
        inicio_x = punto_medio_x - (self.columnas // 2) * ancho_celda
        inicio_y = punto_medio_y - self.filas * alto_celda

        # Guardar la matriz manual como la matriz actual
        self.current_matriz = np.array(matriz_manual)

        # Dibujar y guardar la imagen con la matriz
        self.guardar_imagen_con_matriz(imagen, nombre_imagen, inicio_x, inicio_y, ancho_celda, alto_celda)
        print(f"Imagen con matriz manual guardada para {nombre_imagen}")

    def guardar_csv(self):
        fieldnames = ['imagen', 'punto_medio_x', 'punto_medio_y', 'mm_por_pixel', 'matriz']

        with open(self.archivo_csv, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for resultado in self.resultados_matriz.values():
                resultado_copy = resultado.copy()
                resultado_copy['matriz'] = str(resultado_copy['matriz'])
                writer.writerow(resultado_copy)
        print(f"Resultados guardados en {self.archivo_csv}")
