import pyxel

pyxel.init(128,128)
pyxel.load("penguin.pyxres")                # イメージバンク0にタイルマップ
pyxel.image(2).load(0, 0, "penguin.png")    # イメージバンク2に画像ファイル
pyxel.colors[3] = 0x19C5FA                  # 背景塗りつぶしに使う薄い青色

# シーン番号の定義
SNO_TITLE    = 0
SNO_STAGESET = 10
SNO_PLAY     = 11
SNO_SFINISH  = 12
SNO_GAMEOVER = 13
SNO_END      = 20

LEFT_BORDER = 40
RIGHT_BORDER = pyxel.width - 48

scroll_x = 0
scroll_y = 0
x = 8
y = 100
dx = 0
dy = 0
pldir = 1
jump = 0
score = 0
score_tmp = 0

scene = SNO_TITLE   # ゲームの進行を管理する変数
tmr = 0             # シーン内でカウントするタイマー変数
# ステージデータ 下記タプルのリスト
#               0 タイルマップ番号(0-7)
#               1 ステージ左上 x座標
#               2 ステージ左上 y座標
#               3 ステージ幅
#               4 ステージ高さ
stagedata = [(0, 0,    0, 128*1,128),
             (0, 0,128*2, 128*2,128),
             (1, 0,    0, 128*3,128)]

stage = 0   # 現在のステージ番号（ステージデータ配列のインデックス）
stage_tm = 0    # タイルマップ番号
stage_x = 0
stage_y = 0
stage_width = 0
stage_height = 0
item_list = []  # アイテム復帰用リスト

chkpoint = [(2,0),(6,0),(1,7),(6,7)]
def chkwall(cx,cy):
    c = 0
    if cx < stage_x or stage_width -8 < cx:
        c = c + 1
    if stage_height -8 < cy: # 画面下に行かない設定
        c = c + 1
    for cpx,cpy in chkpoint:
        xi = (cx + cpx)//8
        yi = (cy + cpy)//8
        if (1,0) == pyxel.tilemap(stage_tm).pget(xi,yi):
            c = c + 1
    return c

def restore_tile():
    global item_list
    # 得点アイテムタイルを復帰
    for xi,yi,tile in item_list:
        pyxel.tilemap(stage_tm).pset(xi,yi,tile)
    item_list.clear()  # リストを空にする
    return

def setstage():
    global x,y,scroll_x,scroll_y,stage_tm,stage_x,stage_y,stage_width,stage_height,score_tmp

    stage_tm = stagedata[stage][0]
    scroll_x = stagedata[stage][1]
    scroll_y = stagedata[stage][2]
    x = scroll_x + 8
    y = scroll_y + 100
    stage_x = scroll_x
    stage_y = scroll_y
    stage_width = scroll_x + stagedata[stage][3]
    stage_height = scroll_y + stagedata[stage][4]
    score_tmp = 0
    return

def initgame():
    global score,stage,scroll_x,scroll_y,item_list
    score = 0
    stage = 0
    scroll_x = 0
    scroll_y = 0
    item_list.clear()  # リストを空にする
    return

def moveplayer():
    global scroll_x,scroll_y,x,y,dx,dy,pldir,jump,score_tmp,item_list

    ret = SNO_PLAY         # 戻り値でシーン切り替えを行う

    # 操作判定
    if pyxel.btn(pyxel.KEY_LEFT):
        if -3 < dx:
            dx = dx - 1
        pldir = -1
    elif pyxel.btn(pyxel.KEY_RIGHT):
        if dx < 3:
            dx = dx + 1
        pldir = 1
    else:
        dx = int(dx*0.7)

    # 横方向の移動
    lr = pyxel.sgn(dx)
    loop = abs(dx)
    while 0 < loop :
        if chkwall( x + lr, y) != 0:
            dx = 0
            break
        x = x + lr
        loop = loop -1

    # 左方向へのスクロール
    if x < scroll_x + LEFT_BORDER:
        scroll_x = x - LEFT_BORDER
        if scroll_x < stage_x:
            scroll_x = stage_x

    # 右方向へのスクロール
    if scroll_x + RIGHT_BORDER < x:
        scroll_x = x - RIGHT_BORDER
        if stage_width - pyxel.width < scroll_x:
            scroll_x = stage_width - pyxel.width

    # ジャンプと落下
    if jump == 0:
        if chkwall(x,y+1) == 0:
            jump = 2  # 床が無ければ落下
        if pyxel.btnp(pyxel.KEY_SPACE):
            dy = 8
            jump = 1   # ジャンプ開始
    else:
        dy = dy - 1
        if dy < 0:
            jump = 2    # 頂点で落下開始

    ud = pyxel.sgn(dy)
    loop = abs(dy)
    while 0 < loop :
        if chkwall(x, y - ud) != 0:
            dy = 0
            if jump == 1:
                jump = 2   # 壁にぶつかって落下
            elif jump == 2:
                jump = 0   # 着地　落下終了
            break
        y = y - ud
        loop = loop -1

    # 上方向へのスクロール  本記事では追加しない
    # 下方向へのスクロール  本記事では追加しない

    # タイルマップ判定
    # コイン判定をキャラクター四隅で行うように変更
    for cpx,cpy in chkpoint:
        xi = (x + cpx)//8
        yi = (y + cpy)//8
        tile = pyxel.tilemap(stage_tm).pget(xi,yi)
        if (1,1) == tile :   # 得点アイテム
            score_tmp += 1
            pyxel.tilemap(stage_tm).pset(xi,yi,(0,0))
            item_list.append((xi,yi,tile)) # 消したアイテムを記録

    xi = (x + 4)//8
    yi = (y + 4)//8
    tile = pyxel.tilemap(stage_tm).pget(xi,yi)
    if (2,1) == tile:   # ゴール
        ret = SNO_SFINISH

    if (2,0) == tile or (3,0) == tile:    # NGタイル
        ret = SNO_GAMEOVER

    return ret

