import pandas as pd

from DibujarGrilla import DibujadorGrilla
from SelectorDePuntosEnImagen import SelectorDePuntosEnImagen
if __name__ == "__main__":

    ruta_csv = 'datos/escala.csv'
    directorio_imagenes = 'imagenes/grilla'
    directorio_guardado = "imagenes/procesadas"
    imagen = 'Cordon1_Seccion 1 horizontal C1.jpg'

    datos = 'datos/escala.csv'

    procesador = SelectorDePuntosEnImagen(
        ruta_imagenes=directorio_imagenes,
        archivo_csv=datos,
        directorio_guardado=directorio_guardado,
        columnas=8,
        filas=5
    )

    matriz_manual = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1]
    ]

    procesador.asignar_matriz_manual(imagen, matriz_manual)

    #procesador.procesar_imagenes()
