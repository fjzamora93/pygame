"""
En este tutorial veremos la pantalla de Game OVER,
del mismo modo que aprenderemos a introducir texto.

"""


import pygame,random
pygame.mixer.init()

ancho=900
alto=554


black = (0,0,0)
white = (255,255,255)

#CARGAR SONIDOS


class Corazon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #convert alpha es lo que va a quitar el color de fondo
        self.image = pygame.image.load("corazon.png").convert_alpha() 
        self.rect = self.image.get_rect() 
    def update(self):
        self.rect.y +=1
        if self.rect.y > 459:
            self.rect.y = -10
            self.rect.x = random.randrange(ancho)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("proyectil.png").convert_alpha()
        self.sound=pygame.mixer.Sound("laser2.ogg")
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.vector_vertical= False
    
    def disparo(self,player_x,player_y): #self.player.rect.x  self.player.rect.y
        self.rect.x = player_x +30
        self.rect.y = player_y +20
        self.sound.play()
        
    def update(self):
        if self.vector_vertical== True:
            self.rect.y -= 5
            self.image = pygame.image.load("firework_rocket.png").convert_alpha()

        if self.vector_vertical==False:
            self.rect.x += 5
            self.image = pygame.image.load("proyectil.png").convert_alpha()
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y= 0
        #variables del salto
        self.jumping = False
        self.jump_count=20
        self.jump_height=0

    def changespeedx(self,x):
        self.speed_x += x
    
    def update(self): #Establecer la posición de origen, que se modifica con la velocidad
        self.rect.x = 50 + self.speed_x
        self.rect.y= 400 + self.speed_y
    

class Game(object):
    def  __init__(self):
        #Creamos una instancia de game over FALSE
        self.game_over= False
        
        self.score = 0
        
        #Creamos todas las listas donde estamos acumulando cosas
        self.proyectil_list =pygame.sprite.Group()
        self.corazon_list =pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(20):
            corazon=Corazon()
            corazon.rect.x = random.randrange (ancho)
            corazon.rect.y = random.randrange (alto)
            self.corazon_list.add(corazon)
            self.all_sprites_list.add(corazon)
        
        #Vamos a empezar a crear las entidades del juego...
        self.proyectil = Proyectil()
        self.player =Player()
        self.all_sprites_list.add(self.player)
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            
            #LÓGICA DE LOS CONTROLES
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.changespeedx(10)
                if event.key == pygame.K_a:
                    self.player.changespeedx(-10)

            #El control de salto sigue una lógica muy concreto, revisa abajo en la parte lógica lo que está haciendo
                if event.key == pygame.K_w and not self.player.jumping:
                    self.player.jumping = True
                
                if event.key == pygame.K_SPACE:
                    self.proyectil.vector_vertical = False
                    self.proyectil.disparo(self.player.rect.x,self.player.rect.y)

                if event.key == pygame.K_q:
                    self.proyectil.vector_vertical = True
                    self.proyectil.disparo(self.player.rect.x,self.player.rect.y)

                #! Estas dos lineas de código... a ver dónde las meto    
                self.all_sprites_list.add(self.proyectil)
                self.proyectil_list.add(self.proyectil)
                    
            
         # Obtén las coordenadas del ratón
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(f"X: {mouse_x}, Y: {mouse_y}")

        #Se me olvidó qué es esto
        return False
    
    def run_logic(self):
        
        #Introducimos una condición de cuando NO es Game over
        if not self.game_over:
            self.all_sprites_list.update()

            corazon_hit_list = pygame.sprite.spritecollide (self.player,self.corazon_list, True)
            for corazon in corazon_hit_list:
                self.score -= 1
                print (self.score)
            
            success_shot_list=pygame.sprite.spritecollide (self.proyectil,self.corazon_list, True)
            for shot in success_shot_list:
                self.score +=1
                print (self.score)
        
        #Aquí tenemos la lógica del salto
            if self.player.jumping:
                    #Calcula la altura del salto en el momento actual. Utiliza una fórmula simple de parábola para calcular la altura en función del tiempo de salto (self.player.jump_count). A medida que jump_count disminuye, la altura del salto disminuye.
                    self.player.jump_height = self.player.jump_count ** 2 * 0.5
                    #Recalcula la posición del jugador al saltar
                    self.player.rect.y -= self.player.jump_height
                    #Este contador es el que disminuye la altura:
                    self.player.jump_count -= 1
                    #Reestablece todos los valores a 0
                    if self.player.jump_count < 0:
                        self.player.jumping = False
                        self.player.jump_count = 20
                        self.player.jump_height = 0

        #Pero al mismo tiempo, dentro de la lógica, debemos revisar qué sucede cuando Game Over es True
            if len(self.corazon_list)==0:
                self.game_over = True

    def display_frame(self,screen):
        background= pygame.image.load("background.jpg").convert()
        #? Puedes activar la linea de abajo para pasar la pantalla a blanco o el fondo
        screen.fill(white)
        screen.blit(background, [0,0])
        

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
    pygame.display.set_caption("Coordenadas del Ratón")
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