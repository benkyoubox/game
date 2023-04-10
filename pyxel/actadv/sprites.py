import pyxel
from stages import TM


DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

MOT_WAIT = 0
MOT_WALK = 1
MOT_ATTACK = 2

images = {'player':[0,16,16,16,3],
        'soldierA':[0,64,16,16,2],
        'soldierB':[0,80,16,16,2],
        'enm1':[0,96,16,16,2],
        'enm2':[16,96,16,16,2]
        }

TILE_WALL_X = [1,3,5]

class Sprite:

    def __init__(self,x,y,key):
        self.x = x
        self.y = y
        self.u, self.v, self.w, self.h, self.col = images.get(key,[0,0,8,8,0])
        self.is_alive = True

    def isArea(self,x,y,w,h):
        if x <= self.x < x+w and y <= self.y < y+h :
            return True
        else:
            return False
        
    def update(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def draw(self):
        pyxel.blt(self.x,self.y, 0, self.u,self.v, self.w, self.h, self.col)
        return

ANIMA_WALK = [
    [(0,0),(16,0),(0,0),(32,0)],
    [(0,16),(16,16),(0,16),(32,16)],
    [(0,32),(16,32),(0,32),(32,32)],
    [(0,48),(16,48),(0,48),(32,48)]
    ]

ANIMA_ATTACK = [
    [(48,0),(0,0)],
    [(48,16),(0,16)],
    [(48,32),(0,32)],
    [(48,48),(0,48)]
    ]

WP_SWORD = 0
WEAPONS = [[(0,-14,64,0,16,16,3),
            (-1,13,64,16,16,16,3),
            (-13,0,64,32,16,16,3),
            (13,0,64,48,16,16,3)]]

class Player(Sprite):

    def __init__(self, x, y, key):
        super().__init__(x, y, key) 
        self.life = 10
        self.dir = DIR_DOWN
        self.speed = 3
        self.flmcnt = 0
        self.motion = MOT_WAIT
        self.weapon = WP_SWORD
        self.chkpoint = [(2,5),(7,5),(13,5),
                         (2,7),      (13,7),
                         (2,15),(7,15),(13,15)]
        return

    def chkwall(self,cx,cy):
        for cpx,cpy in self.chkpoint:
            xi = (cx + cpx)//8
            yi = (cy + cpy)//8
            if pyxel.tilemap(TM).pget(xi,yi)[0] in TILE_WALL_X:
                return True
        return False

    def setwalk(self,dir):
        self.dir = dir
        self.flmcnt += 1
        self.motion = MOT_WALK
        return

    def move(self,dx,dy):
        lr = pyxel.sgn(dx)
        loop = abs(dx)
        while 0 < loop:
            if self.chkwall(self.x+lr,self.y):
                dx = 0
                break
            self.x += lr
            loop -= 1

        ud = pyxel.sgn(dy)
        loop = abs(dy)
        while 0 < loop:
            if self.chkwall(self.x,self.y+ud):
                dy = 0
                break
            self.y += ud
            loop -= 1
        return

    def attack(self):
        self.motion = MOT_ATTACK
        self.flmcnt = 0
        return

    def update(self, dx, dy):
        if MOT_WAIT == self.motion or MOT_WALK ==  self.motion:
            self.move(dx,dy)
        if MOT_ATTACK == self.motion:
            self.flmcnt += 1
            if 10 < self.flmcnt :
                self.motion = MOT_WALK
                self.flmcnt = 0
        return

    def draw(self):
        if MOT_WAIT == self.motion :
            self.u, self.v = (0,16)
        elif MOT_WALK ==  self.motion :
            self.u, self.v = ANIMA_WALK[self.dir][self.flmcnt//6 % 4]
        
        if MOT_ATTACK == self.motion :
            self.u, self.v = ANIMA_ATTACK[self.dir][self.flmcnt//10 % 2]
            xp, yp, u, v, w, h, col = WEAPONS[self.weapon][self.dir]
            if DIR_UP == self.dir :
                pyxel.blt(self.x + xp, self.y + yp, 0, u, v, w, h, col)
                super().draw()
            else:
                super().draw()
                pyxel.blt(self.x + xp, self.y + yp, 0, u, v, w, h, col)
        else:
            super().draw()
        return 



class Bullet(Sprite):

    def __init__(self, x, y, kind, dir):
        self.dir = dir
        self.x = x
        self.y = y
        self.w = 2
        self.h = 2
        self.dx = 0
        self.dy = 0
        self.dist = 0
        self.kind = kind
        self.cnt = 30
        self.is_alive = True
        if WP_SWORD == kind :
            speed = 3
            self.cnt = 6
            if DIR_UP == dir :
                self.y -= 2
                self.w = 16
                self.dy = -speed
            elif DIR_DOWN == dir :
                self.y += 18
                self.w = 16
                self.dy = speed
            elif DIR_LEFT == dir :
                self.x -= 2
                self.h = 16
                self.dx = -speed
            elif DIR_RIGHT == dir :
                self.x += 18
                self.h = 16
                self.dx = speed
        return

    def update(self):
        self.cnt -= 1
        if self.cnt < 0:
            self.is_alive = False
        self.x += self.dx
        self.y += self.dy
        return

    def draw(self):
        # DEBUG
        if WP_SWORD == self.kind :
            pyxel.rect(self.x, self.y, self.w, self.h, 10)
        return


class Enemy(Sprite):

    def __init__(self, x, y, key):
        self.life = 1
        self.cnt = 0
        super().__init__(x, y, key)

    def update(self):
        dx = dy = 0
        self.cnt += 1
        if self.cnt % 10 and pyxel.rndi(1,100) < 10:
            dx = pyxel.rndi(-2,2)
            dy = pyxel.rndi(-2,2)
        return super().update(dx, dy)
    