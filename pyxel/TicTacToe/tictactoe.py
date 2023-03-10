import pyxel
pyxel.init(32,32,title="Tic-Tac-Toe",capture_scale=5)
pyxel.load("sample.pyxres")
pyxel.mouse(True)

character_list =[(8,0),(0,16)]
MARGIN = 2  # 盤面余白ドット

def idx_to_points(xi,yi):
    """ マス目の位置を座標に変換 """
    x = MARGIN + 1 +(8+1)*xi
    y = MARGIN + 1 +(8+1)*yi
    return (x,y)

def points_to_idx(x,y):
    """ xy座標をマス目に変換 """
    xi = (x - (MARGIN+1))//9
    yi = (y - (MARGIN+1))//9
    return (xi,yi)

class Board:
    """ 盤面を管理するクラス """
    def __init__(self):
        self.grids = [[0,0,0],
                      [0,0,0],
                      [0,0,0]] # 状態 0:空き 1:先手 2:後手
        self.markers = []   # コマのインスタンスを格納する配列
        self.turn = 0       # 手番 0:先手　1:後手
        self.status = 0 # 0:クリック待ち 1:P1勝利 2:P2勝利 3:引き分け
        self.effect = []

    def check_grids(self,x,y):
        """ クリック位置の判定処理 """
        ret = False
        xi,yi = points_to_idx(x,y)
        if 0 <= xi and xi < 3 and 0 <= yi and yi < 3:
            if 0 == self.grids[yi][xi]:
                # 空きマスの場合は盤面の状態を更新する
                ret = True
                self.grids[yi][xi] = self.turn + 1 # 先手を1，後手を2
        return ret,xi,yi

    def is_win(self,xi,yi):
        """ 勝利判定 勝ちの場合True """
        t = self.grids[yi][xi]
        flg_win = False
        # 横方向
        if t == self.grids[yi][0] and t == self.grids[yi][1] and t == self.grids[yi][2]:
            flg_win = True
            self.effect = [(0,yi),(1,yi),(2,yi)]
        # 縦方向
        if t == self.grids[0][xi] and t == self.grids[1][xi] and t == self.grids[2][xi]:
            flg_win = True
            self.effect = [(xi,0),(xi,1),(xi,2)]
        # 斜め
        if t == self.grids[0][0] and t == self.grids[1][1] and t == self.grids[2][2]:
            flg_win = True
            self.effect = [(0,0),(1,1),(2,2)]
        if t == self.grids[2][0] and t == self.grids[1][1] and t == self.grids[0][2]:
            flg_win = True
            self.effect = [(0,2),(1,1),(2,0)]
        return flg_win

    def is_full(self):
        """ 空きマス判定 空き無しの場合True """
        ret = True
        for row in self.grids:
            for cell in row:
                if 0 == cell:
                    ret = False
                    break
            if not(ret) :
                break
        return ret

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 0 == self.status:
            ret,xi,yi = self.check_grids(pyxel.mouse_x,pyxel.mouse_y)
            if ret :
                x,y = idx_to_points(xi,yi)
                self.markers.append(Sprite(x,y,self.turn))
                if self.is_win(xi,yi) :
                    # 手番プレーヤーの勝利
                    self.status = self.turn + 1
                elif self.is_full():
                    # 引き分け
                    self.status = 3
                else:
                    # 手番交代(0と1の繰り返し)
                    self.turn = 1 - self.turn
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 0 != self.status:
            # 最初に戻す
            self.markers.clear()
            self.effect.clear()
            self.__init__()

        return
    
    def draw(self):
        pyxel.cls(0)
        # 枠線を1ドットのlineで描く
        m = MARGIN
        width = (8+1)*3     # 線の終端用
        for i in range(4):
            pyxel.line(m,m+9*i, m+width,m+9*i, 1)
            pyxel.line(m+9*i,m, m+9*i,m+width, 1)

        # コマを表示する
        for marker in self.markers:
            marker.draw()

        if 1 == self.status or 2 == self.status:
            for xi,yi in self.effect:
                x,y = idx_to_points(xi,yi)
                pyxel.circb(x+3,y+3,4,pyxel.frame_count % 16)
        if 3 == self.status:
            pyxel.rect(7,13,17,7,0)
            pyxel.text(8,14,"DRAW",7)

        return

class Sprite:
    """ キャラクターを表示するクラス """
    def __init__(self,x,y,idx):
        self.x = x
        self.y = y
        self.u , self.v = character_list[idx]
   
    def draw(self):
        pyxel.blt(self.x,self.y, 0, self.u,self.v, 8,8, 0)
        return

# ここからメインの処理
b = Board()
def update():
    b.update()
    return

def draw():
    b.draw()
    return

pyxel.run(update, draw)
