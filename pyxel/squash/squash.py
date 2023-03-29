import pyxel
pyxel.init(256,224)

ball_x = 40
ball_y = 20
ball_r = 4
ball_dx = 6
ball_dy = 4

bar_x = 20
bar_y = 204
bar_w = 40
bar_h = 4

flg = False

def update():
    global ball_x,ball_y,ball_dx,ball_dy,bar_x,flg

    if flg :
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            flg = False
            ball_x = 40
            ball_y = 20
        return

    ball_x += ball_dx
    if ball_x < 0 or pyxel.width - ball_r < ball_x :
        ball_dx = -ball_dx
       
    ball_y += ball_dy
    if ball_y < 0 :
        ball_dy = -ball_dy
    elif pyxel.height - ball_r < ball_y :
        flg = True

    bar_x = pyxel.mouse_x
    if bar_x < 0 :
        bar_x = 0
    elif pyxel.width - bar_w < bar_x :
        bar_x = pyxel.width - bar_w

    if ( bar_x - 8 < ball_x < bar_x + bar_w + 16 ) and ( bar_y - 8 < ball_y < bar_y ) :
           ball_dy = -4 - pyxel.rndi(0,2)
    
    return

def draw():
    pyxel.cls(0)
    pyxel.circ(ball_x, ball_y, ball_r, 10)
    pyxel.rect(bar_x, bar_y, bar_w, bar_h, 3)

    if flg :
        pyxel.text(110,100, "GAME OVER", 7)
    
    return

pyxel.run(update,draw)
