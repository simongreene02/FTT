import random

DIR_NORTH = 1
DIR_EAST = 2
DIR_SOUTH = 3
DIR_WEST = 4

ai = None

#def FileError(error):
#    raise Exception("fileError", error)

#def SizeError(error):
#    raise Exception("sizeError", error)


player_dead = False

class Entity:
    def __init__(self, image, x, y, dire, board, HP, weight):
        self.image = image
        self.x = x
        self.y = y
        self.dire = dire
        self.board = board
        self.HP = HP
        self.lastmove = -1
        self.weight = weight

    def squareInFront(self, dire, squares = 1):
        if dire == DIR_NORTH:
            sif = [self.x, self.y - squares]
        elif dire == DIR_EAST:
            sif = [self.x + squares, self.y]
        elif dire == DIR_SOUTH:
            sif = [self.x, self.y + squares]
        else:
            sif = [self.x - squares, self.y]


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
        if self == self.board.boss:
            if self.squareInFront(self.dire, 1) == [self.board.player.x, self.board.player.y]:
                self.board.PlayerLogic()
    def move_north(self):
        if self.y > 0 and not frozenEntites:
            sif = self.squareInFront(self.dire)
            for entity in [self.board.player, self.board.boss] + self.board.bullets:
                if sif == [entity.x, entity.y]:
                    if entity.weight < 0:
                        entity.HP = 0
                        self.y -= 1
                        return None
                    if entity.weight < self.weight:
                        sif2 = self.squareInFront(self.dire, 2)
                        if sif2 == None:
                            entity.HP = 0
                            self.y -= 1
                            return None
                        else:
                            entity.x = sif2[0]
                            entity.y = sif2[1]
                            self.y -= 1
                            return None
                    return None
            self.y -= 1
            return None

    def move_east(self):
        if self.x < self.board.width - 1 and not frozenEntites:
            sif = self.squareInFront(self.dire)
            for entity in [self.board.player, self.board.boss] + self.board.bullets:
                if sif == [entity.x, entity.y]:
                    if entity.weight < 0:
                        entity.HP = 0
                        self.x += 1
                        return None
                    if entity.weight < self.weight:
                        sif2 = self.squareInFront(self.dire, 2)
                        if sif2 == None:
                            entity.HP = 0
                            self.x += 1
                            return None
                        else:
                            entity.x = sif2[0]
                            entity.y = sif2[1]
                            self.x += 1
                            return None
                    return None
            self.x += 1
            return None

    def move_south(self):
        if self.y < self.board.height - 1 and not frozenEntites:
            sif = self.squareInFront(self.dire)
            for entity in [self.board.player, self.board.boss] + self.board.bullets:
                if sif == [entity.x, entity.y]:
                    if entity.weight < 0:
                        entity.HP = 0
                        self.y += 1
                        return None
                    if entity.weight < self.weight:
                        sif2 = self.squareInFront(self.dire, 2)
                        if sif2 == None:
                            entity.HP = 0
                            self.y += 1
                            return None
                        else:
                            entity.x = sif2[0]
                            entity.y = sif2[1]
                            self.y += 1
                            return None
                    return None
            self.y += 1
            return None

    def move_west(self):
        if self.x > 0 and not frozenEntites:
            sif = self.squareInFront(self.dire)
            for entity in [self.board.player, self.board.boss] + self.board.bullets:
                if sif == [entity.x, entity.y]:
                    if entity.weight < 0:
                        entity.HP = 0
                        self.x -= 1
                        return None
                    if entity.weight < self.weight:
                        sif2 = self.squareInFront(self.dire, 2)
                        if sif2 == None:
                            entity.HP = 0
                            self.x -= 1
                            return None
                        else:
                            entity.x = sif2[0]
                            entity.y = sif2[1]
                            self.x -= 1
                            return None
                    return None
            self.x -= 1
            return None

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
        self.player = Entity('player', 0, 0, DIR_NORTH, self, 1, 1)
        self.bullets = []
        self.boss = Entity('boss', width - 1, height - 1, DIR_WEST, self, 1, 10)

    def PlayerLogic(self):
        if [self.player.x, self.player.y] in self.killSquares:
            self.player.HP = 0

    def BossLogic(self):
        """ai = random.choice([2])
        if ai == 1:
            if self.player.lastmove == DIR_NORTH:
                self.boss.move(DIR_SOUTH)
            elif self.player.lastmove == DIR_SOUTH:
                self.boss.move(DIR_NORTH)
            elif self.player.lastmove == DIR_EAST:
                self.boss.move(DIR_WEST)
            elif self.player.lastmove == DIR_WEST:
                self.boss.move(DIR_EAST)
        if ai == 0:
            safeList = []
            if self.boss.y > 0:
                safeList.append(DIR_NORTH)
            if self.boss.x > 0:
                safeList.append(DIR_WEST)
            if self.boss.y < self.height - 1:
                safeList.append(DIR_SOUTH)
            if self.boss.x < self.width - 1:
                safeList.append(DIR_EAST)

            self.boss.move(random.choice(safeList))"""

        global ai

        if ai is None:
            ai = random.choice([ChargeAI])
            ai = ai(self.boss, self.player, self)

        ai.RunAI()
        
        if [self.boss.x,self.boss.y] not in self.killSquares:
            self.killSquares.append([self.boss.x,self.boss.y])

        #if len(self.killSquares) > 10:
           #del self.killSquares[0]
        
    def fireBullet(self):
        if not self.player.squareInFront(self.dire) == None:
            self.bullets.append(Entity('bullet', self.player.x, self.player.y, self.player.dire, self, 1, -1))

    def moveBullets(self):
        deleteFlag = []
        for index, bullet in enumerate(self.bullets):
            sqrInFront = bullet.squareInFront(self.dire)
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


class ChargeAI:
    def __init__(self, boss, player, board):
        self.boss = boss
        self.player = player
        self.board = board
        self.dodgingSqrs = 0

    def RunAI(self):
        if random.randint(1, 5) == 1:
            dodgingSqrs = random.randint(3, 5)
            print dodgingSqrs
        if self.boss.x == self.player.x or self.boss.y == self.player.y:
            if self.boss.x < self.player.x:
                self.boss.move(DIR_EAST)
                return None

            if self.boss.x > self.player.x:
                self.boss.move(DIR_WEST)
                return None

            if self.boss.y < self.player.y:
                self.boss.move(DIR_SOUTH)
                return None

            if self.boss.y > self.player.y:
                self.boss.move(DIR_NORTH)
                return None

