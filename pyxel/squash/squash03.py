import pyxel
pyxel.init(120,96)

ball_x = 40
ball_y = 20
ball_r = 4
ball_xp = 3
ball_yp = 2

# add *******
bar_x = 20
bar_y = 80
bar_w = 20
bar_h = 4

def update():
    # add bar_x
    global ball_x,ball_y,ball_xp,ball_yp,bar_x

    ball_x += ball_xp
    if ball_x < 0 or pyxel.width - ball_r < ball_x :
        ball_xp = -ball_xp
       
    ball_y += ball_yp
    if ball_y < 0 or pyxel.height - ball_r < ball_y :
        ball_yp = -ball_yp

    # add *******
    bar_x = pyxel.mouse_x
    if bar_x < 0 :
        bar_x = 0
    elif pyxel.width - bar_w < bar_x :
        bar_x = pyxel.width - bar_w
    
    return

def draw():
    pyxel.cls(0)
    pyxel.circ(ball_x, ball_y, ball_r, 10)

    # add *******
    pyxel.rect(bar_x, bar_y, bar_w, bar_h, 3)

    return

pyxel.run(update,draw)
