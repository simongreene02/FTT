import pygame, Square_Gen, Draw, sys
pygame.init()

width = 10
height = 10

STATE_RUNNING = 1
STATE_MENU = 2
STATE_GAMEOVER = 3

mb = Square_Gen.Board(width, height)

s = Draw.ScreenMaker(mb)

gameState = STATE_RUNNING

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
    else:
        isTurnTaken = False

def logicGameRunning():
    global isTurnTaken
    global gameState
    if not isTurnTaken:
        return None
    mb.PlayerLogic()
    if len(mb.bullets) != 0:
        mb.moveBullets()
    if not mb.player.stillAlive():
        gameState = STATE_GAMEOVER
        logicGameOver()
        return None
    #bossAI()

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

