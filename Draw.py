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

    def drawScreen(self, state):
        for y in range(self.board.height):
            for x in range(self.board.width):
                if [x, y] in self.board.killSquares:
                    image = 'killSq'
                else:
                    image = 'safeSq'
                self.screen.blit(self.images[image], (x*SQUAREWIDTH, y*SQUAREHEIGHT))
                if self.board.player.x == x and self.board.player.y == y:
                    plyImg = pygame.transform.rotate(self.images[self.board.player.image], dirRotation[self.board.player.dire])
                    self.screen.blit(plyImg, (x*SQUAREWIDTH, y*SQUAREHEIGHT))

        for bullet in self.board.bullets:
            self.screen.blit(self.images["bullet"], (bullet.x*SQUAREWIDTH, bullet.y*SQUAREHEIGHT))
        
        pygame.display.flip()
