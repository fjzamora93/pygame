import pygame
screen=pygame.display.set_mode([735,459])
clock = pygame.time.Clock()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

done=False

#Cargar imagen, tiene que estar en la misma carpeta
background= pygame.image.load("fondo_pantalla.jpg").convert()
player = pygame.image.load("player.png").convert()

#Quitamos el color de fondo de los png
player.set_colorkey(black)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    x= mouse_pos[0]
    y= mouse_pos[1]

    #En lugar de screen.fill introducimos esta función:
    screen.blit(background, [0,0])
    screen.blit(player,[x,y]) #Le pasamos las coordenadas del mouse

    pygame.display.flip()
    clock.tick(60)
pygame.quit()