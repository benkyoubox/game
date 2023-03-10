import pyxel

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

MOT_WAIT = 0
MOT_WALK = 1
MOT_GOAL = 2
MOT_ATTACK = 3

ANIMA_WALK = [
    [(0,0),(16,0),(0,0),(32,0)],
    [(0,16),(16,16),(0,16),(32,16)],
    [(0,32),(16,32),(0,32),(32,32)],
    [(0,48),(16,48),(0,48),(32,48)],
    ]
SPEED = 3

ANIMA_GOAL = [(0,80),(0,16)]

ANIMA_ATTACK = [
    [(48,0),(0,0)],
    [(48,16),(0,16)],
    [(48,32),(0,32)],
    [(48,48),(0,48)],
    ]

TILE_WALL = (1,0)
chkpoint = [(0,5),(7,5),(15,5),
            (0,7),      (15,7),
            (0,15),(7,15),(15,15)]
def chkwall(cx,cy):
    c = 0
    for cpx,cpy in chkpoint:
        xi = (cx + cpx)//8
        yi = (cy + cpy)//8
        if TILE_WALL == pyxel.tilemap(0).pget(xi,yi):
            c += 1
    return c


class Player:
    ''' プレイヤーキャラクター '''

    def __init__(self,x,y):
        self.setpos(x,y)
        self.w = 16
        self.h = 16
        return

    def setpos(self,x,y):
        ''' スタート位置設定 '''
        self.x = x
        self.y = y        
        self.dir = DIR_DOWN
        self.flmcnt = 0
        self.motion = MOT_WAIT
        
    def setwalk(self,dir):
        self.dir = dir
        self.flmcnt += 1
        self.motion = MOT_WALK
        
    def move(self):
        ''' 座標移動 '''
        dx = dy = 0
        
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.setwalk(DIR_UP)
            dy = -SPEED
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.setwalk(DIR_DOWN)
            dy = SPEED
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.setwalk(DIR_LEFT)
            dx = -SPEED
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.setwalk(DIR_RIGHT)
            dx = SPEED
            
        if pyxel.btnp(pyxel.KEY_A):
            dx = dy = 0
            self.motion = MOT_ATTACK
            self.flmcnt = 0

        # キャラクターの移動
        lr = pyxel.sgn(dx)
        loop = abs(dx)
        while 0 < loop:
            if 0 != chkwall(self.x+lr,self.y):
                dx = 0
                break
            self.x += lr
            loop -= 1

        ud = pyxel.sgn(dy)
        loop = abs(dy)
        while 0 < loop:
            if 0 != chkwall(self.x,self.y+ud):
                dy = 0
                break
            self.y += ud
            loop -= 1

        return

    def goal(self):
        ''' ゴール到達 '''
        self.motion = MOT_GOAL
        self.flmcnt = 0
        return
    
    def update(self):
        if MOT_WAIT == self.motion or MOT_WALK ==  self.motion:
            self.move()
        elif MOT_GOAL == self.motion:
            self.flmcnt += 1
        elif MOT_ATTACK == self.motion:
            self.flmcnt += 1
            if 19 < self.flmcnt:
                self.motion = MOT_WALK
                self.flmcnt = 0
        
        return

    def getImg(self):
        u,v = (0,0)
        if MOT_WAIT == self.motion :
            u,v = (0,16)
        elif MOT_WALK ==  self.motion :
            u,v = ANIMA_WALK[self.dir][self.flmcnt//6 % 4]
        elif MOT_GOAL == self.motion:
            u,v = ANIMA_GOAL[self.flmcnt//8 % 2]
        elif MOT_ATTACK == self.motion:
            u,v = ANIMA_ATTACK[self.dir][self.flmcnt//10 % 2]

        return u,v

    def test_attack(self,u,v):
        if 0 < self.flmcnt < 10:
            x = self.x
            y = self.y
            
            if DIR_UP == self.dir:
                x -= 2
                y -= 14
            elif DIR_DOWN == self.dir:
                x += 2
                y += 13
            elif DIR_LEFT == self.dir:
                x -= 13
            elif DIR_RIGHT == self.dir:
                x += 13
            
            pyxel.blt(x,y, 0, u+self.w,v, 16,16,2)
        return
    
    def draw(self):
        u,v = self.getImg()
        if MOT_GOAL == self.motion:
            y = self.y - 1 + self.flmcnt//8 % 2
            pyxel.blt(self.x,y, 0, u,v, self.w,self.h,2)
        else:
            pyxel.blt(self.x,self.y, 0, u,v, self.w,self.h,2)

        if MOT_ATTACK == self.motion:
            self.test_attack(u,v)

        return

# テストコード
if __name__ == '__main__':
    pyxel.init(128, 128)
    pyxel.load("alice.pyxres")
    pl = Player(10,10)

    def update():
        if pyxel.btnp(pyxel.KEY_G):
            if MOT_GOAL != pl.motion :
                pl.goal()
            else:
                pl.setpos(pl.x,pl.y)
        
        pl.update()

    def draw():
        pyxel.cls(1)
        pyxel.text(1,1,"Player Test",7)
        pl.draw()

    pyxel.run(update,draw)
