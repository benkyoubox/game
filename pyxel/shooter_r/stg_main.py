import pyxel
import stages as st
import player as pl
import enemies as en
import effects as ef
import sound as snd

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

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


class App:
    """ アプリケーション本体 """
    
    def __init__(self):
        pyxel.init(240, 160, title="Pyxel Shooter r")
        pyxel.load("sample.pyxres")
        snd.init()
        snd.bgm()
        self.scene = SCENE_TITLE
        self.score = 0
        self.tmr = 0
        self.boss = False
        self.stage = 1
        self.background = st.Background()
        self.player = pl.Player(20, pyxel.height / 2)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tmr += 1
        self.background.update()
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()
        return

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_PLAY
            self.tmr = 0

    def update_play_scene(self):
        sec = self.tmr // 30

        if sec < 0:
            pass
        elif sec < 10:
            if pyxel.frame_count % 30 == 0:
                en.Enemy(pyxel.width,pyxel.rndi(20,pyxel.height - 20),-2,0)
            if pyxel.frame_count % 60 == 20 and 5 < sec :
                en.EnemyA(pyxel.width,pyxel.rndi(40,pyxel.height - 40),-2.5,pyxel.rndi(-2,2))
        elif sec < 20:
            if pyxel.frame_count % 60 == 0:
                en.Enemy(pyxel.width,pyxel.rndi(20,pyxel.height - 20),-2,0)
            if pyxel.frame_count % 60 == 20:
                en.EnemyA(pyxel.width,pyxel.rndi(40,pyxel.height - 40),-2.5,pyxel.rndi(-2,2))
            if pyxel.frame_count % 90 == 30:
                en.EnemyB(pyxel.width,pyxel.rndi(30,pyxel.height - 30),-2.5,0)
        else:
            if False == self.boss:
                en.Boss(pyxel.width,pyxel.height/2,5*self.stage)
                self.boss = True

        for enemy in en.enemies:
            if en.TYPE_NORMAL == enemy.type or en.TYPE_BOSS == enemy.type:
                for bullet in pl.bullets:
                    if (
                        enemy.x + enemy.w > bullet.x
                        and bullet.x + bullet.w > enemy.x
                        and enemy.y + enemy.h > bullet.y
                        and bullet.y + bullet.h > enemy.y
                    ):
                        bullet.is_alive = False
                        enemy.life -= 1
                        if enemy.life <= 0 and en.TYPE_NORMAL == enemy.type:
                            enemy.is_alive = False
                            ef.blasts.append(
                                ef.Blast(enemy.x + enemy.w / 2,
                                      enemy.y + enemy.h / 2)
                            )
                            snd.blast()
                            self.score += 10
                        elif enemy.life <= 0 and en.TYPE_BOSS == enemy.type:
                            enemy.destroy()
                            enemy.is_alive = False
                            tmpx = enemy.x + enemy.w / 2 -8
                            tmpy = enemy.y + enemy.h / 2 -8
                            for i in range(1,7):
                                tgtx = tmpx + pyxel.rndi(-7,7)
                                tgty = tmpy + pyxel.rndi(-7,7)
                                ef.blasts.append(ef.BlastLarge(tgtx,tgty, i*5))
                            snd.blast()
                            self.score += 500
                            self.boss = False
                            self.tmr = -30*3  # 次の周回開始まで3秒
                            self.stage += 1
                        else:
                            ef.blasts.append(
                                ef.BlastSmall(enemy.x + enemy.w / 2,
                                      enemy.y + enemy.h / 2)
                            )

        for enemy in en.enemies:
            if (
                self.player.x + self.player.w > enemy.x
                and enemy.x + enemy.w > self.player.x
                and self.player.y + self.player.h > enemy.y
                and enemy.y + enemy.h > self.player.y
            ):
                enemy.life -= 1
                if enemy.life <= 0:
                    enemy.is_alive = False

                ef.blasts.append(
                    ef.Blast(
                        self.player.x + self.player.w / 2,
                        self.player.y + self.player.h / 2,
                    )
                )
                snd.blast()
                self.scene = SCENE_GAMEOVER
                self.tmr = 0

        self.player.update()
        update_list(pl.bullets)
        update_list(en.enemies)
        update_list(ef.blasts)
        cleanup_list(en.enemies)
        cleanup_list(pl.bullets)
        cleanup_list(ef.blasts)
        return

    def update_gameover_scene(self):
        update_list(pl.bullets)
        update_list(en.enemies)
        update_list(ef.blasts)
        cleanup_list(en.enemies)
        cleanup_list(pl.bullets)
        cleanup_list(ef.blasts)

        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_PLAY
            self.tmr = 0
            self.player.x = 20
            self.player.y = pyxel.height / 2
            self.score = 0
            self.boss = False
            self.stage = 1
            en.enemies.clear()
            pl.bullets.clear()
            ef.blasts.clear()

    def draw(self):
        pyxel.cls(0)
        self.background.draw()
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()
        pyxel.text(10, 4, f"SCORE {self.score:5}", 7)
        return

    def draw_title_scene(self):
        pyxel.text(95, 66, "Pyxel Shooter", pyxel.frame_count % 16)
        pyxel.text(91, 126, "- PRESS ENTER -", 13)

    def draw_play_scene(self):
        self.player.draw()
        draw_list(pl.bullets)
        draw_list(en.enemies)
        draw_list(ef.blasts)
        return

    def draw_gameover_scene(self):
        draw_list(pl.bullets)
        draw_list(en.enemies)
        draw_list(ef.blasts)
        pyxel.text(102, 66, "GAME OVER", 8)
        pyxel.text(91, 126, "- PRESS ENTER -", 13)


App()
