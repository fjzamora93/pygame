"""
En esta tercera lección vamos a crear un efecto
de nieve

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



coor_list = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    coor_list.append([x, y])


while True:
    screen.fill(WHITE) 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    for coor in coor_list:
        pygame.draw.circle(screen,RED,coor,2)
        coor[1]+=1
        if coor[1] > 500:
            coor[1]=0



    
    pygame.display.flip()
    clock.tick(60)



