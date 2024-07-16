from classBoton import Boton
from funciones_generales import crear_matriz

def crear_teclado (x: int, y: int, width: int, height: int) -> list:
    """
    Crea y devuelve una matriz de botones y letras que representan un teclado de juego.

    Args:
        x (int): La coordenada x inicial para el primer botón del teclado.
        y (int): La coordenada y inicial para el primer botón del teclado.
        width (int): El ancho de cada botón del teclado.
        height (int): La altura de cada botón del teclado.

    Returns:
        list: Una matriz de objetos Letra, representando un teclado organizado en filas y columnas.
    """
    posicion_inicial = x
    
    matriz_letras = crear_matriz (3, 9)
    teclado = "c<./789x456-123+0()="

    indice = 0
    for i in range (len(matriz_letras)):
        x = posicion_inicial
        for j in range (len(matriz_letras[0])):
            letra = teclado [indice]

            path = rf"image\Abecedario\{letra}.PNG"
            path_colision = rf"image\Abecedario\{letra} highlight.PNG"

            boton =  Boton ((x,y), (width, height), path, path_colision)


            matriz_letras[i][j] = letra_boton

            x += width

            indice += 1
        y += height

    return matriz_letras