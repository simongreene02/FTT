SQUAREWIDTH = 32
SQUAREHEIGHT = 32

#pygame (Graphics Program) uses counterclockwise rotation

dirRotation = {1:-0, 2:-90, 3:-180, 4:-270}

import pygame
pygame.init()

class ScreenMaker:
    def __init__(self, board): #add menu argument
        self.screen_size = widthA, heightA = board.width * SQUAREWIDTH, board.height * SQUAREHEIGHT
        self.screen = pygame.display.set_mode(self.screen_size)
        self.board = board
        self.images = {}
        self.images['safeSq'] = pygame.image.load("Safe_Square.bmp")
        self.images['killSq'] = pygame.image.load("Hazard_Square.bmp")
        self.images['player'] = pygame.image.load("Player.bmp")
        self.images['bullet'] = pygame.image.load("Bullet.bmp")
        self.images['boss'] = pygame.image.load("Boss.bmp")
        self.images['pAU'] = pygame.image.load("Play_Again_Unselected.bmp")
        self.images['qU'] = pygame.image.load("Quit_Unselected.bmp")
        self.images['pAS'] = pygame.image.load("Play_Again_Selected.bmp")
        self.images['qS'] = pygame.image.load("Quit_Selected.bmp")

    def drawScreen(self, state):
        if state == 2:
            self.screen.blit(self.images['pAU'], (50, 25))
            self.screen.blit(self.images['qU'], (50, 175))
        else:
            for y in range(self.board.height):
                for x in range(self.board.width):
                    if [x, y] in self.board.killSquares:
                        image = 'killSq'
                    else:
                        image = 'safeSq'
                    self.screen.blit(self.images[image], (x*SQUAREWIDTH, y*SQUAREHEIGHT))

            #for bullet in self.board.bullets:
                #self.screen.blit(self.images["bullet"], (bullet.x*SQUAREWIDTH, bullet.y*SQUAREHEIGHT))

            for entity in [self.board.player, self.board.boss] + self.board.bullets:
                if entity.stillAlive():
                    entImg = pygame.transform.rotate(self.images[entity.image], dirRotation[entity.dire])
                    self.screen.blit(entImg, (entity.x*SQUAREWIDTH, entity.y*SQUAREHEIGHT))
        
        pygame.display.flip()
