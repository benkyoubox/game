import pyxel
pyxel.init(256,224)

# add *******
ball_x = 40
ball_y = 20
ball_r = 4
ball_dx = 6
ball_dy = 4

def update():
    global ball_x,ball_y,ball_dx,ball_dy

    ball_x += ball_dx
    if ball_x < 0 or pyxel.width - ball_r < ball_x :
        ball_dx = -ball_dx
       
    ball_y += ball_dy
    if ball_y < 0 or pyxel.height - ball_r < ball_y :
        ball_dy = -ball_dy

    return

def draw():
    pyxel.cls(0)

    # add *******
    pyxel.circ(ball_x, ball_y, ball_r, 10)

    return

pyxel.run(update,draw)
