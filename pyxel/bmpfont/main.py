# ビットマップフォントを表示するPyxelプログラム
#
# Pyxel 1.9.13 以降で実行してください
#

import pyxel
from font.bdfrenderer import BDFRenderer

APP_WIDTH = 256
APP_HEIGHT = 224

bdf = None

class App:
    def __init__(self):
        pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
        #pyxel.load("sample.pyxres")
        global bdf
        bdf = BDFRenderer("font/umplus_j10r.bdf")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        return

    def draw(self):
        pyxel.cls(0)
        bdf.draw_text(10,10, "日本語表示", 7)
        bdf.draw_text(10,30, "縁取り色指定", 7, 11)
        return

App()
