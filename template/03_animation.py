# Save the screen capture video to the desktop
# Win   Alt+3
# Mac   Option+3

import pyxel

SCALE = 5
pyxel.init(64, 64, display_scale=SCALE,capture_scale=SCALE,capture_sec=10)
#pyxel.load(".pyxres")


# 一定時間だけ動かしたいときはforループ
#for i in range(60):
while(True):
    pyxel.cls(0)
    pyxel.text(10,10, "Test", pyxel.frame_count % 16)

    pyxel.flip()


# プログラムでのgifファイル出力
#pyxel.screencast(SCALE)
#pyxel.quit()
