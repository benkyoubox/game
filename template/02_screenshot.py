# Save the screenshot to the desktop
# Win   Alt+1
# Mac   Option+1

import pyxel

pyxel.init(64, 64, display_scale=5,capture_scale=5)
pyxel.load("sample.pyxres")
pyxel.cls(0)

#     blt( x, y, img, u, v, w, h,  col )
pyxel.blt( 0, 0,   0, 0, 0, pyxel.width,pyxel.height, 0 )

pyxel.show()
