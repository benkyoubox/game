import pyxel
from common import *
import sprites as spr

ANI_TYPE_FRONT = 0
ANI_TYPE_LR = 1
ANI_TYPE_4WAY = 2

enemydata = {
    'bat':[[0,152,16,8,3],[16,152,16,8,3]],
    'rat':[[[34,153,5,7,3]],
           [[34,153,5,-7,3]],
           [[41,155,-5,4,3]],
           [[41,155,5,4,3]]  ],
    'slimeG':[[[18,99,12,10,2]],
            [[2,99,12,10,2]],
            [[34,99,12,10,2]],
            [[50,99,12,10,2]]]
}




class Enemy(spr.Sprite):

    def __init__(self, x, y, key, tm, type=ANI_TYPE_4WAY, speed=1):
        self.key = key
        self.anitype = type
        self.dir = pyxel.rndi(0,3)
        self.speed = 2
        self.life = 1
        self.cnt = 0
        self.tm = tm

        self.x = x
        self.y = y
        u,v,w,h,col = 0,0,8,8,0
        if self.anitype == ANI_TYPE_FRONT:
            data = enemydata.get(self.key)
            u,v,w,h,col = data[ self.cnt // 4 % len(data) ]
        elif self.anitype == ANI_TYPE_4WAY:
            data = enemydata.get(self.key)[self.dir]
            u,v,w,h,col = data[ self.cnt // 4 % len(data) ]
        self.u, self.v, self.w, self.h, self.col = u,v,abs(w),abs(h),col
        self.is_alive = True
        return

    def chkwall(self,dx,dy):
        wnum = self.w // 7 + 1
        hnum = self.h // 7 + 1
        for i in range(wnum):
            for j in range(hnum):
                cx = self.x + i*7
                cy = self.y + j*7
                xi = (cx + dx)//8
                yi = (cy + dy)//8
                if pyxel.tilemap(self.tm).pget(xi,yi)[0] in TILE_WALL_X:
                    return True
        return False

    def ai(self,x,y):
        dx = dy = 0
        return dx,dy

    def update(self,px,py):
        self.cnt += 1
        dx,dy = self.ai(px,py)
        return super().update(dx, dy)

    def draw(self):
        if self.anitype == ANI_TYPE_FRONT:
            data = enemydata.get(self.key)
            u,v,w,h,col = data[ self.cnt // 4 % len(data) ]
        elif self.anitype == ANI_TYPE_4WAY:
            data = enemydata.get(self.key)[self.dir]
            u,v,w,h,col = data[ self.cnt // 4 % len(data) ]

        pyxel.blt(self.x,self.y, 0, u, v, w, h, col)
        return

class EnemyWondering(Enemy):
    def ai(self,px,py):
        dx = dy = 0

        if self.cnt % 4 != 0 :
            return dx,dy

        # ルールベースAI

        # 範囲内にプレイヤーがいれば近づく
        dist = 16*3
        speed = self.speed + pyxel.rndi(0,2)
        if self.dir != DIR_DOWN and 2 < self.y - py < dist :
            dy = -speed
            self.dir = DIR_UP
        if self.dir != DIR_UP and 2 < py - self.y < dist :
            dy = speed
            self.dir = DIR_DOWN
        if self.dir != DIR_RIGHT and 2 < self.x - px < dist :
            dx = -speed
            self.dir = DIR_LEFT
        if self.dir != DIR_LEFT and 2 < px - self.x < dist :
            dx = speed
            self.dir = DIR_RIGHT

        # 前進
        if dx == 0 and dy == 0 and self.cnt % 8 == 0:
            r = pyxel.rndf(0,1.0)
            if 0 < r < 0.4:
                if self.dir == DIR_UP :
                    dy = -speed
                elif self.dir == DIR_DOWN :
                    dy = speed
                elif self.dir == DIR_LEFT :
                    dx = -speed
                elif self.dir == DIR_RIGHT :
                    dx = speed
            elif r < 0.6:
                # 一定の割合で方向転換
                self.dir = pyxel.rndi(0,3)

        if self.chkwall(dx,dy) :
            dx = dy = 0
            self.dir = pyxel.rndi(0,3)

        return dx,dy

