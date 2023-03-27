import pyxel
pyxel.init(120,96)

ball_x = 40
ball_y = 20
ball_r = 4
ball_xp = 3
ball_yp = 2

bar_x = 20
bar_y = 80
bar_w = 20
bar_h = 4

# add ******
flg = False

def update():
    # add flg
    global ball_x,ball_y,ball_xp,ball_yp,bar_x,flg

    # add ******
    if flg :
        return

    ball_x += ball_xp
    if ball_x < 0 or pyxel.width - ball_r < ball_x :
        ball_xp = -ball_xp
       
    ball_y += ball_yp
    # chg *******
    if ball_y < 0 :
        ball_yp = -ball_yp
    elif pyxel.height - ball_r < ball_y :
        flg = True

    bar_x = pyxel.mouse_x
    if bar_x < 0 :
        bar_x = 0
    elif pyxel.width - bar_w < bar_x :
        bar_x = pyxel.width - bar_w

    # add *******
    if ( bar_x - 4 < ball_x < bar_x + bar_w + 8 ) and ( bar_y - 4 < ball_y < bar_y + 2 ) :
           ball_yp = -2 - pyxel.rndi(0,2)
    
    return

def draw():
    pyxel.cls(0)
    pyxel.circ(ball_x, ball_y, ball_r, 10)
    pyxel.rect(bar_x, bar_y, bar_w, bar_h, 3)

    # add *******
    if flg :
        pyxel.text(42,40, "GAME OVER", 7)
    
    return

pyxel.run(update,draw)
