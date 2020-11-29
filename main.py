import pygame
import random

size=[500,336] #tamanno de la pantalla adecuado a las medidas de los cuadros
pygame.init()
screen=pygame.display.set_mode(size)

#Declaro los colores que se van a utilizar
negro = (0,0,0)
blanco = (255,255,255)
#               morado              azul           naranja                 crema           cafe              
colores = [ (114, 106, 149) , (112, 159, 176) , (238, 127, 30) , (245, 231, 141) , (160, 118, 118)]

screen.fill(negro) #Pinto la ventana de negro

#Medidas de los cuadrados
width=74
height=74
margin = 8

#Crea una matriz de 4 filas y 6 columnas blancas 
matriz = [[blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco]]

pygame.display.set_caption("Color Boxes") #Titulo de la ventana

#Dibuja la matriz
def pintarMatriz():
    for row in range(len(matriz)):  #por cada fila
        for column in range(len(matriz[row])):  #por cada columna
            color = matriz[row][column] #Obtengo el color de la celda
            #Dibujo un rectangulo en la pantalla con el color de la celda y las medidas que establecimos antes
            pygame.draw.rect( screen , color , [(margin+width)*column+margin,(margin+height)*row+margin,width,height] )
            pygame.display.update() #Acualizo la pantalla

#Imprime la matriz
def printmatriz():
    for row in matriz:
        print(row)

#Funcion para solucionar celdas que estan en los margenes
def normalizarResultado(num, esColumna):
    #Se resta 2 y se suma 3 por que la idea es evaluar las celdas vecinas
    #Si si restara 1 y se sumara 2, estariamos evaluando la celda original
    if num == 6 and esColumna:  #Si es columna 6
        return num-2            #Lo convierte en columna 4
    elif num == 4 and not esColumna:    #Si es fila 4
        return num-2                    #Lo convierte en fila 2
    elif num == -1:     #Si es fila o columna -1
        return num+3    #Lo convierte en fila o columna 2
    else:
        return num  #Y sino lo deja igual

#Evalua las celdas vecinas para ver si son del mismo color
def checkCells(column, row, color):
    #Se obitnene las 8 celdas vecinas
    #Se usa la funcion normalizarResultado para las celdas en los margenes
    arriba = matriz[ normalizarResultado(row-1, False) ][ column ]
    abajo = matriz[ normalizarResultado(row+1, False) ][ column ]
    derecha = matriz[ row ][ normalizarResultado(column+1, True) ]
    izquierda = matriz[ row ][ normalizarResultado(column-1, True) ]

    arribaDerecha = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column+1, True) ]
    arribaIzquierda = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column-1, True) ]
    abajoDerecha = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column+1, True) ]
    abajoIzquierda = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column-1, True) ]

    #Si la celda de arriba, la derecha y la de arriba y derecha son del mismo color, se forma un cuadrado de 4 celdas
    if arriba == color and derecha == color and arribaDerecha == color:
        #Por lo tanto las pintamos color negro
        matriz[row][column] = matriz[ normalizarResultado(row-1, False) ][ column ] = matriz[ row ][ normalizarResultado(column+1, True) ] = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column+1, True) ] = negro
    elif arriba == color and izquierda == color and arribaIzquierda == color:
        matriz[row][column] = matriz[ normalizarResultado(row-1, False) ][ column ] = matriz[ row ][ normalizarResultado(column-1, True) ] = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column-1, True) ] = negro
    elif abajo == color and izquierda == color and abajoIzquierda == color:
        matriz[row][column] = matriz[ normalizarResultado(row+1, False) ][ column ] = izquierda = matriz[ row ][ normalizarResultado(column-1, True) ] = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column-1, True) ] = negro
    elif abajo == color and derecha == color and abajoDerecha == color:
        matriz[row][column] = matriz[ normalizarResultado(row+1, False) ][ column ] = matriz[ row ][ normalizarResultado(column+1, True) ] = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column+1, True) ] = negro

def main():   
    cerrar=False #Variable para saber si debo terminar
    while cerrar==False: #Mientras no deba terminar
        pintarMatriz() #Pinto la matriz
        for event in pygame.event.get(): #Obtengo cualquier cosa que se haga en la ventana 
            if event.type == pygame.QUIT:   #Si cierra la ventana
                cerrar=True                 #Debo terminar el programa
            if event.type == pygame.MOUSEBUTTONDOWN:    #Si hice click
                pos = pygame.mouse.get_pos()            #Obtengo la posicion donde hice click
                column=pos[0] // (width+margin)         #Calculo la columna
                row=pos[1] // (height+margin)           #Calculo la fila
                if matriz[row][column] != negro:        #Si no hice click en una celda negra 
                    color = colores[random.randint(0,4)]    #Consigo un color aleatorio de mi lista de colores
                    matriz[row][column] = color             #Le establezco a mi celda ese color
                    checkCells(column,row,color)            #Evaluo si se formo un cuadrado con las celdas vecinas
    pygame.quit ()

main()