# Save pngfiles
# output image_0.png,image_1.png,image_2.png

import pyxel

SCALE = 1
pyxel.init(256, 256, display_scale=SCALE,capture_scale=SCALE)
pyxel.load("sample.pyxres")

pyxel.image(0).save("image_0", SCALE)
pyxel.image(1).save("image_1", SCALE)
pyxel.image(2).save("image_2", SCALE)

pyxel.text(10,10,"save images",7)
pyxel.show()
