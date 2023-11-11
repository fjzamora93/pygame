
import pygame,random
screen=pygame.display.set_mode([735,459])
clock = pygame.time.Clock()
done=False
score=0

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)



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
            self.rect.x = random.randrange(735)

corazon_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
proyectil_list = pygame.sprite.Group()

def generar_corazon():
    for i in range(20):
        corazon=Corazon()
        corazon.rect.x = random.randrange (700)
        corazon.rect.y = random.randrange (400)
        corazon_list.add(corazon)
        all_sprite_list.add(corazon)
        
generar_corazon()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x= mouse_pos[0]
        player.rect.y= 300

player= Player()
all_sprite_list.add(player)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("proyectil.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 5

pygame.init()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            proyectil = Proyectil()
            proyectil.rect.x = player.rect.x + 45
            proyectil.rect.y = player.rect.y -20

            all_sprite_list.add(proyectil)
            proyectil_list.add(proyectil)
        
            

    screen.fill(black)

    all_sprite_list.draw(screen) 
    all_sprite_list.update()
   

    corazon_hit_list= pygame.sprite.spritecollide(player,corazon_list, True)
    



    for proyectil in proyectil_list:
        corazon_hit_list = pygame.sprite.spritecollide(proyectil, corazon_list, True)
        #Y ahora iteramos para que el laser desaparezca
        for corazon in corazon_hit_list:
            all_sprite_list.remove(proyectil)
            proyectil_list.remove(proyectil)
            score +=1
            print (score)
        
        #Y lo quiamos para que no ocupe sitio en la memoria
        if proyectil.rect.y < -10:
            all_sprite_list.remove(proyectil)
            proyectil_list.remove(proyectil)




    pygame.display.flip()
    clock.tick(60)
pygame.quit()