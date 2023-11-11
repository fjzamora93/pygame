"""
En esta segunda lección vamos a aprender a mover objetos

Para hacerlo deberemos crear las variables de coordenadas sobre las que 
después se va a generar un cambio y que dará la sensación de movimiento.


"""

import pygame,sys
pygame.init()

#Definir colores (formato RGB)

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)


size=(1200,700)

#Crear ventana
screen=pygame.display.set_mode(size)
#Controlar los FPS
clock=pygame.time.Clock()

#Creación de variables

coord_x=400
coord_y=200

speed_x=1
speed_y=10


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    ### ---- ZONA LÓGICA
    if coord_x > 950 or coord_x <50:
        speed_x *= -1
    coord_x += speed_x   
    

    if coord_y > 750 or coord_y <200:
        speed_y *= -1
    coord_y += speed_y
    """FIN ZONA LÓGICA"""


    
    ### ----- ZONA DE DIBUJO
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, BLUE, (coord_x,coord_y, 100, 50))

    ### ------ ZONA DE DIBUJO

    #actualizar pantalla
    pygame.display.flip()
    clock.tick(120) #Aquí están los fps