import pyxel

class Enemy:
    ''' 敵キャラクター '''

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.setspeed(True)
        return

    def setspeed(self,init):
        ''' init=Trueで初期化 '''
        if init:
            self.speed = 50
        else:
            # 呼び出しのたびに速さアップ
            self.speed = max( 30, self.speed - 2)
        return
        
    def moverandom(self,x,y,size):
        ''' 指定位置から離れた場所に配置 '''
        while True:
            self.x = pyxel.rndi(1,size)
            self.y = pyxel.rndi(1,size)
            if self.chkenemy(x,y,limit=200) == False :
                break
            
        self.setspeed(False)
        return

    def chkenemy(self,x,y,limit=13):
        ''' 距離判定 '''
        ret = False
        dx = self.x - x
        dy = self.y - y
        dis = pyxel.sqrt(dx**2+dy**2)
        if dis <= limit :
            ret = True
        return ret
    
    def update(self,px,py):
        self.x = self.x + (px - self.x) / self.speed
        self.y = self.y + (py - self.y) / self.speed
        
        return
    
    def draw(self):

        pyxel.blt(self.x,self.y, 0, 16,112, self.w,self.h,2)
        return


# テストコード
if __name__ == '__main__':
    pyxel.init(128, 128)
    pyxel.load("alice.pyxres")
    en = Enemy(10,10)

    def update():
        en.update(90,90)

    def draw():
        pyxel.cls(1)
        pyxel.text(1,1,"Enemy Test",7)
        en.draw()

    pyxel.run(update,draw)
