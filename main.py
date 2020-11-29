import pygame
import random

size=[500,336]
pygame.init()
screen=pygame.display.set_mode(size)

negro = (0,0,0)
blanco = (255,255,255)
colores = [ (114, 106, 149) , (112, 159, 176) , (160, 193, 184) , (244, 235, 193) , (160, 118, 118)]

screen.fill(negro)

# Medidas de los cuadrados
width=74
height=74
margin = 8

#Crea una matriz de 4 filas y 6 columnas blancas 
matriz = [[blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco]]

pygame.display.set_caption("Color Boxes")

#Dibuja la matriz
def pintarMatriz():
    for row in range(len(matriz)):
        for column in range(len(matriz[row])):
            color = matriz[row][column]
            pygame.draw.rect( screen , color , [(margin+width)*column+margin,(margin+height)*row+margin,width,height] )
            pygame.display.update() 

#Imprime la matriz
def printmatriz():
    for row in matriz:
        print(row)

def normalizarResultado(num, esColumna):
    if num == 6 and esColumna:
        return num-2
    elif num == 4 and not esColumna:
        return num-2
    elif num == -1:
        return num+3
    else:
        return num

def checkCells(column, row, color):
    arriba = matriz[ normalizarResultado(row-1, False) ][ column ]
    abajo = matriz[ normalizarResultado(row+1, False) ][ column ]
    derecha = matriz[ row ][ normalizarResultado(column+1, True) ]
    izquierda = matriz[ row ][ normalizarResultado(column-1, True) ]

    arribaDerecha = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column+1, True) ]
    arribaIzquierda = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column-1, True) ]
    abajoDerecha = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column+1, True) ]
    abajoIzquierda = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column-1, True) ]

    if arriba == color and derecha == color and arribaDerecha == color:
        matriz[row][column] = matriz[ normalizarResultado(row-1, False) ][ column ] = matriz[ row ][ normalizarResultado(column+1, True) ] = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column+1, True) ] = negro
    elif arriba == color and izquierda == color and arribaIzquierda == color:
        matriz[row][column] = matriz[ normalizarResultado(row-1, False) ][ column ] = matriz[ row ][ normalizarResultado(column-1, True) ] = matriz[ normalizarResultado(row-1, False) ][ normalizarResultado(column-1, True) ] = negro
    elif abajo == color and izquierda == color and abajoIzquierda == color:
        matriz[row][column] = matriz[ normalizarResultado(row+1, False) ][ column ] = izquierda = matriz[ row ][ normalizarResultado(column-1, True) ] = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column-1, True) ] = negro
    elif abajo == color and derecha == color and abajoDerecha == color:
        matriz[row][column] = matriz[ normalizarResultado(row+1, False) ][ column ] = matriz[ row ][ normalizarResultado(column+1, True) ] = matriz[ normalizarResultado(row+1, False) ][ normalizarResultado(column+1, True) ] = negro

def main():   
    cerrar=False
    while cerrar==False:
        pintarMatriz()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                cerrar=True 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                column=pos[0] // (width+margin)
                row=pos[1] // (height+margin)
                if matriz[row][column] != negro:
                    color = colores[random.randint(0,4)]

                    matriz[row][column] = color

                    checkCells(column,row,color)
    pygame.quit ()

main()