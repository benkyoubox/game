# ビットマップフォントを表示するPyxelプログラム
#
# Pyxel 1.9.13 以降で実行してください
#

import pyxel
from font.bdfrenderer import BDFRenderer
pyxel.init(256, 128,display_scale=2,capture_scale=2)

# BDFRendererはpyxel.init()後に呼び出すこと
bdf1 = BDFRenderer("font/umplus_j10r.bdf")
bdf2 = BDFRenderer("font/umplus_j12r.bdf")

pyxel.cls(1)

# 参考
# ""で囲んだ文字列内で \ " をただの記号として扱うには
# エスケープ文字\をつけて，\\ \" で指定する
str1 = "0123456789+-*/=\\"
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'\"<>_"

pyxel.text(10,2,"umplus_j10r.bdf",11)
bdf1.draw_text(10, 10, str1, 7)
bdf1.draw_text(10, 20, str2, 7)
bdf1.draw_text(10, 30, str3, 7)

pyxel.text(10,50,"umplus_j12r.bdf",11)
bdf2.draw_text(10, 60, str1, 7)
bdf2.draw_text(10, 72, str2, 7)
bdf2.draw_text(10, 84, str3, 7)

pyxel.show()
