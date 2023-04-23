import pyxel

effects = []

class Hit:

    def __init__(self,x,y) -> None:
        self.x = x-8
        self.y = y-8
        self.w = 16
        self.h = 16
        self.cnt = 10
        self.is_alive = True
        effects.append(self)
    
    def update(self):
        self.cnt -= 1
        if self.cnt <= 0:
            self.is_alive = False
    
    def draw(self):
        pyxel.blt(self.x,self.y,0, 0,176, self.w,self.h, 0)


