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
        #self.boss = Entity()

    def PlayerLogic(self):
        if [self.player.x, self.player.y] in self.killSquares:
            self.player.HP = 0

    def fireBullet(self):
        if not self.player.squareInFront() == None:
            self.bullets.append(Entity('bullet', self.player.x, self.player.y, self.player.dire, self, 1))

    def moveBullets(self):
        deleteFlag = []
        for index, bullet in enumerate(self.bullets):
            if bullet.squareInFront() == None:
                deleteFlag.append(index)
            bullet.move(bullet.dire)
        for index in deleteFlag:
            del self.bullets[index]
