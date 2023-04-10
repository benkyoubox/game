import pyxel

stagetiles = {'grassy':[[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,3)],[(1,1),(1,2)]],
              'rocky': [[(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,3)],[(3,1),(3,2)]],
              'ice':   [[(4,0),(4,1),(4,2),(4,3)],[(5,0),(5,3)],[(5,1),(5,2)]]}

class Stage:

    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
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
    
    def genmap(self,width,height,scale,z,key):
        ''' w,h pixelsize  scale=0.05-0.07 z=1- '''
        self.width = width
        self.height = height
        self.tm = 7
        tm = self.tm
        pyxel.tilemap(tm).refimg = 1 # imagebank
        span = 12
        border = 6
        fieldtile_low = stagetiles[key][0] #[(0,3),(0,4),(0,5),(0,6)]
        fieldtile_high = stagetiles[key][1] #[(1,3),(1,6)]
        lidx = 0
        for y in range(self.width//8):
            for x in range(self.height//8):
                val = pyxel.floor(abs(pyxel.noise(x*scale, y*scale, z*scale) * span))
                if val < border :
                    pyxel.tilemap(tm).pset(x,y,fieldtile_low[0])
                    if pyxel.rndi(0,100) < val:
                        pyxel.tilemap(tm).pset(x,y,fieldtile_low[lidx%len(fieldtile_low)])
                        lidx += 1
                else:
                    pyxel.tilemap(tm).pset(x,y,fieldtile_high[0])
        

        clifftile = stagetiles[key][2] #[(1,4),(1,5)]
        for y in range(self.width//8 - 1):
            for x in range(self.height//8):
                if fieldtile_high[0] == pyxel.tilemap(tm).pget(x,y) :
                    if fieldtile_low[0][0] == pyxel.tilemap(tm).pget(x,y+1)[0] :
                        pyxel.tilemap(tm).pset(x,y+1,clifftile[0])
                        if y+2 < self.height//8:
                            pyxel.tilemap(tm).pset(x,y+2,clifftile[1])
                    elif pyxel.rndi(1,100) < 10:
                        pyxel.tilemap(tm).pset(x,y,fieldtile_high[1])
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



if __name__ == '__main__':
    APP_WIDTH = 256
    APP_HEIGHT = 224
    pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
    pyxel.load("actadv.pyxres")

    x=y=0
    stg = Stage(256,200)

    stgname = ['grassy','rocky','ice']
    cnt = 0

    def update():
        global x,y,cnt

        if pyxel.btnp(pyxel.KEY_SPACE):
            scale = pyxel.rndf(0.055,0.075)
            z = pyxel.rndi(0,128)
            stg.genmap(1024,1024,scale,z,stgname[cnt%len(stgname)])
            cnt += 1
    
        dx = dy = 0
        if pyxel.btn(pyxel.KEY_UP):
            dy -= 20
        if pyxel.btn(pyxel.KEY_DOWN):
            dy += 20
        if pyxel.btn(pyxel.KEY_LEFT):
            dx -= 20
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx += 20
        
        x += dx
        y += dy
        stg.update(x,y)
        return

    def draw():
        pyxel.cls(0)
        stg.draw()
        
        return

    pyxel.run(update, draw)
