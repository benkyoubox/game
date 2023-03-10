import pyxel

SND_SHOT = 60
SND_BLAST = 61
BGM = 0
SE_CH = 3

def init():
    pyxel.sound(SND_SHOT).set("a3a2c1a1", "p", "7", "s", 5)
    pyxel.sound(SND_BLAST).set("a3a2c2c2", "n", "7742", "s", 10)


def shot():
    pyxel.play(SE_CH, SND_SHOT)

def blast():
    pyxel.play(SE_CH, SND_BLAST)

def bgm():
    pyxel.playm(BGM, loop=True)
