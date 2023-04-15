import pyxel
APP_WIDTH = 256
APP_HEIGHT = 256
pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel", capture_scale=4)

#pyxel.load("newmap.pyxres")
TM = 0
IMGBANK = 1

data = ["0000000033333333ffffffffeeeeeeee7777777767677777",
"000000003b333333f9ffffffe9eeeeee7777777777776776",
"00000000333333b3ffffff9feeeeee9e77777777777dd777",
"0000000033333333ffffffffeeeeeeee777777777dd77777",
"0000000033333b33fff9ffffeeeeeeee777777776d777776",
"0000000033333333ffffffffeeeefeee7777777777776777",
"0000000033b333339fffffffeeeeeeee7777777776777777",
"0000000033333333fffff9ffeeeeeeee7777777777777777",
"bbbbbbbbb3b3b3b3ffdffdff444444447777777777777777",
"bbb3bbbb5b5b5b5bdfffffdf494444447777777777c77777",
"bbbbbbbb45544455ffffdfff44444444777777677dc77d7d",
"bbbbbbbb44444454fdfffffd44444444767777777dc77dcd",
"bbbbbbbb54444444ffdfdfff4444444477777777ddc7cddc",
"bbbbbbb344444444ffffffdf4449444477777777ddddcddc",
"b3bbbbbb4444d444dffffdff4444444477776777dcdddddc",
"bbbbbbbb44444444fffdffff4444444477777777dcdddddc",
"fffbffff44444444000000004444444400000000dcddddd6",
"bfffffff44445444000000004444444400000000dd6ddcd6",
"ffffffbfd4444444000000004444444400000000dd6ddcd6",
"fffbffff44444444000000004444449400000000dddd6dd6",
"fffffffb444444d4000000004444444400000000ddd6ddd6",
"fbffffff44444444000000004444444400000000ddd6ddd6",
"fffffbff43444434000000004944444400000000d6ddddd6",
"bfffffff3b43b34b00000000444444440000000076dddd67",
"bb3bbbbb0000000000000000000000000000000000000000",
"3abbb3bb0000000000000000000000000000000000000000",
"bbbbbb730000000000000000000000000000000000000000",
"bbbbb3bb0000000000000000000000000000000000000000",
"b3b3bbbb0000000000000000000000000000000000000000",
"bbabbbb30000000000000000000000000000000000000000",
"bb3bbb3b0000000000000000000000000000000000000000",
"3bbbbbbb0000000000000000000000000000000000000000",
"bbb7bbbb0000000000000000000000000000000000000000",
"bb3b3bb30000000000000000000000000000000000000000",
"3bbbbbab0000000000000000000000000000000000000000",
"bbbbb3b30000000000000000000000000000000000000000",
"b3b3bbbb0000000000000000000000000000000000000000",
"bb7bb3bb0000000000000000000000000000000000000000",
"b3bbbbbb0000000000000000000000000000000000000000",
"bbbb3b3b0000000000000000000000000000000000000000",]

pyxel.image(IMGBANK).set(0,0,data)
pyxel.tilemap(TM).refimg = IMGBANK

stagetiles = {'grassy':[[(0,1),(0,2),(0,3),(0,4)],[(1,0)],[(1,1),(1,2)]],
              'rocky': [[(2,0),(2,1)],[(3,0)],[(3,1),(3,2)]],
              'ice':   [[(4,0),(4,1)],[(5,0)],[(5,1),(5,2)]]}

class Stage:

    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.disp_w = width
        self.disp_h = height
        self.scroll_x = 0
        self.scroll_y = 0
        self.col = 0
        return
    
    def genmap(self,width,height,scale,z,key):
        ''' w,h pixelsize  scale=0.05-0.07 z=1- '''
        self.width = width
        self.height = height
        fieldtile_low = stagetiles[key][0]
        fieldtile_high = stagetiles[key][1]
        lidx = 0
        for y in range(self.width//8):
            for x in range(self.height//8):
                n = abs(pyxel.noise(x*scale, y*scale, z*scale))

                if n < 0.15:
                    pyxel.tilemap(TM).pset(x,y,fieldtile_low[1])
                elif n < 0.5:
                    pyxel.tilemap(TM).pset(x,y,fieldtile_low[0])
                else:
                    pyxel.tilemap(TM).pset(x,y,fieldtile_high[0])

        clifftile = stagetiles[key][2]
        for y in range(self.width//8 - 1):
            for x in range(self.height//8):
                if fieldtile_high[0] == pyxel.tilemap(TM).pget(x,y) :
                    if fieldtile_low[0][0] == pyxel.tilemap(TM).pget(x,y+1)[0] :
                        pyxel.tilemap(TM).pset(x,y+1,clifftile[0])
                        if y+2 < self.height//8:
                            pyxel.tilemap(TM).pset(x,y+2,clifftile[1])
        if 'grassy' == key:
            for y in range(self.width//8):
                for x in range(self.height//8):
                    if fieldtile_low[0] == pyxel.tilemap(TM).pget(x,y) :
                        n = pyxel.noise(x*0.08, y*0.08, z*scale)*pyxel.rndf(-1.11,1.19)
                        if n < -0.4:
                            pyxel.tilemap(0).pset(x,y,fieldtile_low[2])
                        elif 0.4 < n:
                            pyxel.tilemap(0).pset(x,y,fieldtile_low[3])
                    
        return

    def update(self,x,y):
        self.scroll_x = x
        self.scroll_y = y
        return
    
    def draw(self):
        pyxel.camera()
        pyxel.bltm(0,0, TM, self.scroll_x,self.scroll_y, self.disp_w,self.disp_h, self.col)
        pyxel.camera(self.scroll_x,self.scroll_y)
        return


x=y=0
stg = Stage(APP_WIDTH,APP_HEIGHT)

stgname = ['grassy','rocky','ice']
cnt = -1
scale = 0
z = 0
def genmap():
    global cnt,scale,z
    cnt += 1
    scale = pyxel.rndf(0.051,0.061)
    z = pyxel.rndi(0,100)
    stg.genmap(256*8,256*8,scale,z,stgname[cnt%len(stgname)])


genmap()

def update():
    global x,y,TM

    if pyxel.btnp(pyxel.KEY_1):
        TM = 1
    elif pyxel.btnp(pyxel.KEY_2):
        TM = 2
    elif pyxel.btnp(pyxel.KEY_3):
        TM = 3
    pyxel.tilemap(TM).refimg = IMGBANK
        
    if pyxel.btnp(pyxel.KEY_SPACE):
        genmap()
    
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
    pyxel.text(x+10,y+10, "scale="+str(scale)+" z="+str(z),0)
    pyxel.text(x+10,y+20,"[Space] change",0)
    pyxel.text(x+10,y+30,"[S] save",0)
    return

pyxel.run(update, draw)
