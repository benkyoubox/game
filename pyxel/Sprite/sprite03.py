import pyxel
pyxel.init(128, 128)
pyxel.load("mygame.pyxres")

images = {'bo-peep':[0,0,16,16,2],
          'sheep':[0,16,16,16,2]}

class Sprite:

    def __init__(self,x,y,key):
        self.x = x
        self.y = y
        self.u, self.v, self.w, self.h, self.col = images.get(key,[0,0,8,8,0])
        
    def update(self,dx,dy):
        self.x += dx
        if self.x + self.w <= 0 :
            self.x += pyxel.width + self.w
        elif pyxel.width <= self.x :
            self.x -= pyxel.width + self.w
        self.y += dy
        if self.y + self.h <= 0 :
            self.y += pyxel.height + self.h
        elif pyxel.height <= self.y :
            self.y -= pyxel.height + self.h        
        
    def draw(self):
        pyxel.blt(self.x,self.y, 0, self.u,self.v, self.w, self.h, self.col)
        return

lbp = Sprite(10, 8, 'bo-peep')
sheep = []
for i in range(10):
    x = pyxel.rndi(0,pyxel.width-16)
    y = pyxel.rndi(0,pyxel.height-16)
    sheep.append( Sprite(x,y, 'sheep') )

def update():
    # キー入力にあわせてxy方向の移動量を決める
    dx = dy = 0
    speed = 2
    if pyxel.btn(pyxel.KEY_UP) :
        dy -= speed
    if pyxel.btn(pyxel.KEY_DOWN) :
        dy += speed
    if pyxel.btn(pyxel.KEY_LEFT) :
        dx -= speed
    if pyxel.btn(pyxel.KEY_RIGHT) :
        dx += speed
    # キャラクターの移動
    lbp.update(dx,dy)
    
    for obj in sheep:
        obj.update(-1,0)
    return

def draw():
    pyxel.cls(11)
    lbp.draw()
    for obj in sheep:
        obj.draw()
    
    return

pyxel.run(update, draw)
