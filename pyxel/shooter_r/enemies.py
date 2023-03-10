import pyxel

TYPE_BULLET = 0
TYPE_NORMAL = 1
TYPE_BOSS = 2

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_ANIMA =[ (0,48),(8,48),(16,48) ]
ENEMY_A_ANIMA =[ (40,40),(48,40),(56,40),(64,40) ]
BOSS_PARTS = [(16,80,16,8),(16,80,16,-8),(112,40,8,8)]

enemies = []


class Enemy:
    """ 敵機 """

    def __init__(self, x, y, dx, dy):
        self.type = TYPE_NORMAL
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.tmr = 0
        self.is_alive = True
        self.life = 1
        enemies.append(self)

    def update(self):
        self.tmr += 1
        self.move()
        if (self.x < -20 or pyxel.width + 20 < self.x
            or self.y < -20 or pyxel.height + 20 < self.y):
            self.is_alive = False

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        u,v = ENEMY_ANIMA[(self.tmr//4)%3]
        pyxel.blt(self.x, self.y, 0, u, v, self.w, self.h, 0)


class EnemyA(Enemy):
    """ 敵機 上下に移動 """

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if( (self.y < 10 and self.dy < 0)
          or (150 < self.y and 0 < self.dy)):
            self.dy = -self.dy

    def draw(self):
        u,v = ENEMY_A_ANIMA[(self.tmr//10)%4]
        pyxel.blt(self.x, self.y, 0, u, v, self.w, self.h, 0)


class EnemyB(Enemy):
    """ 敵機 弾を撃つ """

    def update(self):
        super().update()
        if pyxel.rndi(0,100) < 3 and 10 < self.tmr:
            EnemyBullet(self.x,self.y+2,-3,pyxel.rndi(-1,1))
            self.tmr = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 88,40, self.w, self.h, 0)


class EnemyBullet(Enemy):
    """ 敵機の撃つ弾 """

    def __init__(self, x, y, dx, dy):
        super().__init__(x,y,dx,dy)
        self.type = TYPE_BULLET
        self.w = 4
        self.h = 4
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 50,34, self.w, self.h, 0)


class Boss(Enemy):
    """ ボス """

    def __init__(self, x, y, lif):
        super().__init__(x,y,-2,1.2)
        self.type = TYPE_BOSS
        self.life = lif
        self.parts = [BossParts(x-6,y-8,99,0),
                      BossParts(x-6,y+8,99,1),
                      BossParts(x-6,y,2,2)]
        self.stime = 0

    def move(self):
        sec = self.tmr // 30
        if sec < 3:
            self.x += self.dx
            self.x = max(self.x, pyxel.width - 40)
        else:
            self.y += self.dy
            if( (self.y < 10 and self.dy < 0)
              or (142 < self.y and 0 < self.dy)):
                self.dy = -self.dy
        self.parts[0].x = self.x-6
        self.parts[0].y = self.y-8
        self.parts[1].x = self.x-6
        self.parts[1].y = self.y+8
        self.parts[2].x = self.x-6
        self.parts[2].y = self.y       

    def update(self):
        self.tmr += 1
        self.move()
        if pyxel.rndi(0,100) < 3 and 20 < self.tmr - self.stime:
            EnemyBullet(self.x,self.y+2,-3,-1)
            EnemyBullet(self.x,self.y+2,-3,0)
            EnemyBullet(self.x,self.y+2,-3,1)
            self.stime = self.tmr
            
    def draw(self):
        if self.life < 3:
            u,v = (8,32)
        elif self.life < 8:
            u,v = (24,32)
        elif self.life < 12:
            u,v = (32,32)
        else:
            u,v = (24,72)            
        pyxel.blt(self.x, self.y, 0, u,v, self.w, self.h, 0)

    def destroy(self):
        self.parts[0].is_alive = False
        self.parts[1].is_alive = False
        self.parts[2].is_alive = False

    def __del__(self):
        self.parts.clear()


class BossParts(Enemy):
    """ ボス周辺部分 """

    def __init__(self, x, y, lif, idx):
        super().__init__(x,y,0,0)
        self.w = abs(BOSS_PARTS[idx][2])
        self.h = abs(BOSS_PARTS[idx][3])
        self.life = lif
        self.idx = idx

    def draw(self):
        u,v,w,h = BOSS_PARTS[self.idx]
        pyxel.blt(self.x, self.y, 0, u,v, w,h, 0)
