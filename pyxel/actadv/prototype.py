import pyxel
from common import *
import sprites as mod_sprite
import enemy as mod_enemy
import stages as mod_stage
import effects as mod_efc


pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
pyxel.load("actadv.pyxres")

stgname = ['grassy','rocky','ice','cave']
player = mod_sprite.Player(10,10,'player')
stg = mod_stage.Stage(STAGE_WIDTH,STAGE_HEIGHT)
tm = 3
stg.setresource(tm,1,128*3,256)
player.setpos(tm,24,24)

bullets = []
enemies = []

enemies.append(mod_enemy.EnemyWondering(164,60,'bat',tm,1, mod_enemy.ANI_TYPE_FRONT))
enemies.append(mod_enemy.EnemyWondering(30,100,'snake',tm,1,mod_enemy.ANI_TYPE_LR))
enemies.append(mod_enemy.EnemyWondering(40,180,'rat',tm,1))
enemies.append(mod_enemy.EnemyWondering(80,180,'wolf',tm,2,ani=8))
enemies.append(mod_enemy.EnemyWondering(40,120,'slimeG',tm,1))
enemies.append(mod_enemy.EnemyWondering(60,150,'slimeY',tm,1))
enemies.append(mod_enemy.EnemyWondering(200,220,'mage',tm,2,mod_enemy.ANI_TYPE_FRONT,ani=8))
enemies.append(mod_enemy.EnemyWondering(280,80,'golem',tm,5,ani=8))


def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        if stg.is_area(elem.x,elem.y,elem.w,elem.h):
            elem.draw()

def draw_front(list,ypos,flg):
    for elem in list:
        if stg.is_area(elem.x,elem.y,elem.w,elem.h):
            if flg and ypos < elem.y + elem.h :
                elem.draw()    
            elif flg == False and elem.y + elem.h < ypos :
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
                mod_efc.Hit(enemy.x + enemy.w//2,enemy.y + enemy.h//2)
                enemy.life -= 1
                if enemy.life <= 0:
                    enemy.is_alive = False
    
    for enemy in enemies:
        if player.chkenemy(enemy.x,enemy.y,enemy.w,enemy.h) :
            # TODO damage
            pass

    player.update(dx, dy)
    update_list(bullets)
    update_list(mod_efc.effects)
    for enemy in enemies:
        enemy.update(player.x+8,player.y+8)
    stg.update(player.x,player.y)

    cleanup_list(bullets)
    cleanup_list(enemies)
    cleanup_list(mod_efc.effects)
    return

def draw():
    pyxel.cls(0)
    stg.draw()
    draw_front(enemies,player.y+player.h,False)
    player.draw()
    draw_front(enemies,player.y+player.h,True)
    draw_list(bullets)
    draw_list(mod_efc.effects)
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
