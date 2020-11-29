import pygame
import random

size=[500,336]
pygame.init()
screen=pygame.display.set_mode(size)

# Colours
negro = (0,0,0)
blanco = (255,255,255)
colores = [ (114, 106, 149) , (112, 159, 176) , (160, 193, 184) , (244, 235, 193) , (160, 118, 118)]

screen.fill(negro)

# Medidas de los cuadrados
width=74
height=74
margin = 8

#Crea una matriz de 4 filas y 6 columnas blancas 

grid = [[blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco],
        [blanco, blanco, blanco, blanco, blanco, blanco]]

# Set title of screen
pygame.display.set_caption("Color Boxes")



#Dibuja la matriz
def pintarMatriz():
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = grid[row][column]
            pygame.draw.rect( screen , color , [(margin+width)*column+margin,(margin+height)*row+margin,width,height] )
            pygame.display.update() 

#Imprime l matriz
def printMatrix():
    for row in grid:
        print(row) 

# -------- Main Program Loop -----------
def main():   
    cerrar=False
    pintarMatriz()
    printMatrix()
    while cerrar==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                cerrar=True # Flag that we are cerrar so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()

                column=pos[0] // (width+margin)
                row=pos[1] // (height+margin)

                grid[row][column] = colores[random.randint(0,4)]
                
                pintarMatriz()
                print("Click ",pos,"Grid coordinates: ",row,column)
        
    pygame.quit ()

main()