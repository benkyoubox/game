import pyxel
import sprites as mod_sprite
import stages as mod_stage

APP_WIDTH = 256
APP_HEIGHT = 224
pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
pyxel.load("actadv.pyxres")

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3


x=y=0
player = mod_sprite.Player(x,y,'player')
stg = mod_stage.Stage(256,200)

stgname = ['grassy','rocky','ice']
cnt = 0
stg.genmap(1024,1024, 0.06, 64, stgname[cnt%len(stgname)])

bullets = []
enemies = []

for i in range(10):
    ex = pyxel.rndi(30,256)
    ey = pyxel.rndi(30,256)
    enemies.append(mod_sprite.Enemy(ex,ey,'enm1'))
    ex = pyxel.rndi(30,256)
    ey = pyxel.rndi(30,256)
    enemies.append(mod_sprite.Enemy(ex,ey,'enm2'))

def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        elem.draw()


def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1

def update():
    global x,y,cnt

    if pyxel.btnp(pyxel.KEY_C):
        scale = pyxel.rndf(0.055,0.075)
        z = pyxel.rndi(0,128)
        stg.genmap(1024,1024,scale,z,stgname[cnt%len(stgname)])
        cnt += 1
 
    dx = dy = 0
    if pyxel.btn(pyxel.KEY_UP):
        dy -= player.speed
        player.setwalk(DIR_UP)
    if pyxel.btn(pyxel.KEY_DOWN):
        dy += player.speed
        player.setwalk(DIR_DOWN)
    if pyxel.btn(pyxel.KEY_LEFT):
        dx -= player.speed
        player.setwalk(DIR_LEFT)
    if pyxel.btn(pyxel.KEY_RIGHT):
        dx += player.speed
        player.setwalk(DIR_RIGHT)
    
    if pyxel.btnp(pyxel.KEY_SPACE):
        player.attack()
        bullets.append(mod_sprite.Bullet(player.x,player.y,mod_sprite.WP_SWORD,player.dir))

    for enemy in enemies:
        for bullet in bullets:
            if (
                enemy.x + enemy.w > bullet.x
                and bullet.x + bullet.w > enemy.x
                and enemy.y + enemy.h > bullet.y
                and bullet.y + bullet.h > enemy.y
            ):
                bullet.is_alive = False
                enemy.life -= 1
                if enemy.life <= 0:
                    enemy.is_alive = False
    
    player.update(dx, dy)
    update_list(bullets)
    update_list(enemies)
    stg.update(player.x,player.y)

    cleanup_list(bullets)
    cleanup_list(enemies)

    return

def draw():
    pyxel.cls(0)
    stg.draw()
    player.draw()
    draw_list(enemies)
    draw_list(bullets)
    return

pyxel.run(update, draw)
