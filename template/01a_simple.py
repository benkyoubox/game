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
