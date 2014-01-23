import pygame, Square_Gen, Draw, sys
pygame.init()

width = 11
height = 11

STATE_RUNNING = 1
STATE_MENU = 2
STATE_GAMEOVER = 3

mb = Square_Gen.Board(width, height)

s = Draw.ScreenMaker(mb)

gameState = STATE_MENU

isTurnTaken = True

def inputGameRunning(event):
    global isTurnTaken

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYUP and event.key == pygame.K_w:
        mb.player.move(Square_Gen.DIR_NORTH)
    elif event.type == pygame.KEYUP and event.key == pygame.K_d:
        mb.player.move(Square_Gen.DIR_EAST)
    elif event.type == pygame.KEYUP and event.key == pygame.K_s:
        mb.player.move(Square_Gen.DIR_SOUTH)
    elif event.type == pygame.KEYUP and event.key == pygame.K_a:
        mb.player.move(Square_Gen.DIR_WEST)
    elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
        mb.fireBullet()
        mb.player.lastmove = 0
    elif event.type == pygame.KEYUP and event.key == pygame.K_n:
        mb.player.lastmove = 0
        pass
    else:
        isTurnTaken = False

def logicGameRunning():
    global isTurnTaken
    global gameState
    if not isTurnTaken:
        return None
    if len(mb.bullets) != 0:
        mb.moveBullets()
    if not mb.player.stillAlive():
        gameState = STATE_GAMEOVER
        logicGameOver()
    if not mb.boss.stillAlive():
        gameState = STATE_GAMEOVER
        logicGameOver()
        return None
    mb.PlayerLogic()
    mb.BossLogic()
    
def inputGameOver(event):
    # Null, High score screen (arcade ver) or Wait for input
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def logicGameOver():
    #ai_dump("null")
    #reset player
    #reset boss
    mb.killSquares = []
 #   gameState = STATE_RUNNING

while 1:
    Square_Gen.frozenEntites = False
    for event in pygame.event.get():
        isTurnTaken = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if gameState == STATE_RUNNING:
            inputGameRunning(event)
            logicGameRunning()
        elif gameState == STATE_GAMEOVER:
            inputGameOver(event)
            logicGameOver()
            #s.drawGameOverText(whoDied)
        elif gameState == STATE_MENU:
            pass
    s.drawScreen(gameState)

