DIR_NORTH = 1
DIR_EAST = 2
DIR_SOUTH = 3
DIR_WEST = 4

#def FileError(error):
#    raise Exception("fileError", error)

#def SizeError(error):
#    raise Exception("sizeError", error)


player_dead = False

class Entity:
    def __init__(self, image, x, y, dire, board, HP):
        self.image = image
        self.x = x
        self.y = y
        self.dire = dire
        self.board = board
        self.HP = HP
        self.lastmove = -1

    def squareInFront(self):
        if self.dire == DIR_NORTH:
            sif = [self.x, self.y - 1]
        elif self.dire == DIR_EAST:
            sif = [self.x + 1, self.y]
        elif self.dire == DIR_SOUTH:
            sif = [self.x, self.y + 1]
        else:
            sif = [self.x - 1, self.y]


        if not (sif[0] > self.board.width - 1 or sif[0] < 0 or sif[1] > self.board.height - 1 or sif[1] < 0):
            return sif



    def move(self, direction):
        if direction == DIR_NORTH:
            self.face_north()
            self.move_north()
        if direction == DIR_EAST:
            self.face_east()
            self.move_east()
        if direction == DIR_SOUTH:
            self.face_south()
            self.move_south()
        if direction == DIR_WEST:
            self.face_west()
            self.move_west()
        self.lastmove = direction
    def move_north(self):
        if self.y > 0 and not frozenEntites:
            self.y -= 1

    def move_east(self):
        if self.x < self.board.width - 1 and not frozenEntites:
            self.x += 1

    def move_south(self):
        if self.y < self.board.height - 1 and not frozenEntites:
            self.y += 1

    def move_west(self):
        if self.x > 0 and not frozenEntites:
            self.x -= 1

    def face_north(self):
        if not frozenEntites:
            self.dire = DIR_NORTH
    def face_east(self):
        if not frozenEntites:
            self.dire = DIR_EAST
    def face_south(self):
        if not frozenEntites:
            self.dire = DIR_SOUTH
    def face_west(self):
        if not frozenEntites:
            self.dire = DIR_WEST

    def stillAlive(self):
        if self.HP <= 0:
            return False
        else:
            return True



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.killSquares = [[9, 9]]
        self.player = Entity('player', 0, 0, DIR_NORTH, self, 1)
        self.bullets = []
        self.boss = Entity('boss', width - 1, height - 1, DIR_WEST, self, 1)

    def PlayerLogic(self):
        if [self.player.x, self.player.y] in self.killSquares:
            self.player.HP = 0

    def BossLogic(self):
        if self.player.lastmove == DIR_NORTH:
            self.boss.move(DIR_SOUTH)
        elif self.player.lastmove == DIR_SOUTH:
            self.boss.move(DIR_NORTH)
        elif self.player.lastmove == DIR_EAST:
            self.boss.move(DIR_WEST)
        elif self.player.lastmove == DIR_WEST:
            self.boss.move(DIR_EAST)
        
        if [self.boss.x,self.boss.y] not in self.killSquares:
            self.killSquares.append([self.boss.x,self.boss.y])
        
    def fireBullet(self):
        if not self.player.squareInFront() == None:
            self.bullets.append(Entity('bullet', self.player.x, self.player.y, self.player.dire, self, 1))

    def moveBullets(self):
        deleteFlag = []
        for index, bullet in enumerate(self.bullets):
            sqrInFront = bullet.squareInFront()
            if sqrInFront == None:
                deleteFlag.append(index)
            elif sqrInFront == [self.boss.x, self.boss.y]:
                deleteFlag.append(index)
                self.boss.HP -= 1
            elif sqrInFront == [self.player.x, self.player.y]:
                deleteFlag.append(index)
            else: bullet.move(bullet.dire)
        deleteFlagSorted = sorted(deleteFlag, reverse=True)
        for index in deleteFlagSorted:
            del self.bullets[index]