def update():
    global scene,tmr,stage,score
    tmr = tmr + 1           # タイマー変数更新
    
    if scene == SNO_TITLE:
        if tmr == 1:
            initgame() # 初期化処理

        if pyxel.btnp(pyxel.KEY_SPACE):
            scene = SNO_STAGESET
            tmr = 0

    elif scene == SNO_STAGESET:
        if tmr == 1:
            setstage() # ステージ初期化
            scene = SNO_PLAY
            tmr = 0

    elif scene == SNO_PLAY:
        # キャラクター操作
        scene = moveplayer()
        if scene != SNO_PLAY :
            tmr = 0
        # シーン変更確認用コードは削除

    elif scene == SNO_SFINISH:
        # 3秒経過後にステージ更新(1秒30フレームなので3倍待つ)
        if 30*3 < tmr :
            restore_tile()  # クリアステージのアイテム復帰
            stage += 1      # 次のステージに変更
            score += score_tmp
            if stage < len(stagedata):
                scene = SNO_STAGESET
                tmr = 0
            else:
                scene = SNO_END
                tmr = 0
                
    elif scene == SNO_GAMEOVER:
        # リトライ確認
        if pyxel.btnp(pyxel.KEY_Y):
            restore_tile()  # ステージのアイテム復帰
            scene = SNO_STAGESET
            tmr = 0
        if pyxel.btnp(pyxel.KEY_N):
            restore_tile()  # ステージのアイテム復帰
            scene = SNO_TITLE
            tmr = 0
           
    else:
        # ゲームクリア画面
        if pyxel.btnp(pyxel.KEY_SPACE):
            scene = SNO_TITLE
            tmr = 0
        
    return

def dispmsg(tx,ty,msg,col):
    # 画面スクロールに合わせて座標を変更して描画する
    pyxel.text(scroll_x+tx,scroll_y+ty,msg,col)
    return

def blinkmsg(tx,ty,msg,col):
    # メッセージを点滅表示(タイマー変数を40で割った余りは0～39を繰り返す)
    if tmr%40 < 20:
        dispmsg(tx,ty,msg,col)
    return

def draw():
    pyxel.cls(3)
    pyxel.camera()

    if scene == SNO_TITLE:
        # タイトル用の画像を表示
        pyxel.blt(0,0, 2, 0,0, 128,128,0)
        blinkmsg(20,100,"Press SPACE to Start.",7)

    elif scene == SNO_PLAY or scene == SNO_SFINISH or scene == SNO_GAMEOVER:
        # リソースファイルのタイルマップを表示
        pyxel.bltm(0,0,
                   stage_tm,
                   scroll_x,scroll_y,
                   pyxel.width,pyxel.height, 0)
        # プレイヤーを表示
        pyxel.camera(scroll_x,scroll_y)
        pyxel.blt( x, y, 0,  0, 8, pldir*8,8, 3)
        # 点数表示
        dispmsg(1,1,"SCORE:"+str(score+score_tmp),7)
    
    elif scene == SNO_END:
        # エンド用の画像を表示
        pyxel.blt(0,0, 2, 0,128, 128,128,0)
        pyxel.text(1,1,"SCORE:"+str(score),7)

    if scene == SNO_SFINISH:
        blinkmsg(35,56,"Clear a stage.",7)   
    elif scene == SNO_GAMEOVER:
        pyxel.rect(scroll_x+25,scroll_y+40, 78,30, 0)
        dispmsg(46,45,"GAME OVER",7)
        dispmsg(35,60,"Retry? [Y]or[N]",7)
    
    return

pyxel.run(update,draw)

