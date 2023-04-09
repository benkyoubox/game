import pyxel
APP_WIDTH = 256
APP_HEIGHT = 224
pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
pyxel.load("actadv.pyxres")

images = {'soldierA':[0,64,16,16,2],
          'soldierB':[0,80,16,16,2]}


class Sprite:

    def __init__(self,x,y,key):
        self.x = x
        self.y = y
        self.u, self.v, self.w, self.h, self.col = images.get(key,[0,0,8,8,0])
        self.life = True

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


class Stage:

    def __init__(self,width,height) -> None:
        self.width = 256 * 8
        self.height = 256 * 8
        self.area_w = width
        self.area_h = height
        self.scroll_x = 0
        self.scroll_y = 0
        self.left_border = width *0.33
        self.right_border = width *0.66 -16
        self.upper_border = height * 0.33
        self.bottom_border = height * 0.66 -16
        self.tm = 0
        self.col = 0
        return
    
    def genmap(self,tm):
        self.tm = tm
        pyxel.tilemap(tm).refimg = 1 # imagebank
        scale = 0.06
        z = 256
        fieldtile_y = 1
        for y in range(self.width//8):
            for x in range(self.height//8):
                tileNo = pyxel.floor(abs(pyxel.noise(x*scale, y*scale, z*scale) * 12))
                pyxel.tilemap(tm).pset(x,y,(tileNo,fieldtile_y))
        
        tgt = 6
        clifftile = [(7,2),(7,3)]
        for y in range(self.width//8 - 2):
            for x in range(self.height//8):
                tile = pyxel.tilemap(tm).pget(x,y)
                if tgt <= tile[0] and fieldtile_y == tile[1] and  pyxel.tilemap(tm).pget(x,y+1)[0] < tgt:
                    pyxel.tilemap(tm).pset(x,y+1,clifftile[0])
                    pyxel.tilemap(tm).pset(x,y+2,clifftile[1])

        return

    def update(self,x,y):
        if x < self.scroll_x + self.left_border:
            self.scroll_x = x - self.left_border
            if self.scroll_x < 0:
                self.scroll_x = 0
        if self.scroll_x + self.right_border < x:
            self.scroll_x = x - self.right_border
            if self.width - self.area_w < self.scroll_x:
                self.scroll_x = self.width - self.area_w
            
        if y < self.scroll_y + self.upper_border:
            self.scroll_y = y - self.upper_border
            if self.scroll_y < 0:
                self.scroll_y = 0
        if self.scroll_y + self.bottom_border < y:
            self.scroll_y = y - self.bottom_border
            if self.height - self.area_h < self.scroll_y:
                self.scroll_y = self.height - self.area_h
        return
    
    def draw(self):
        pyxel.camera()
        pyxel.bltm(0,0, self.tm, self.scroll_x,self.scroll_y, self.area_w,self.area_h, self.col)
        pyxel.camera(self.scroll_x,self.scroll_y)
        return


x=y=0
player = Sprite(x,y,'soldierA')
stg = Stage(256,200)
stg.genmap(1)


def update():
    global x,y
    dx = dy = 0
    if pyxel.btn(pyxel.KEY_UP):
        dy -= 2
    if pyxel.btn(pyxel.KEY_DOWN):
        dy += 2
    if pyxel.btn(pyxel.KEY_LEFT):
        dx -= 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        dx += 2
    
    player.update(dx,dy)
    x += dx
    y += dy
    stg.update(x,y)
    return

def draw():
    pyxel.cls(0)
    stg.draw()
    player.draw()
    
    return

pyxel.run(update, draw)
