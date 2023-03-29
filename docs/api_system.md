# Pyxel API sample

システム，リソース，入力  
バージョン：Pyxel 1.9版  
  
## contents


| 分類 | 項目 |
|:---:|:---|
|[システム](api_system.md#システム)| [変数](api_system.md#variable) [init()](api_system.md#init) [run()](api_system.md#run) [show()](api_system.md#show) [flip()](api_system.md#flip) [quit()](api_system.md#quit)|
|[リソース](api_system.md#リソース)| [load()](api_system.md#load)  |
|[入力](api_system.md#入力)| [変数](api_system.md#variable-1) [btn()](api_system.md#btn) [btnp()](api_system.md#btnp) [btnr()](api_system.md#btnr) [mouse()](api_system.md#mouse) [キー記述例](api_system.md#keycode) |  
|[グラフィックス](api_graphics.md#グラフィックス)| [変数](api_graphics.md#variable) [image()](api_graphics.md#image) [tilemap()](api_graphics.md#tilemap) [clip()](api_graphics.md#clip) [camera()](api_graphics.md#camera) [pal()](api_graphics.md#pal) [cls()](api_graphics.md#cls) [pget()](api_graphics.md#pget) [pset()](api_graphics.md#pset) <br> [line()](api_graphics.md#line) [rect()](api_graphics.md#rect) [rectb()](api_graphics.md#rectb) [circ()](api_graphics.md#circ) [circb()](api_graphics.md#circb) [elli()](api_graphics.md#elli) [ellib()](api_graphics.md#ellib) [tri()](api_graphics.md#tri) [trib()](api_graphics.md#trib) <br> [fill()](api_graphics.md#fill) [blt()](api_graphics.md#blt) [bltm()](api_graphics.md#bltm) [text()](api_graphics.md#text) [表示色](api_graphics.md#color) |
|[イメージクラス](api_graphics.md#イメージクラス)| [変数](api_graphics.md#variable-1) [set()](api_graphics.md#set) [load()](api_graphics.md#load) [save()](api_graphics.md#save) [pget()](api_graphics.md#pget-1) [pset()](api_graphics.md#pset-1) |
|[タイルマップクラス](api_graphics.md#タイルマップクラス)| [変数](api_graphics.md#variable-2)  [set()](api_graphics.md#set-1) [pget()](api_graphics.md#pget-2) [pset()](api_graphics.md#pset-2) |
|[オーディオ](api_audio.md#オーディオ)| [sound()](api_audio.md#sound) [music()](api_audio.md#music) [play_pos()](api_audio.md#play_pos) [play()](api_audio.md#play) [playm()](api_audio.md#playm) [stop()](api_audio.md#stop) |
|[サウンドクラス](api_audio.md#サウンドクラス)| [変数](api_audio.md#variable) [set()](api_audio.md#set) [set_notes()](api_audio.md#set_notes) [set_tones()](api_audio.md#set_tones) [set_volumes()](api_audio.md#set_volumes) [set_effects()](api_audio.md#set_effects) |
|[ミュージッククラス](api_audio.md#ミュージッククラス)| [変数](api_audio.md#variable-1) [set()](api_audio.md#set-1) |
|[数学](api_math.md#pyxel-api-sample)| [ceil()](api_math.md#ceil) [floor()](api_math.md#floor) [sgn()](api_math.md#sgn) [sqrt()](api_math.md#sqrt) [sin()](api_math.md#sin) [cos()](api_math.md#cos) [atan2()](api_math.md#atan2) [rseed()](api_math.md#rseed) [rndi()](api_math.md#rndi) [rndf()](api_math.md#rndf) [nseed()](api_math.md#nseed) [noise()](api_math.md#noise) |


<br>


- [Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。  

<br>

- 下記import文でPyxelをインポートしたときのAPIの呼び出し記述になります。  
``` python
import pyxel
```
<br>

- 説明中の「型」は数値や文字列の種別を示しています。  

| 型 | 内容 |
|:---:|:---|
| i32 | 符号付き整数型（負の値あり） |
| u8 <br> u32 | 符号なし整数型（負の値なし） |
| f64 | 浮動小数点数（小数の値） |
| str | 文字列 |
| bool | True/False |  
<br>

- コード例で使用しているリソースファイル（[sample.pyxres](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/assets/sample.pyxres)）は公式サイトからDownloadできます。


<br>


## システム  
<br>  

### variable  

|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| width | u32 | 画面の幅 | `pyxel.width` |
| height | u32 | 画面の高さ | `pyxel.height` |
| frame_count | u32 | 経過フレーム数 | `pyxel.frame_count` |  
<br>

``` python
sw = pyxel.width
sh = pyxel.height
print("width=",sw,"height=",sh)     # print文はIDLEシェル等への出力でデバッグに利用できます
```

``` python
pyxel.text(10, 10, "Hello, Pyxel!", pyxel.frame_count % 16)
```

<br>

### init()  
  Pyxel アプリケーションを初期化します。  
  `init(width, height, [title], [fps], [quit_key], [display_scale], [capture_scale], [capture_sec])`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| width | u32 | 画面の幅 |
| height | u32 | 画面の高さ |
| title | str | ウィンドウタイトル |
| fps | u32 | 動作フレームレート |
| quit_key | u32 | アプリケーション終了キー（[キー記述例](api_system.md#keycode)） |
| display_scale | u32 | 画面表示の倍率 |
| capture_scale | u32 | 画面キャプチャの倍率 |
| capture_sec | u32 | 画面キャプチャ動画の最大録画時間 |  

<br>
 
・アプリケーション初期化 画面サイズとタイトル指定
``` python
pyxel.init(240, 160, title="Pyxel App")
```  
・アプリケーション初期化 動作フレームレート60fps，終了キー（なし）に指定  
``` python
pyxel.init(240, 160, title="Pyxel App", fps=60, quit_key=pyxel.KEY_NONE)
```  
・画面表示の倍率，画面キャプチャの倍率，画面キャプチャ動画の録画時間指定  
``` python
pyxel.init(128, 64, display_scale=5,capture_scale=5,capture_sec=10)
```  
<br>

### run()  
  Pyxel アプリケーションを開始、フレーム更新時にupdate関数、描画時にdraw関数を呼びます。  
  `run(update, draw)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| update | 関数 | 更新時に実行する関数名を指定 |
| draw | 関数 | 描画時に実行する関数名を指定 |

<br>

``` python
import pyxel
pyxel.init(64, 64)

def update():
    return

def draw():
    pyxel.cls(0)
    return

pyxel.run(update, draw)
```

<br>  

### show()  
  画面を表示してEscキーが押されるまで待機  
``` python
import pyxel
pyxel.init(64, 64)
pyxel.text(10, 10, "Test", 7)
pyxel.show()
```

<br>

### flip()  
  画面を 1 フレーム更新（Webでは使用不可）
``` python
import pyxel
pyxel.init(64, 64)
while(True):
    pyxel.cls(0)
    pyxel.text(10,10, "Test", pyxel.frame_count % 16)
    pyxel.flip()
```

<br>  

### quit()  
  Pyxel アプリケーションを終了
``` python
def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    return
```


[ページの先頭に戻る](#pyxel-api-sample)　


## リソース

<br>  

### load()  
  リソースファイル (.pyxres) を読み込みます。  
  `load(filename, [image], [tilemap], [sound], [music])`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| filename | str | リソースファイルのパス |
| image | bool | イメージバンクを読み込まない場合 False を指定 |
| tilemap | bool | タイルマップを読み込まない場合 False を指定 |
| sound | bool | サウンドを読み込まない場合 False を指定 |
| music | bool | ミュージックを読み込まない場合 False を指定 |

<br>

・同じフォルダにある sample.pyxres を読み込む例
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.blt(16,8, 0, 8,0, 8,8, 0)
    return

pyxel.run(update, draw)
```
・リソースタイプ (image/tilemap/sound/music) にFalseを指定すると，そのリソースは読み込まれない。
``` python
# image   True
# tilemap False
# sound   True
# music   True の例
pyxel.load("sample.pyxres",True,False)
```


[ページの先頭に戻る](#pyxel-api-sample)　


## 入力
<br>


### variable  


|変数名| 型 |説明|記述例|
|:---:|:---:|:---|:---|
| mouse_x | i32 | 現在のマウスカーソルx座標 | `pyxel.mouse_x` |  
| mouse_y | i32 | 現在のマウスカーソルy座標 | `pyxel.mouse_y` |  
| mouse_wheel | i32 | 現在のマウスホイールの値 | `pyxel.mouse_wheel` |  
  
※Pyxel Web では mouse_x,mouse_y でスマホタッチ位置を取得可

<br>

``` python
import pyxel
pyxel.init(64, 64)
pyxel.mouse(True) # マウスカーソル表示指定(表示無しでも座標は取得可能)

def update():
    # update()内で座標判定処理などに使う例
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(pyxel.mouse_x)+","+str(pyxel.mouse_y),7)
    return

pyxel.run(update, draw)
```
 
``` python
import pyxel
pyxel.init(64, 64)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(pyxel.mouse_wheel),7)
    return

pyxel.run(update, draw)
```

<br>  

###  btn() 
  keyが押されていたらTrue、押されていなければFalseを返します。  
  `btn(key) `  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| key | u32 | 判定するキー（[キー記述例](api_system.md#keycode)） |  
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| キー状態 | bool | 押している間 True |  


<br>

``` python
import pyxel
pyxel.init(64, 64)

flg = False
def update():
    global flg
    if pyxel.btn(pyxel.KEY_SPACE):
        # キーが押されているときの処理
        flg = True
    else:
        # キーが押されていないときの処理
        flg = False
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(flg),7)
    return

pyxel.run(update, draw)
```

<br>

### btnp()  
  そのフレームにkeyが押されたらTrue、押されなければFalseを返します。holdとrepeatを指定すると、holdフレーム以上ボタンを押し続けた時にrepeatフレーム間隔でTrueが返ります。  
  `btnp(key, [hold], [repeat]) `  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| key | u32 | 判定するキー（[キー記述例](api_system.md#keycode)） |  
| hold | u32 | 押し続け判定フレーム数 |
| repeat | u32 | Trueを返すフレーム間隔 |
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| キー状態 | bool | 押した最初の瞬間だけTrue<br>holdとrepeatを指定するとSTGなどで押し続けて連射ができる |  

<br>

``` python
import pyxel
pyxel.init(64, 64)

cnt = 0
def update():
    global cnt
    if pyxel.btnp(pyxel.KEY_SPACE) :
        cnt += 1
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(cnt),7)
    return

pyxel.run(update, draw)
```

``` python
import pyxel
pyxel.init(64, 64)

cnt = 0
def update():
    global cnt
    if pyxel.btnp(pyxel.KEY_SPACE,15,15) :
        cnt += 1
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(cnt),7)
    return

pyxel.run(update, draw)
```

<br>

### btnr()  
  そのフレームにkeyが離されたらTrue、離されなければFalseを返します。  
  `btnr(key)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| key | 定義値 | 判定するキー（[キー記述例](api_system.md#keycode)） |  
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| キー状態 | bool | 押している間 False , 押されたキーが離されたら True <br>押す前（通常状態）は False　|  


<br>

``` python
import pyxel
pyxel.init(64, 64)

cnt = 0
def update():
    global cnt
    if pyxel.btnr(pyxel.KEY_SPACE) :
        cnt += 1
    return

def draw():
    pyxel.cls(0)
    pyxel.text(4,4, str(cnt),7)
    return

pyxel.run(update, draw)
```

<br>

### mouse()  
  visibleがTrueならマウスカーソルを表示し、Falseなら非表示にします。マウスカーソルが非表示でも座標は更新されます。  
  `mouse(visible)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| visible | bool | 表示させる場合 True |  

<br>

``` python
pyxel.mouse(True)    # 以降False指定されるまで表示
```
  
<br>
  

## Keycode  

  Keycodeの定義値です。　(詳細は[キー定義一覧](https://github.com/kitao/pyxel/blob/main/python/pyxel/__init__.pyi)参照)  


| コード例 | キー |
|:---|:---|
| pyxel.KEY_SPACE | スペースキー |
| pyxel.KEY_RETURN | Enterキー |
| pyxel.KEY_0 | 数字キー 0 |
| pyxel.KEY_A | 文字キー A |
| pyxel.KEY_UP | 上方向キー |
| pyxel.KEY_DOWN | 下方向キー |
| pyxel.KEY_LEFT | 左方向キー |
| pyxel.KEY_RIGHT | 右方向キー |
| pyxel.MOUSE_BUTTON_LEFT | マウス左ボタン<br>スマホ画面タップ(Web) |
| pyxel.MOUSE_BUTTON_RIGHT | マウス右ボタン |
| pyxel.KEY_KP_1 | テンキー数字 1 |
| pyxel.KEY_KP_ENTER | テンキーEnterキー |
| pyxel.GAMEPAD1_BUTTON_DPAD_UP | バーチャルゲームパッド上 |
| pyxel.GAMEPAD1_BUTTON_DPAD_DOWN | バーチャルゲームパッド下 |
| pyxel.GAMEPAD1_BUTTON_DPAD_LEFT | バーチャルゲームパッド左 |
| pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT | バーチャルゲームパッド右 |
| pyxel.GAMEPAD1_BUTTON_A | バーチャルゲームパッドA | 
| pyxel.GAMEPAD1_BUTTON_B | バーチャルゲームパッドB |
| pyxel.GAMEPAD1_BUTTON_X | バーチャルゲームパッドX |
| pyxel.GAMEPAD1_BUTTON_Y | バーチャルゲームパッドY |
  
  
<br>

[ページの先頭に戻る](#pyxel-api-sample)　　[TOPに戻る](../README.md#pyxel-game-development)
