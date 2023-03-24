# Pyxel用 Appクラス
# メイン処理コード例

import pyxel

APP_WIDTH = 256
APP_HEIGHT = 224

class App:
    def __init__(self):
        pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
        #pyxel.load("sample.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        return

    def draw(self):
        pyxel.cls(0)
        return

App()

# 以降 Appクラスの update() と draw() が繰り返し実行されます
