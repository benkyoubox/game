import pyxel
from common import *
import sprites as mod_sprite
import stages as mod_stage


pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
pyxel.load("actadv.pyxres")

stgname = ['grassy','rocky','ice','cave']
player = mod_sprite.Player(10,10,'player')
stg = mod_stage.Stage(STAGE_WIDTH,STAGE_HEIGHT)
cnt = 0
stg.setresource(cnt,1,256*8,256*8)
player.setpos(cnt,10,10)

bullets = []
enemies = []

for i in range(100):
    ex = pyxel.rndi(30,2000)
    ey = pyxel.rndi(30,2000)
    enemies.append(mod_sprite.Enemy(ex,ey,'enm1'))
    ex = pyxel.rndi(30,2000)
    ey = pyxel.rndi(30,2000)
    enemies.append(mod_sprite.Enemy(ex,ey,'enm2'))

def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        if stg.is_area(elem.x,elem.y,elem.w,elem.h):
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
    global cnt

    if pyxel.btnp(pyxel.KEY_C):
        cnt += 1
        stg.setresource(cnt%3,1,256*8,256*8)
        scale = pyxel.rndf(0.055,0.075)
        z = pyxel.rndi(0,128)
        stg.genmap(256*8,256*8,scale,z,stgname[cnt%len(stgname)])
        player.setpos(cnt%3,player.x,player.y)

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
    
    for enemy in enemies:
        if player.chkenemy(enemy.x,enemy.y,enemy.w,enemy.h) :
            # TODO damage
            pass

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
    pyxel.camera()
    pyxel.rect(0,STAGE_HEIGHT,STAGE_WIDTH,APP_HEIGHT-STAGE_HEIGHT,0)
    x = 10
    y = STAGE_HEIGHT+5
    w = 50 * player.life / 10
    h = 8
    pyxel.text(x,y+2,"Life",7)
    pyxel.rect(x+18,y,w,h,11)
    pyxel.rectb(x+18,y,50,h,7)
    return

pyxel.run(update, draw)
