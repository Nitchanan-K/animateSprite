import pygame, sys
from settings import *
from player_Goku import Player_Goku


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Dargon ball Z')
        self.clock = pygame.time.Clock()


        # Creating the sprites and groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player_Goku())


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
           
                
                
            self.screen.fill('black')
            # set level run here

            # draw player
            self.player.draw(self.screen)
            self.player.update()

            pygame.display.update()
            self.clock.tick(FPS)

            

if __name__ == '__main__':
	game = Game()
	game.run()