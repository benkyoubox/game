import pyxel
pyxel.init(128,128)
pyxel.load("maze.pyxres")
STAGE_WIDTH = 128 * 16
STAGE_HEIGHT = 128 * 16
LEFT_BORDER = 40
RIGHT_BORDER = pyxel.width - 48
UPPER_BORDER = 40
BOTTOM_BORDER = pyxel.height - 40
scroll_x = 0
scroll_y = 0

x = 8
y = 8
pldir = 1 # 0:up 1:down 2:left 3:right
speed = 2
u = 0
v0 = 16
v1 = v0 + 16
v2 = v1 + 16
v3 = v2    # 左右同じ絵を使う
CHR_ANIMA = [
    [(u,v0),(u+16,v0),(u,v0),(u+32,v0)],
    [(u,v1),(u+16,v1),(u,v1),(u+32,v1)],
    [(u,v2),(u+16,v2),(u,v2),(u+32,v2)],
    [(u,v3),(u+16,v3),(u,v3),(u+32,v3)]
    ]
ani = 0

en_x = 128
en_y = 128

chkpoint = [(0,0),(7,0),(15,0),
            (0,7),      (15,7),
            (0,15),(7,15),(15,15)]
def chkwall(cx,cy):
    c = 0
    if cx < 0 or STAGE_WIDTH < cx + 16:
        c += 1
    if cy < 0 or STAGE_HEIGHT < cy + 16:
        c += 1
    for cpx,cpy in chkpoint:
        xi = (cx + cpx)//8
        yi = (cy + cpy)//8
        if (1,0) == pyxel.tilemap(0).pget(xi,yi):
            c += 1
    return c

def chkgoal():
    ret = False
    xi = (x + 8)//8
    yi = (y + 8)//8
    tile = pyxel.tilemap(0).pget(xi,yi)
    if (2,0) == tile or (3,0) == tile or (2,1) == tile or (3,1) == tile:
        ret = True
    return ret

def chkenemy():
    ret = False
    if ( x < en_x + 16
         and en_x < x + 16
         and y < en_y +16
         and en_y < y + 16):
        ret = True
    return ret        

def update():
    global scroll_x,scroll_y,x,y,pldir,ani,en_x,en_y
    dx = dy = 0
    
    if pyxel.btn(pyxel.KEY_UP):
        pldir = 0
        ani += 1
        dy = -speed
    if pyxel.btn(pyxel.KEY_DOWN):
        pldir = 1
        ani += 1
        dy = speed
    if pyxel.btn(pyxel.KEY_LEFT):
        pldir = 2
        ani += 1
        dx = -speed
    if pyxel.btn(pyxel.KEY_RIGHT):
        pldir = 3
        ani += 1
        dx = speed

    # キャラクターの移動
    if 0 == chkwall(x+dx,y+dy):
        x += dx
        y += dy

    # 画面のスクロール
    if x < scroll_x + LEFT_BORDER:
        scroll_x = x - LEFT_BORDER
        if scroll_x < 0:
            scroll_x = 0
    if scroll_x + RIGHT_BORDER < x:
        scroll_x = x - RIGHT_BORDER
        if STAGE_WIDTH - pyxel.width < scroll_x:
            scroll_x = STAGE_WIDTH - pyxel.width

    if y < scroll_y + UPPER_BORDER:
        scroll_y = y - UPPER_BORDER
        if scroll_y < 0:
            scroll_y = 0
    if scroll_y + BOTTOM_BORDER < y:
        scroll_y = y - BOTTOM_BORDER
        if STAGE_HEIGHT - pyxel.height < scroll_y:
            scroll_y = STAGE_HEIGHT - pyxel.height

    # お化けの移動
    if chkgoal() == False:
        en_x = en_x + (x - en_x) / 60
        en_y = en_y + (y - en_y) / 60
    
    return

def draw():
    pyxel.cls(1)
    pyxel.camera()
    pyxel.bltm(0,0, 0, scroll_x,scroll_y, pyxel.width,pyxel.height, 0)

    pyxel.camera(scroll_x,scroll_y)
    
    u,v = CHR_ANIMA[pldir][ani//4 % 4]
    w = 16
    if 3 == pldir:
        w = -16
    pyxel.blt( x, y, 0,  u, v, w,16, 0)

    # お化けの表示
    pyxel.blt(en_x,en_y, 0, 32,0, 16,16, 0)

    if chkgoal() :
        pyxel.text(scroll_x+50,scroll_y+50,"GOAL!!", pyxel.frame_count % 16)
    elif chkenemy():
        pyxel.text(scroll_x+50,scroll_y+50,"failure", pyxel.frame_count % 16)
        
    return

pyxel.run(update,draw)
