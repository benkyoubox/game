# Pyxel API sample

グラフィックス，イメージクラス，タイルマップクラス  
バージョン：Pyxel 1.9版  
  
## contents


| 分類 | 項目 |
|:---:|:---|
|[システム](api_system.md#システム)| [変数](api_system.md#variable) [init()](api_system.md#init) [run()](api_system.md#run) [show()](api_system.md#show) [flip()](api_system.md#flip) [quit()](api_system.md#quit)|
|[リソース](api_system.md#リソース)| [load()](api_system.md#load)  |
|[入力](api_system.md#入力)| [変数](api_system.md#variable-1) [btn()](api_system.md#btn) [btnp()](api_system.md#btnp) [btnr()](api_system.md#btnr) [mouse()](api_system.md#mouse) [キー記述例](api_system.md#keycode) |  
|[グラフィックス](api_graphics.md#グラフィックス)| [変数](api_graphics.md#variable) [image()](api_graphics.md#image) [tilemap()](api_graphics.md#tilemap) [clip()](api_graphics.md#clip) [camera()](api_graphics.md#camera) [pal()](api_graphics.md#pal) [cls()](api_graphics.md#cls) [pget()](api_graphics.md#pget) [pset()](api_graphics.md#pset) <br> [line()](api_graphics.md#line) [rect()](api_graphics.md#rect) [rectb()](api_graphics.md#rectb) [circ()](api_graphics.md#circ) [circb()](api_graphics.md#circb) [elli()](api_graphics.md#elli) [ellib()](api_graphics.md#ellib) [tri()](api_graphics.md#tri) [trib()](api_graphics.md#trib) <br> [fill()](api_graphics.md#fill) [blt()](api_graphics.md#blt) [bltm()](api_graphics.md#bltm) [text()](api_graphics.md#text) |
|[イメージクラス](api_graphics.md#イメージクラス)| [変数](api_graphics.md#variable-1) [set()](api_graphics.md#set) [load()](api_graphics.md#load) [pget()](api_graphics.md#pget-1) [pset()](api_graphics.md#pset-1) |
|[タイルマップクラス](api_graphics.md#タイルマップクラス)| [変数](api_graphics.md#variable-2)  [set()](api_graphics.md#set-1) [pget()](api_graphics.md#pget-2) [pset()](api_graphics.md#pset-2) |
|[オーディオ](api_audio.md#オーディオ)| [sound()](api_audio.md#sound) [music()](api_audio.md#music) [play_pos()](api_audio.md#play_pos) [play()](api_audio.md#play) [playm()](api_audio.md#playm) [stop()](api_audio.md#stop) |
|[サウンドクラス](api_audio.md#サウンドクラス)| [変数](api_audio.md#variable) [set()](api_audio.md#set) [set_notes()](api_audio.md#set_notes) [set_tones()](api_audio.md#set_tones) [set_volumes()](api_audio.md#set_volumes) [set_effects()](api_audio.md#set_effects) |
|[ミュージッククラス](api_audio.md#ミュージッククラス)| [変数](api_audio.md#variable-1) [set()](api_audio.md#set-1) |
|[数学](api_math.md#pyxel-api-sample)| [ceil()](api_math.md#ceil) [floor()](api_math.md#floor) [sgn()](api_math.md#sgn) [sin()](api_math.md#sin) [cos()](api_math.md#cos) [atan2()](api_math.md#atan2) [rseed()](api_math.md#rseed) [rndi()](api_math.md#rndi) [rndf()](api_math.md#rndf) [nseed()](api_math.md#nseed) [noise()](api_math.md#noise) |


<br>
  
[Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。 
（公式サンプルは[03_draw_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/03_draw_api.py)を参照してください）  

※下記import文でPyxelをインポートしたときのAPIの呼び出し記述になります。
``` python
import pyxel
```
  
## グラフィックス  
<br>  


### variable  


|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| colors | リスト | パレットの表示色リスト。<br>表示色は 24 ビット数値(0x000000-0xffffff)で指定します。 | pyxel.colors |  

<br>

``` python
pyxel.colors[3] = 0x19C5FA    # 表示色3を薄い青色に変更
pyxel.cls(3)
```
・Python リストを直接代入、取得する場合はcolors.from_listとcolors.to_listを使用してください。
``` python
# デフォルトのカラーパレットを退避
org_colors = pyxel.colors.to_list()

# デフォルトのカラーパレットで復帰
pyxel.colors.from_list(org_colors)
```

<br>  

### image()
  イメージバンクimg (0-2) を操作します。([イメージクラス](#イメージクラス)を参照のこと)  
  `image(img)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| img | u32 | 操作対象のイメージバンク (0-2) |

<br>
  
### tilemap()  
  タイルマップtm (0-7) を操作します。([タイルマップクラス](#タイルマップクラス)を参照のこと)  
  `tilemap(tm)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| tm | u32 | 操作対象のタイルマップ (0-7) |

<br>

### clip()  
  画面の描画領域を (x, y) から幅w、高さhに設定します。clip()で描画領域を全画面にリセットします。    
  `clip(x, y, w, h)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | 左上座標 |
| y | f64 | 左上座標 |
| w | f64 | 幅 |
| h | f64 | 高さ |

<br>

``` python
import pyxel
pyxel.init(64, 64)
pyxel.mouse(True)

def update():
    return

def draw():
    pyxel.cls(1)
    pyxel.rectb(2,2,60,60,10)
    pyxel.text(8,28,"Hello world!",7)
    pyxel.clip(pyxel.mouse_x,pyxel.mouse_y, 32,32)
    return

pyxel.run(update, draw)
```
![image clip](images/api/g_clip.gif)  
<br>
  
### camera()  
  画面の左上隅の座標を (x, y) に変更します。camera()で左上隅の座標を (0, 0) にリセットします。  
  `camera(x, y)`

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | 左上座標 |
| y | f64 | 左上座標 | 

<br>

``` python
import pyxel
pyxel.init(64, 64)

def update():
    return

def draw():
    pyxel.cls(1)
    pyxel.camera(-5,-5)
    pyxel.rectb(2,2,60,60,10)
    pyxel.text(8,28,"Hello world!",7)
    return

pyxel.run(update, draw)
```
<br>
  
### pal()  
  描画時に色col1をcol2に置き換えます。pal()で初期状態にリセットします。  
  `pal(col1, col2)`

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| col1 | u8 | 置き換え対象の色 (0-15) |  
| col2 | u8 | 置き換える色 (0-15) |  

<br>

``` python
import pyxel
pyxel.init(64, 64)

toggle = 0
def update():
    global toggle
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        toggle = 1 - toggle
    return

def draw():
    pyxel.cls(1)
    pyxel.rectb(2,2,60,60,10)
    pyxel.text(8,28,"Hello world!",7)
    if toggle:
        pyxel.pal(1,7)
        pyxel.pal(7,1)
    else:
        pyxel.pal()
    return

pyxel.run(update, draw)
```
![image pal](images/api/g_pal.gif)   
<br>
  
### cls()  
  画面を色colでクリアします。  
  `cls(col)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| col | u8 | 画面を塗りつぶす色 (0-15) |  

<br>

``` python
pyxel.cls(0)
```
<br>
  
### pget()  
  (x, y) のピクセルの色を取得します。  
  `pget(x, y)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | x座標 |  
| y | f64 | y座標 |  

<br>

``` python
import pyxel
pyxel.init(64, 64)

col = 0
def update():
    global col
    col = pyxel.pget(pyxel.mouse_x, pyxel.mouse_y)
    return

def draw():
    pyxel.cls(1)
    for i in range(16):
        pyxel.rect(4*i,0,4,40,i)
    pyxel.text(8,48,"col="+str(col),7)
    return

pyxel.run(update, draw)
```
![image pget](images/api/g_pget.png)  
<br>
  
### pset()  
  (x, y) に色colのピクセルを描画します。  
  `pset(x, y, col)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | x座標 |  
| y | f64 | y座標 |  
| col | u8 | 描画色 (0-15) |  

<br>

``` python
import pyxel
pyxel.init(64, 64)

def update():
    return

def draw():
    #pyxel.cls(0)
    pyxel.pset(pyxel.mouse_x, pyxel.mouse_y,pyxel.rndi(1,15))
    return

pyxel.run(update, draw)
```
![image pset](images/api/g_pset.png)  
<br>

### line()  
  色colの直線を (x1, y1)-(x2, y2) に描画します。  
  `line(x1, y1, x2, y2, col)`  

### rect()  
  幅w、高さh、色colの矩形を (x, y) に描画します。※矩形（くけい）は長方形  
  `rect(x, y, w, h, col)`  

### rectb()  
  幅w、高さh、色colの矩形の輪郭線を (x, y) に描画します。  
  `rectb(x, y, w, h, col)`  

### circ()  
  半径r、色colの円を (x, y) に描画します。  
  `circ(x, y, r, col)`  

### circb()  
  半径r、色colの円の輪郭線を (x, y) に描画します。  
  `circb(x, y, r, col)`  

### elli()  
  幅w、高さh、色colの楕円を (x, y) に描画します。  
  `elli(x, y, w, h, col)`  

### ellib()  
  幅w、高さh、色colの楕円の輪郭線を (x, y) に描画します。  
  `ellib(x, y, w, h, col)`  

### tri()  
  頂点が (x1, y1)、(x2, y2)、(x3, y3)、色colの三角形を描画します。  
  `tri(x1, y1, x2, y2, x3, y3, col)`  

### trib()  
  頂点が (x1, y1)、(x2, y2)、(x3, y3)、色colの三角形の輪郭線を描画します。  
  `trib(x1, y1, x2, y2, x3, y3, col)`  
  
``` python
import pyxel
pyxel.init(128, 128)

def update():
    return

def draw():
    pyxel.cls(0)
    # 線
    pyxel.line(4,4, 64,4, 3)
    # 長方形
    pyxel.rect(2,8, 24,16, 4)
    pyxel.rectb(42,8, 24,16, 5)
    # 円
    pyxel.circ(12,38, 8, 6)
    pyxel.circb(50,38, 8, 7)
    # 楕円
    pyxel.elli(2,54, 24,16, 8)
    pyxel.ellib(42,54, 24,16, 9)
    # 三角形
    pyxel.tri(2,100, 22,100, 12,80, 10)
    pyxel.trib(42,100, 62,100, 52,80, 11)
    return

pyxel.run(update, draw)
```
<br>
  
### fill()  
  (x, y) と同じ色でつながっている領域を色colで塗りつぶします。  
  `fill(x, y, col)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | x座標 |  
| y | f64 | y座標 |  
| col | u8 | 塗りつぶし色 (0-15) |  

<br>


``` python
import pyxel
pyxel.init(64, 64)
pyxel.mouse(True)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.rectb(2,2, 50,50, 7)
    pyxel.circb(40,20, 18, 7)
    pyxel.tri(10,60, 60,60, 60,40, 7)
    pyxel.fill(pyxel.mouse_x, pyxel.mouse_y, 10)
    return

pyxel.run(update, draw)
```
![image fill](images/api/g_fill.gif)   

<br>
 
### blt()  
  イメージバンクimg (0-2) の (u, v) からサイズ (w, h) の領域を (x, y) にコピーします。w、hそれぞれに負の値を設定すると水平、垂直方向に反転します。colkeyに色を指定すると透明色として扱われます。  
  `blt(x, y, img, u, v, w, h, [colkey])`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | 描画先のx座標 |  
| y | f64 | 描画先のy座標 |  
| img | u32 | イメージバンク (0-2) |  
| u | f64 | ドット絵の座標 |  
| v | f64 | ドット絵の座標 |  
| w | f64 | ドット絵の幅（マイナスで左右反転） |  
| h | f64 | ドット絵の高さ（マイナスで上下反転） |  
| colkey | u8 | 透明色 (0-15) |  

<br>

``` python
import pyxel
pyxel.init(42, 12)
pyxel.load("sample.pyxres")

def update():
    return

def draw():
    pyxel.cls(3)
    pyxel.blt(2,2, 0, 8,0, 8,8)
    pyxel.blt(12,2, 0, 8,0, 8,8, 0)
    pyxel.blt(22,2, 0, 8,0, -8,8, 0)
    pyxel.blt(32,2, 0, 8,0, 8,-8, 0)
    return

pyxel.run(update, draw)
```
![image blt](images/api/g_blt.png)  
<br>
  
### bltm()  
  タイルマップtm (0-7) の (u, v) からサイズ (w, h) の領域を (x, y) にコピーします。w、hそれぞれに負の値を設定すると水平、垂直方向に反転します。colkeyに色を指定すると透明色として扱われます。1 タイルのサイズは 8x8 ピクセルで、(tile_x, tile_y)のタプルとしてタイルマップに格納されています。  
  `bltm(x, y, tm, u, v, w, h, [colkey])`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | 描画先のx座標 |  
| y | f64 | 描画先のy座標 |  
| tm | u32 | タイルマップ (0-7) |  
| u | f64 | タイルマップの座標 |  
| v | f64 | タイルマップの座標 |  
| w | f64 | タイルマップの幅（マイナスで左右反転） |  
| h | f64 | タイルマップ高さ（マイナスで上下反転） |  
| colkey | u8 | 透明色 (0-15) | 

<br>

``` python
pyxel.bltm(0,0, 0, 0,0, 128,128, 0)
```
``` python
pyxel.camera()
pyxel.bltm(0,0, 0, self.scroll_x,self.scroll_y, pyxel.width,pyxel.height, 0)
pyxel.camera(self.scroll_x,self.scroll_y)
```
``` python
import pyxel
pyxel.init(42, 12)
pyxel.load("sample.pyxres")

def update():
    return

def draw():
    pyxel.cls(3)
    pyxel.bltm(2,2, 0, 8,0, 8,8)
    pyxel.bltm(12,2, 0, 8,0, 8,8, 0)
    pyxel.bltm(22,2, 0, 8,0, -8,8, 0)
    pyxel.bltm(32,2, 0, 8,0, 8,-8, 0)
    return

pyxel.run(update, draw)
```
<br>
  
### text()  
  色colの文字列sを (x, y) に描画します。  
  `text(x, y, s, col)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | 描画先のx座標 |  
| y | f64 | 描画先のy座標 | 
| s | str | 文字列（半角英数） |
| col | u8 | 文字色 (0-15) |  

<br>


``` python
pyxel.text(4, 4, "Hello, Pyxel!", pyxel.frame_count % 16)
```

<br>

[ページの先頭に戻る](#pyxel-api-sample)　


## イメージクラス
<br>


### variable  


|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| width | u32 | イメージの幅 | `pyxel.image(0).width` |
| height | u32 | イメージの高さ | `pyxel.image(0).height` |
<br>

``` python
print(pyxel.image(0).width)   # 256
print(pyxel.image(0).height)  # 256
```
<br>
  
### set()  
  (x, y) に文字列のリストでイメージを設定します。  
  `set(x, y, data)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | i32 | イメージバンクの座標 |  
| y | i32 | イメージバンクの座標 |  
| data | リスト | ["1行目データ","2行目データ",・・・]<br>ドットの色を16進数で指定 |  

<br>

``` python
import pyxel
pyxel.init(32, 32)

data = ["bbbb",
        "b77b",
        "b77b",
        "3333"]
pyxel.image(0).set(0,0, data)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.blt(4,8, 0, 0,0, 4,4, 0)
    return

pyxel.run(update, draw)
```
![img set](images/api/g_set.png)  
<br>
  
### load()  
  (x, y) に画像ファイル (png/gif/jpeg) を読み込みます。  
  `load(x, y, filename)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | i32 | イメージバンクの座標 |  
| y | i32 | イメージバンクの座標 |  
| filename | str | 画像ファイル名 (png/gif/jpeg) |  

<br>

``` python
pyxel.image(2).load(0, 0, "penguin.png")    # イメージバンク2に画像ファイルを読み込む例
```

<br>

### save()  
  指定したイメージバンクをPNGファイルに出力する。（上級者向けAPI）  
  `save(filename, scale)`

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| filename | str | 出力ファイル名 (.png が付加される) |  
| scale | u32 | 画像サイズの倍率 |  

<br>

``` python
pyxel.image(0).save("image_0", 1)    # イメージバンク0を等倍で出力
```

<br>

### pget()  
  イメージバンクの (x, y) のピクセルの色 (0-15) を取得します。  
  `pget(x, y)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | イメージバンクの座標 |  
| y | f64 | イメージバンクの座標 |  

<br>

``` python
import pyxel
pyxel.init(32, 32)
pyxel.load("sample.pyxres")

# リソースファイルのイメージバンク0の色を取得して
# 行のデータごとに16進数の文字列に変換する例
data = []
for v in range(8):
    tmpstr = ""
    for u in range(8,16):
        tmpstr += format(pyxel.image(0).pget(u, v),'x')
    data.append(tmpstr)

# 文字列データを標準出力
for row in data:
    print('"'+row+'",')

# 文字列でイメージバンク2に設定
pyxel.image(2).set(0,0,data)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.blt(0,0, 2, 0,0, 8,8)
    return

pyxel.run(update, draw)
```
　print結果
<pre>"0a0ccc0a",
"0ac666ca",
"70f1f1f0",
"07ccccc0",
"00fccc50",
"000c5c0f",
"00556600",
"00000500",</pre>  
<br>
  
### pset()  
  イメージバンクの (x, y) に色colのピクセルを描画します。  
  `pset(x, y, col)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | イメージバンクの座標 |  
| y | f64 | イメージバンクの座標 |  
| col | u8 | 描画色 (0-15) |

<br>

``` python
import pyxel
pyxel.init(32, 32)
pyxel.load("sample.pyxres")
pyxel.image(0).pset(11,0, 10)
pyxel.image(0).pset(12,1, 10)
pyxel.image(0).pset(13,0, 10)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.blt(12,2, 0, 8,0, 8,8, 0)
    return

pyxel.run(update, draw)
```

<br>

[ページの先頭に戻る](#pyxel-api-sample)　

## タイルマップクラス  
<br>


### variable  


|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| width | u32 | タイルマップの幅 | `pyxel.tilemap(0).width` |
| height | u32 | タイルマップの高さ | `pyxel.tilemap(0).height` |
| refimg | u32 | タイルマップが参照するイメージバンク (0-2) | `pyxel.tilemap(0).refimg` |
<br>

``` python
print(pyxel.tilemap(0).width)   # 256
print(pyxel.tilemap(0).height)  # 256
```
 
``` python
pyxel.tilemap(0).refimg = 1  # イメージバンク1を設定する例
```
・[03_draw_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/03_draw_api.py)内の切り替え例
``` python
print(pyxel.tilemap(0).refimg, pyxel.tilemap(0).image)
pyxel.tilemap(0).image = pyxel.image(1)
print(pyxel.tilemap(0).refimg, pyxel.tilemap(0).image)
```

<br>
  
### set()  
  (x, y) に文字列のリストでタイルマップを設定します。  
  `set(x, y, data)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | i32 | タイルマップの書き込み開始位置 |  
| y | i32 | タイルマップの書き込み開始位置 |  
| data | リスト | ["1行目データ","2行目データ",・・・]<br>タイル座標を16進数で指定 |  

<br>
　※APIリファレンス記載の例にあるdataの値は古い仕様のものです。[03_draw_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/03_draw_api.py)内のコードを参照してください。  

``` python
import pyxel
pyxel.init(128, 128)
pyxel.load("sample.pyxres")

# タイルマップの左上4マスを下記のタイルにする例
# ( 1,0) ( 2,0) -> "0100 0200" 
# (12,0) (12,1) -> "0c00 0c01"
# 
# (tile_x,tile_y)の指定を xxyy の2オクテットで表す
# 値は16進数で範囲は0x00-0x1f
data = ["0100 0200",
        "0c00 0c01"]
pyxel.tilemap(0).set(0, 0, data)

def update():
    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, 128,128)
    return

pyxel.run(update, draw)
```
<br>

### pget()  
  (x, y) のタイルを取得します。タイルは(tile_x, tile_y)のタプルです。  
  `pget(x, y)`    

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | タイルマップの位置 |  
| y | f64 | タイルマップの位置 |  

<br>

``` python
import pyxel
pyxel.init(128, 128)
pyxel.load("sample.pyxres")
pyxel.mouse(True)

tile = (0,0)
def update():
    global tile
    xidx = pyxel.mouse_x // 8
    yidx = pyxel.mouse_y // 8
    tile = pyxel.tilemap(0).pget(xidx,yidx)
    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, 128,128)
    pyxel.text(1,9, str(tile), 7)
    return

pyxel.run(update, draw)
```
<br>
  
### pset()  
  (x, y) にタイルを設定します。タイルは(tile_x, tile_y)のタプルです。  
  `pset(x, y, tile)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| x | f64 | タイルマップの位置 |  
| y | f64 | タイルマップの位置 |  
| tile | (u8,u8) | タイル種類（イメージバンク上の位置） |  

<br>

``` python
xidx = x // 8
yidx = y // 8
pyxel.tilemap(0).pset(xidx,yidx, (1,0) )
```
<br>
  
  
[ページの先頭に戻る](#pyxel-api-sample)　　[TOPに戻る](../README.md#pyxel-game-development)
