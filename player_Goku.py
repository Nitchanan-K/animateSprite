import pygame
from debug import debug 
from settings import *
from support import import_folder
from debug import debug

class Player_Goku(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 200
        self.pos_y = 200
        self.image = pygame.image.load('graphics/Goku/standing/standing_0.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.pos_x,self.pos_y))
        self.gravity = 1
        
        # graphics setup
        self.import_player_assets()
        self.status = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.17
        
        # movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        # jump
        self.jumping = False
        self.jump_cooldown = 2000
        self.jump_time = None
        self.jump_height = 20
        self.y_velocity = self.jump_height
        # walk
        self.walk = False

    def import_player_assets(self):
        character_path = 'graphics/Goku/'
        self.animations = {'walk_backward':[],'walk_forward':[],'block':[],'idle':[],'jump':[],'powerup':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

            print(full_path)
            print(self.animations[animation])
        
        
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.pos_x += 4 # speed
            self.status = 'walk_forward'
            self.walk = True
            debug(self.direction.x,self.direction.y)
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.pos_x -= 3 # speed
            self.status = 'walk_backward'
            self.walk = True
            debug(self.direction.x,self.direction.y)
        else:
            self.direction.x = 0

        # jump
        if keys[pygame.K_SPACE] and self.pos_y >= 200 and not self.jumping :
                self.jumping = True
                self.create_jump()
                self.jump_time = pygame.time.get_ticks()
                debug(self.jumping)
           
        # powerup
        if keys[pygame.K_s] and not self.walk:
            self.status = 'powerup' 
            self.direction.x = -2
            debug(self.direction.x,self.direction.y)

    def create_jump(self):
        self.direction.y = 1
        self.gravity -= 20
        self.status = 'jump' 
      
    def apply_gravity(self):
        self.gravity += 1
        self.pos_y += self.gravity
        if self.pos_y  >= 200:
            self.pos_y  = 200
            self.direction.y = 0
            self.jumping = False # fix later
            
    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            self.status = 'idle'
            self.walk = False
            if self.direction.x == -2:
                self.status = 'powerup'
        elif self.direction.y == 1: # to kept jump_3 animation in air
            self.status = 'jump'
          
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.jumping:
            if current_time - self.jump_time >= self.jump_cooldown:
                self.jumping = True


    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0 

            if self.walk:
                self.frame_index = len(animation) - 1 
            

		# set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(midbottom = (self.pos_x,self.pos_y))
        #self.rect.midbottom = [self.pos_x,self.pos_y]
        

    def update(self):
        
        self.apply_gravity()
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()


    
