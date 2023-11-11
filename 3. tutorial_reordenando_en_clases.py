"""
Hasta ahora todo el texto era bastante caótico.

En este tutorial vamos a introducir una nueva clase (game). 
Dentro de esa clase se van a checkar tres cosas distintas:

1. Los eventos que suceden.
2. La lógica de dichos eventos.
3. Lo que aparece en pantalla.


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
        return False
    
    def run_logic(self):
        self.all_sprites_list.update()

        corazon_hit_list = pygame.sprite.spritecollide (self.player,self.corazon_list, True)
        for corazon in corazon_hit_list:
            self.score += 1
            print (self.score)

    def display_frame(self,screen):
        screen.fill(white)
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