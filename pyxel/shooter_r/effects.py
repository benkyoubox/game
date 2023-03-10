import pyxel

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

BLAST_ANIMA =[ (80,56),(96,56),(128,56),(32,72),(48,72),(64,72) ]

blasts = []


class Blast:
    """ 爆発演出 """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.is_alive = True
        blasts.append(self)

    def update(self):
        self.radius += 1
        if self.radius > BLAST_END_RADIUS:
            self.is_alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
        pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)


class BlastSmall(Blast):
    """ 爆発演出 小 """

    def update(self):
        self.radius += 1
        if self.radius > BLAST_END_RADIUS-5:
            self.is_alive = False


class BlastLarge(Blast):
    """ 爆発演出 大 """

    def __init__(self, x, y, delay):
        super().__init__(x,y)
        self.tmr = -delay
        
    def update(self):
        self.tmr += 1
        if len(BLAST_ANIMA) -1 == self.tmr//4 :
            self.is_alive = False
            
    def draw(self):
        if 0 <= self.tmr:
            u,v = BLAST_ANIMA[(self.tmr//4)%5]
            pyxel.blt(self.x, self.y, 0, u, v, 16, 16, 0)


def update():
    global eff
    if pyxel.btnp(pyxel.KEY_SPACE):
        eff = BlastLarge(20,20,0)
    if eff.is_alive:
        eff.update()

def draw():
    pyxel.cls(0)
    if eff.is_alive:
        eff.draw()
    
if __name__ == "__main__":
    pyxel.init(80,80)
    pyxel.load("sample.pyxres")
    eff = BlastLarge(20,20,15)
    
    pyxel.run(update,draw)
