import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut1.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut2.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut3.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut4.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut5.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut6.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut7.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut8.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut9.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut10.png'),0,2))
        self.sprites.append(pygame.transform.rotozoom(pygame.image.load('Future Trunks cut11.png'),0,2))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True
    
    def offanimate(self):
        self.is_animating = False

    def update(self,speed):
        if self.is_animating == True:
            self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            #self.is_animating = False

        self.image = self.sprites[int(self.current_sprite)]



# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")


# Creating the sprites and groups
moving_sprites =pygame.sprite.Group()
player = Player(200,100)
moving_sprites.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            player.animate()
        if  not keys[pygame.K_DOWN]:
            player.offanimate()
        #if event.type == pygame.KEYUP:
                #player.offanimate()
       
       
            

    # Drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.2)
    pygame.display.flip()
    clock.tick(60)