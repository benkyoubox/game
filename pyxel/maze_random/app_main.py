import pyxel
import player as pl
import stage as stg
import enemy as en

APP_WIDTH = 240
APP_HEIGHT = 160

# シーン番号
SNO_TITLE    = 0
SNO_STAGESET = 10
SNO_PLAY     = 11
SNO_SFINISH  = 12
SNO_GAMEOVER = 13

    
class App:
    ''' メイン処理 '''
    
    def __init__(self):
        pyxel.init(APP_WIDTH, APP_HEIGHT)
        pyxel.load("alice.pyxres")
        self.scene = SNO_TITLE
        self.tmr = 0
        self.player = pl.Player(112,100)
        self.enemy = en.Enemy(184,32)
        self.stg = stg.Stage()
        self.stage_no = 1
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tmr += 1
        if SNO_TITLE == self.scene:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.scene = SNO_STAGESET
                self.tmr = 0
                self.stage_no = 1
        elif SNO_STAGESET == self.scene:
            if 30 == self.tmr:
                size = 42+self.stage_no*6
                self.stg.makemaze(size)
                x = self.stg.sx
                y = self.stg.sy
                self.player.setpos(x,y)
                self.enemy.moverandom(x,y,size*8)
                self.scene = SNO_PLAY
                self.tmr = 0
            
        elif SNO_PLAY == self.scene:
            self.enemy.update(self.player.x,self.player.y)
            self.player.update()
            x = self.player.x
            y = self.player.y
            self.stg.update(x,y)

            if self.stg.chkgoal(x,y) :
                self.player.goal()
                self.scene = SNO_SFINISH
                self.tmr = 0
            elif self.enemy.chkenemy(x,y) :
                self.scene = SNO_GAMEOVER
                self.tmr = 0
            
        elif SNO_SFINISH == self.scene:
            self.player.update()
            if 30*3 < self.tmr :
                self.stage_no += 1
                self.scene = SNO_STAGESET
                self.tmr = 0
            
        elif SNO_GAMEOVER == self.scene:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                self.scene = SNO_STAGESET
                self.tmr = 0
                self.stage_no = 1
                self.enemy.setspeed(True)
        else:
            pass
        
        
        return

    def ctext(self,tx,ty,msg,col):
        ''' メッセージを中央表示 '''
        sx = self.stg.scroll_x
        sy = self.stg.scroll_y
        cx = APP_WIDTH / 2
        cy = APP_HEIGHT / 2        
        num = len(msg) # 文字数取得
        x = sx + cx - (num*4)/2
        y = sy + cy - 4
        pyxel.text(x+tx,y+ty,msg,col)
        
        return

    def draw(self):
        self.stg.draw()
        self.player.draw()
        self.enemy.draw()

        if SNO_TITLE == self.scene:
            if self.tmr%40 < 20:
                self.ctext(0,0,"Press SPACE to Start.",7)

        elif SNO_STAGESET == self.scene:
            self.ctext(0,0,"Stage "+str(self.stage_no),7)
        elif SNO_PLAY == self.scene:
            pass
        elif SNO_SFINISH == self.scene:
            self.ctext(0,0,"Clear a stage.",7)
        elif SNO_GAMEOVER == self.scene:
            self.ctext(0,-20,"GAME OVER",7)
            self.ctext(0,-10,"Stage "+str(self.stage_no),7)
            self.ctext(0,10,"Press SPACE to Start.",7)
        else:
            pass


        return

App()
