"""
Mover objetos con el teclado

"""

import pygame,sys,random
pygame.init()
size=(1200,700)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()



BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#Coordenadas
x = 10
y = 10

#velocidad
x_speed=0
y_speed=0

while True:
    screen.fill(WHITE) 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Eventos teclados
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed=-3
            if event.key == pygame.K_RIGHT:
                x_speed=3

            
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0

    x += x_speed

    pygame.draw.rect(screen,RED, (x,y,100,100))


    
    pygame.display.flip()
    clock.tick(60)


