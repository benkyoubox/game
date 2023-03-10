import pyxel

# 迷路作成用定義
TM = 0
IMG_NO = 1
TILE_BLANK = (0,0)
TILE_WALL = (1,0)
UNIT = 6 # 迷路1区画のサイズ

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

def isblank(xi,yi,ck):
    ret = False
    if DIR_UP == ck:
        yi-=1
    elif DIR_DOWN == ck:
        yi+=1
    elif DIR_LEFT == ck:
        xi-=1
    elif DIR_RIGHT == ck:
        xi+=1
        
    if TILE_BLANK == pyxel.tilemap(TM).pget(xi,yi):
        ret = True
        
    return ret

class Stage:
    ''' 迷路表示 '''

    def __init__(self):
        self.scroll_x = 0
        self.scroll_y = 0
        self.left_border = pyxel.width *0.33
        self.right_border = pyxel.width *0.66 -16
        self.upper_border = pyxel.height * 0.33
        self.bottom_border = pyxel.height * 0.66 -16
        self.sx = 8
        self.sy = 8
        self.gx = 40
        self.gy = 32
        pyxel.tilemap(TM).refimg = IMG_NO
        return
        
    def initmaze(self):
        for yi in range(self.size):
            for xi in range(self.size):
                pyxel.tilemap(TM).pset(xi,yi,TILE_BLANK)

        return

    def makemaze(self,size):
        ''' 迷路作成 引数:size 一辺のタイル数 '''

        size = min(size,252)    # タイルマップ最大256
        self.size = size
        self.width = (size+1)*8
        self.height = (size+1)*8

        self.initmaze()

        # 外周を壁にする
        for yi in range(size+1):
            pyxel.tilemap(TM).pset(0,yi,TILE_WALL)
            pyxel.tilemap(TM).pset(size,yi,TILE_WALL)
            for xi in range(size+1):
                if 0 != yi and size != yi:
                    continue
                pyxel.tilemap(TM).pset(xi,yi,TILE_WALL)    

        # 壁の生成
        r_min = DIR_UP
        for yi in range(UNIT,size,UNIT):
            if UNIT < yi:
                r_min = DIR_DOWN
            for xi in range(UNIT,size,UNIT):
                if pyxel.rndi(1,100) < 16:
                    continue
                while True:
                    wk = pyxel.rndi(r_min,DIR_RIGHT)
                    if isblank(xi,yi,wk) :
                        tmpx = xi
                        tmpy = yi
                        pyxel.tilemap(TM).pset(tmpx,tmpy,TILE_WALL)
                        for i in range(UNIT):
                            if DIR_UP == wk:
                                tmpy -= 1
                            elif DIR_DOWN == wk:
                                tmpy += 1
                            elif DIR_LEFT == wk:
                                tmpx -= 1
                            elif DIR_RIGHT == wk:
                                tmpx += 1
                            pyxel.tilemap(TM).pset(tmpx,tmpy,TILE_WALL)
                        break # while loop break

        self.setgoal()
        return

    def setgoal(self):
        ''' ゴール作成 '''
        while True:
            gxi = pyxel.rndi(1,self.size-1)
            gyi = pyxel.rndi(1,self.size-1)
            if (
                    TILE_BLANK == pyxel.tilemap(TM).pget(gxi,gyi)
                and TILE_BLANK == pyxel.tilemap(TM).pget(gxi+1,gyi)
                and TILE_BLANK == pyxel.tilemap(TM).pget(gxi,gyi+1)
                and TILE_BLANK == pyxel.tilemap(TM).pget(gxi+1,gyi+1)
                ):
                self.gx = gxi * 8
                self.gy = gyi * 8
                break;
        rs = 1
        re = self.size // 2
        if self.gx < self.width / 2 :
            rs = re
            re = self.size - 1

        while True:
            sxi = pyxel.rndi(rs,re)
            syi = pyxel.rndi(1,self.size-1)
            if (
                    TILE_BLANK == pyxel.tilemap(TM).pget(sxi,syi)
                and TILE_BLANK == pyxel.tilemap(TM).pget(sxi+1,syi)
                and TILE_BLANK == pyxel.tilemap(TM).pget(sxi,syi+1)
                and TILE_BLANK == pyxel.tilemap(TM).pget(sxi+1,syi+1)
                and self.chkgoal(sxi * 8,syi * 8,limit=200) == False
                ):
                self.sx = sxi * 8
                self.sy = syi * 8
                break;

    def chkgoal(self,x,y,limit=15):
        ''' ゴール到達判定 '''
        ret = False
        dx = self.gx - x
        dy = self.gy - y
        dis = pyxel.sqrt(dx**2+dy**2)
        if dis <= limit :
            ret = True
        return ret
        
    def update(self,x,y):
        ''' 画面のスクロール '''

        if x < self.scroll_x + self.left_border:
            self.scroll_x = x - self.left_border
            if self.scroll_x < 0:
                self.scroll_x = 0
        if self.scroll_x + self.right_border < x:
            self.scroll_x = x - self.right_border
            if self.width - pyxel.width < self.scroll_x:
                self.scroll_x = self.width - pyxel.width
            
        if y < self.scroll_y + self.upper_border:
            self.scroll_y = y - self.upper_border
            if self.scroll_y < 0:
                self.scroll_y = 0
        if self.scroll_y + self.bottom_border < y:
            self.scroll_y = y - self.bottom_border
            if self.height - pyxel.height < self.scroll_y:
                self.scroll_y = self.height - pyxel.height
        return
    
    def draw(self):
        pyxel.cls(1)
        pyxel.camera()
        pyxel.bltm(0,0, TM, self.scroll_x,self.scroll_y, pyxel.width,pyxel.height, 0)
        pyxel.camera(self.scroll_x,self.scroll_y)

        # ゴール表示
        pyxel.blt(self.gx,self.gy, 0, 0,112, 16,16, 0)
        
        return

# テストコード
if __name__ == '__main__':
    pyxel.init(512, 512)
    pyxel.load("alice.pyxres")
    stg = Stage()
    size = 252
    stg.makemaze(size)
    x = y = 0
    def update():
        global x,y

        if pyxel.btnp(pyxel.KEY_SPACE):
            stg.makemaze(size)
            
        if pyxel.btn(pyxel.KEY_UP):
            y -= 80
        if pyxel.btn(pyxel.KEY_DOWN):
            y += 80
        if pyxel.btn(pyxel.KEY_LEFT):
            x -= 80
        if pyxel.btn(pyxel.KEY_RIGHT):
            x += 80
        stg.update(x,y)

    def draw():
        stg.draw()
        pyxel.rect(stg.sx,stg.sy,16,16,8)
        pyxel.text(1,1,"Stage Test",7)

    pyxel.run(update,draw)
    
