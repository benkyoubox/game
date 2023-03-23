# Save the screen capture video to the desktop
# Win   Alt+3
# Mac   Option+3
#
# アプリ画面が終了しないときはIDLEシェルを終了させる

import pyxel

SCALE = 5
pyxel.init(64, 64, display_scale=SCALE,capture_scale=SCALE,capture_sec=10)
#pyxel.load(".pyxres")

x = 4
y = 4
w = 16
h = 16

for i in range(60):
    pyxel.cls(0)
    x += 1
    y += 1
    w += 1
    h += 1
    pyxel.rect(x,y, w,h, 7)
    pyxel.flip()

# プログラムでのgifファイル出力
#pyxel.screencast(SCALE)
