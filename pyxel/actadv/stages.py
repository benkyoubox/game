import pyxel
from common import *

stagetiles = {'grassy':[[(0,1),(0,2),(0,3),(0,4)],[(1,0)],[(1,1),(1,2)]],
              'rocky': [[(2,0),(2,1)],[(3,0)],[(3,1),(3,2)]],
              'ice':   [[(4,0),(4,1)],[(5,0)],[(5,1),(5,2)]]}

class Stage:

    def __init__(self,width,height) -> None:
        self.area_width = width
        self.area_height = height
        self.disp_w = width
        self.disp_h = height
        self.scroll_x = 0
        self.scroll_y = 0
        self.left_border = width *0.33
        self.right_border = width *0.66 -16
        self.upper_border = height * 0.33
        self.bottom_border = height * 0.66 -16
        self.col = 0
        self.tm = 0
        return

    def is_area(self,x,y,w,h) -> bool:
        if self.scroll_x < x + w and x < self.scroll_x + self.disp_w \
            and self.scroll_y < y + h and y < self.scroll_y + self.disp_h :
            return True
        else:
            return False
            

    def setresource(self,tm_,img,width,height):
        self.tm = tm_
        pyxel.tilemap(self.tm).refimg = img
        self.area_width = width
        self.area_height = height
        return

    def genmap(self,width,height,scale,z,key):
        ''' w,h pixelsize  scale=0.05-0.07 z=1- '''
        self.area_width = width
        self.area_height = height
        fieldtile_low = stagetiles[key][0]
        fieldtile_high = stagetiles[key][1]
        for y in range(self.area_width//8):
            for x in range(self.area_height//8):
                n = abs(pyxel.noise(x*scale, y*scale, z*scale))

                if n < 0.15:
                    pyxel.tilemap(self.tm).pset(x,y,fieldtile_low[1])
                elif n < 0.5:
                    pyxel.tilemap(self.tm).pset(x,y,fieldtile_low[0])
                else:
                    pyxel.tilemap(self.tm).pset(x,y,fieldtile_high[0])

        clifftile = stagetiles[key][2]
        for y in range(self.area_width//8 - 1):
            for x in range(self.area_height//8):
                if fieldtile_high[0] == pyxel.tilemap(self.tm).pget(x,y) :
                    if fieldtile_low[0][0] == pyxel.tilemap(self.tm).pget(x,y+1)[0] :
                        pyxel.tilemap(self.tm).pset(x,y+1,clifftile[0])
                        if y+2 < self.area_height//8:
                            pyxel.tilemap(self.tm).pset(x,y+2,clifftile[1])
        if 'grassy' == key:
            for y in range(self.area_width//8):
                for x in range(self.area_height//8):
                    if fieldtile_low[0] == pyxel.tilemap(self.tm).pget(x,y) :
                        n = pyxel.noise(x*0.08, y*0.08, z*scale)*pyxel.rndf(-1.11,1.19)
                        if n < -0.4:
                            pyxel.tilemap(0).pset(x,y,fieldtile_low[2])
                        elif 0.4 < n:
                            pyxel.tilemap(0).pset(x,y,fieldtile_low[3])
                    
        return

    def update(self,x,y):
        if x < self.scroll_x + self.left_border:
            self.scroll_x = x - self.left_border
            if self.scroll_x < 0:
                self.scroll_x = 0
        if self.scroll_x + self.right_border < x:
            self.scroll_x = x - self.right_border
            if self.area_width - self.disp_w < self.scroll_x:
                self.scroll_x = self.area_width - self.disp_w
            
        if y < self.scroll_y + self.upper_border:
            self.scroll_y = y - self.upper_border
            if self.scroll_y < 0:
                self.scroll_y = 0
        if self.scroll_y + self.bottom_border < y:
            self.scroll_y = y - self.bottom_border
            if self.area_height - self.disp_h < self.scroll_y:
                self.scroll_y = self.area_height - self.disp_h
        return
    
    def draw(self):
        pyxel.camera()
        pyxel.bltm(0,0, self.tm, self.scroll_x,self.scroll_y, self.disp_w,self.disp_h, self.col)
        pyxel.camera(self.scroll_x,self.scroll_y)
        return



if __name__ == '__main__':
    APP_WIDTH = 256
    APP_HEIGHT = 224
    pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
    pyxel.load("actadv.pyxres")

    x=y=0
    stg = Stage(256,200)
    stg.setresource(0,1,256*8,256*8)

    stgname = ['grassy','rocky','ice']
    cnt = 0

    def update():
        global x,y,cnt

        if pyxel.btnp(pyxel.KEY_SPACE):
            stg.setresource(7,1,256*8,256*8)
            scale = pyxel.rndf(0.055,0.075)
            z = pyxel.rndi(0,128)
            stg.genmap(256*8,256*8,scale,z,stgname[cnt%len(stgname)])
        
        if pyxel.btnp(pyxel.KEY_S):
            pyxel.save("newmap.pyxres")
    
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
