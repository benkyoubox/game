import pyxel
from common import *
import sprites as spr

ANI_TYPE_FRONT = 0
ANI_TYPE_LR = 1
ANI_TYPE_4WAY = 2

enemydata = {
    'bat':[[0,152,16,8,3],[16,152,16,8,3]],
    'snake':[[[48,152,-16,8,2]],
            [[48,152,16,8,2]]],
    'rat':[[[34,153,5,7,3]],
           [[34,153,5,-7,3]],
           [[41,155,-5,4,3]],
           [[41,155,5,4,3]]  ],
    'slimeG':[[[18,99,12,10,2]],
            [[2,99,12,10,2]],
            [[34,99,12,10,2]],
            [[50,99,12,10,2]]],
    'slimeY':[[[82,99,12,10,2]],
            [[66,99,12,10,2]],
            [[98,99,12,10,2]],
            [[114,99,12,10,2]]],
    'wolf':[[[16,136,16,16,3],[16,136,-16,16,3]],
            [[0,136,16,16,3],[0,136,-16,16,3]],
            [[33,136,14,16,3],[49,136,14,16,3]],
            [[33,136,-14,16,3],[49,136,-14,16,3]]],
    'mage':[[0,160,16,16,2],[16,160,16,16,2]],
    'golem':[[[24,112,24,24,2],[24,112,-24,24,2]],
        [[0,112,24,24,2],[0,112,-24,24,2]],
        [[48,112,24,24,2],[72,112,24,24,2]],
        [[48,112,-24,24,2],[72,112,-24,24,2]],]
}




class Enemy(spr.Sprite):

    def __init__(self, x, y, key, tm, life, type=ANI_TYPE_4WAY, speed=1, ani=4):
        self.key = key
        self.anitype = type
        self.anirate = ani
        self.dir = pyxel.rndi(0,3)
        self.speed = 2
        self.sensor = 16 * 5
        self.life = life
        self.cnt = 0
        self.tm = tm

        self.x = x
        self.y = y
        u,v,w,h,col = self.getdata()
        self.u, self.v, self.w, self.h, self.col = u,v,abs(w),abs(h),col
        self.is_alive = True
        return

    def getdata(self):
        u,v,w,h,col = 0,0,8,8,0
        if self.anitype == ANI_TYPE_FRONT:
            data = enemydata.get(self.key)
            u,v,w,h,col = data[ self.cnt // self.anirate % len(data) ]
        elif self.anitype == ANI_TYPE_LR :
            data = enemydata.get(self.key)[self.dir%2]
            u,v,w,h,col = data[ self.cnt // self.anirate % len(data) ]
        elif self.anitype == ANI_TYPE_4WAY:
            data = enemydata.get(self.key)[self.dir]
            u,v,w,h,col = data[ self.cnt // self.anirate % len(data) ]
        return u,v,w,h,col

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

    def getdir(self,x,y):
        dir = DIR_DOWN
        deg = pyxel.atan2(y,x)
        if -135 <= deg < -45 :
            dir = DIR_UP
        elif -45 <= deg < 45 :
            dir = DIR_RIGHT
        elif 45 <= deg < 135 :
            dir = DIR_DOWN
        else:
            dir = DIR_LEFT
        return dir

    def ai(self,x,y):
        dx = dy = 0
        return dx,dy

    def update(self,px,py):
        self.cnt += 1
        dx,dy = self.ai(px,py)
        return super().update(dx, dy)

    def draw(self):
        u,v,w,h,col = self.getdata()
        pyxel.blt(self.x,self.y, 0, u, v, w, h, col)
        return

class EnemyWondering(Enemy):
    
    def ai(self,px,py):
        dx = dy = 0

        if self.cnt % 4 != 0 :
            return dx,dy

        # ルールベースAI

        # 範囲内にプレイヤーがいれば近づく
        u,v,w,h,col = self.getdata()
        dist = self.sensor
        x = self.x + abs(w)//2
        y = self.y + abs(h)//2
        if self.dir == DIR_UP :
            cx = x - dist // 2
            cy = y - dist
        elif self.dir == DIR_DOWN:
            cx = x - dist // 2
            cy = y
        elif self.dir == DIR_LEFT:
            cx = x - dist
            cy = y - dist // 2
        elif self.dir == DIR_RIGHT:
            cx = x
            cy = y - dist // 2

        speed = self.speed + pyxel.rndi(0,2)
        if cx <= px <= cx + dist and cy <= py <= cy + dist:
            self.dir = self.getdir(px-x,py-y)
            if self.dir == DIR_UP :
                dy = -speed                
            elif self.dir == DIR_DOWN :
                dy = speed
            elif self.dir == DIR_LEFT:
                dx = -speed
            elif self.dir == DIR_RIGHT :
                dx = speed

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
        chk = 0
        if self.chkwall(dx,0) :
            dx = 0
            chk += 1
        if self.chkwall(0,dy) :
            dy = 0
            chk += 1
        if 1 < chk:
            self.dir = pyxel.rndi(0,3)

        return dx,dy

