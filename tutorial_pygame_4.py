"""
Mover objetos con el MOUSE

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


#Definir visibilidad del mouse
pygame.mouse.set_visible(0) #1 para ver el mouse

while True:
    screen.fill(WHITE) 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    
    mouse_pos = pygame.mouse.get_pos()
    x= mouse_pos[0]
    y=mouse_pos[1]
    print(mouse_pos) #Eso solo imprime en la terminal la posición del mouse


    pygame.draw.rect(screen,RED, (x,y,100,100))


    
    pygame.display.flip()
    clock.tick(60)



