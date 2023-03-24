# Pyxel用 プログラムひな形
# クラスを使わない記述例

import pyxel

APP_WIDTH = 256
APP_HEIGHT = 224

pyxel.init(APP_WIDTH, APP_HEIGHT, title="Pyxel")
#pyxel.load("sample.pyxres")
pyxel.mouse(True)

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    return

def draw():
    pyxel.cls(0)
    return

pyxel.run(update, draw)

# 以降 update() と draw() が繰り返し実行されます
