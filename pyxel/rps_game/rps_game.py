import pyxel

pyxel.init(80,64,title="rock paper scissors",capture_scale=3,capture_sec=10)
pyxel.load("rps_game.pyxres")
pyxel.mouse(True)

com_hand = 0
player_hand = 0
status = 0
# result[ player ][ cpu ]  0:draw 1:p win 2:p lose
result = [[0,1,2],
          [2,0,1],
          [1,2,0]]
message = ["DRAW","WIN","LOSE"]

def check_area():
    ret = False
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    if 16 <= x and x < 64 and 32 <= y and y < 48:
        ret = True
    return ret

def update():
    global com_hand, status, player_hand
    if status == 0:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and check_area():
            player_hand = int(pyxel.mouse_x / 16) - 1
            com_hand = pyxel.rndi(0,2)
            idx = result[player_hand][com_hand]
            pyxel.play(0,idx)
            status = 1
        else:
            # クリック前は次々手を変える
            com_hand = int(pyxel.frame_count / 5) % 3
    elif status == 1:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            status = 0
    
    return

def draw():
    pyxel.cls(0)

    # コンピューターの手を描画
    pyxel.text(4,10, "COM",7)
    pyxel.blt(32,10, 0, com_hand*16,0, 16,16, 0)

    # プレーヤーの手を描画
    pyxel.text(4,32, "YOU",7)
    if status == 0:
        pyxel.blt(16,32, 0,  0,0, 16,16, 0)
        pyxel.blt(32,32, 0, 16,0, 16,16, 0)
        pyxel.blt(48,32, 0, 32,0, 16,16, 0)
    elif status == 1:
        pyxel.blt(16*(player_hand+1),32, 0, 16*player_hand,0, 16,16, 0)
        idx = result[player_hand][com_hand]
        pyxel.text(16*(player_hand+1),48, message[idx],7)
    
    return

pyxel.run(update, draw)
