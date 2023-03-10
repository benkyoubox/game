import pyxel
pyxel.init(128,128,title="NINJA")
pyxel.load("ninja.pyxres")

x = 8
y = 100
dx = 0
dy = 0
pldir = 1
jump = 0
score = 0

chkpoint = [(2,0),(6,0),(2,7),(6,7)]
def chkwall(cx,cy):
    c = 0
    if cx < 0 or pyxel.width -8 < cx:
        c = c + 1
    if pyxel.height < cy:
        c = c + 1
    for cpx,cpy in chkpoint:
        xi = (cx + cpx)//8
        yi = (cy + cpy)//8
        if (1,0) == pyxel.tilemap(0).pget(xi,yi):
            c = c + 1
    return c

def update():
    global x,y,dx,dy,pldir,jump,score

    # 操作判定
    if pyxel.btn(pyxel.KEY_LEFT):
        if -3 < dx:
            dx = dx - 1
        pldir = -1
    elif pyxel.btn(pyxel.KEY_RIGHT):
        if dx < 3:
            dx = dx + 1
        pldir = 1
    else:
        dx = int(dx*0.7)

    # 横方向の移動
    lr = pyxel.sgn(dx)
    loop = abs(dx)
    while 0 < loop :
        if chkwall( x + lr, y) != 0:
            dx = 0
            break
        x = x + lr
        loop = loop -1

    # ジャンプと落下
    if jump == 0:
        if chkwall(x,y+1) == 0:
            jump = 2  # 床が無ければ落下
        # スペースキーを押したらジャンプ開始
        if pyxel.btnp(pyxel.KEY_SPACE):
            dy = 8
            jump = 1 # ジャンプ開始
            pyxel.play(0,0)
    else:
        dy = dy - 1
        if dy < 0:
            jump = 2    # 頂点で落下開始

    ud = pyxel.sgn(dy)
    loop = abs(dy)
    while 0 < loop :
        if chkwall(x, y - ud) != 0:
            dy = 0
            if jump == 1:
                jump = 2   # 壁にぶつかって落下
            elif jump == 2:
                jump = 0   # 着地　落下終了
            break
        y = y - ud
        loop = loop -1

    # コイン判定
    xi = (x + 4)//8
    yi = (y + 4)//8
    if (1,1) == pyxel.tilemap(0).pget(xi,yi):
        score = score + 1
        pyxel.tilemap(0).pset(xi,yi,(0,0))
        pyxel.play(1,1)

    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    pyxel.blt( x, y, 0,  0, 8, pldir*8,8, 0)

    if 10 == score :
        pyxel.text(45,56,"FINISH!",7)
    return

pyxel.run(update,draw)
