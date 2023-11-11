"""
En este tutorial veremos la pantalla de Game OVER,
del mismo modo que aprenderemos a introducir texto.

"""


import pygame,random


ancho=900
alto=600


black = (0,0,0)
white = (255,255,255)


class Corazon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("corazon.png").convert() 
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect() 
    def update(self):
        self.rect.y +=1
        if self.rect.y > 459:
            self.rect.y = -10
            self.rect.x = random.randrange(ancho)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x= mouse_pos[0] 
        self.rect.y= mouse_pos[1]
    

class Game(object):
    def  __init__(self):
        #Creamos una instancia de game over FALSE
        self.game_over= False

        self.score = 0
        
        self.corazon_list =pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(20):
            corazon=Corazon()
            corazon.rect.x = random.randrange (ancho)
            corazon.rect.y = random.randrange (alto)
            
            self.corazon_list.add(corazon)
            self.all_sprites_list.add(corazon)
        
        self.player =Player()
        self.all_sprites_list.add(self.player)
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            #CREAMOS UNA NUEVA LÓGICA PARA REINICIAR EL JUEGO
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    if self.game_over:
                        self.__init__()

        return False
    
    def run_logic(self):
        
        #Introducimos una condición de cuando NO es Game over
        if not self.game_over:
            self.all_sprites_list.update()

            corazon_hit_list = pygame.sprite.spritecollide (self.player,self.corazon_list, True)
            for corazon in corazon_hit_list:
                self.score += 1
                print (self.score)

        #Pero al mismo tiempo, dentro de la lógica, debemos revisar qué sucede cuando Game Over es True
            if len(self.corazon_list)==0:
                self.game_over = True

    def display_frame(self,screen):
        screen.fill(white)


        #CREAR LAS CONDICIONES DE LO QUE SE MUESTRA EN PANTALLA
        #Y así aprendemos a meter texto en pantalla (Video Implementando Game Over)
        if self.game_over:
            font= pygame.font.SysFont("arial", 40)
            text = font.render("Game Over, click to Continue", True, black) #Ese True es solo para que se vea más marcado, no funciona
            center_x = (ancho//2 ) - (text.get_width()//2)
            center_y= (alto//2) - (text.get_height()//2)
            screen.blit(text, [center_x, center_y])
        
        if not self.game_over:
            self.all_sprites_list.draw(screen)
        
        pygame.display.flip()

def main():
    pygame.init()

    screen= pygame.display.set_mode([ancho,alto])
    done= False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()