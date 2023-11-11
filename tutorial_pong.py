#MINUTO 11

import pygame,sys,random
pygame.init()
size=(800,500)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()


black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

ancho_jugador=20
alto_jugador=90


#Coordenadas y velocidad del jugador 1 y 2
player1_x_coor=50
player1_y_coor=300-45
player1_y_speed=0

player2_x_coor=750
player2_y_coor=300-45
player2_y_speed=0

#Coordenadas de la pelota
pelota_x=400
pelota_y=250
pelota_speed_x=3
pelota_speed_y=3


game_over=False

while not game_over:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               game_over = True

            #AQUÍ DEFINIMOS LOS EVENTOS QUE VAN A SUCEDER
          if event.type == pygame.KEYDOWN:
               #jugador 1
               if event.key == pygame.K_w:
                    player1_y_speed = -3
               if event.key == pygame.K_s:
                    player1_y_speed = 3
            
               #jugador 2
               if event.key == pygame.K_UP:
                    player2_y_speed= -3
               if event.key == pygame.K_DOWN:
                    player2_y_speed = 3
        
          if event.type == pygame.KEYUP:
               #jugador 1
               if event.key == pygame.K_w:
                    player1_y_speed = 0
               if event.key == pygame.K_s:
                    player1_y_speed = 0
               
               #jugador 2
               if event.key == pygame.K_UP:
                    player2_y_speed= 0
               if event.key == pygame.K_DOWN:
                    player2_y_speed = 0
        
     """ PARTE DE DIBUJO Y LÓGICA DEL JUEGO """    
     screen.fill(black) 
    #MODIFICA LAS COORDENADAS PARA DAR MOVIMIENTO A JUGADORES Y PLEOTA
    #Date cuenta de que la parte lógica del juego está dentro del bucle y no fuera

     player1_y_coor += player1_y_speed
     player2_y_coor += player2_y_speed

    #Movimiento pelota, con el condicional para los límites. Esto se hace FUERA DEL BUCLE, para que se actualice bien
     pelota_x += pelota_speed_x
     pelota_y += pelota_speed_y

     if pelota_y > 500 or pelota_y<0:
          pelota_speed_y *= -1
     if pelota_x > 800 or pelota_x < 0:
          pelota_x = 400
          pelota_y = 250
          pelota_speed_x *= -1
          pelota_speed_y *= -1

            

     jugador1= pygame.draw.rect(screen,white,(player1_x_coor, player1_y_coor-45, ancho_jugador, alto_jugador))
     jugador2= pygame.draw.rect(screen,white,(player2_x_coor, player2_y_coor-45, ancho_jugador, alto_jugador))

     pelota=pygame.draw.circle(screen,white,(pelota_x,pelota_y),10)

     #COLISIONES

     if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
          pelota_speed_x*=-1


     """ PARTE DE DIBUJO Y LÓGICA DEL JUEGO """


     pygame.display.flip()
     clock.tick(60)
pygame.quit()








 
    