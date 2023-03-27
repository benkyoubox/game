# Pyxel Game Development
![DEMO image](docs/images/demo.gif)  
Python向けレトロゲームエンジン Pyxel を使用したゲーム作成の情報  


<br>


- [Pyxel公式サイト](https://github.com/kitao/pyxel/blob/main/docs/README.ja.md)  
  
- [ブログ記事（Pyxelゲーム作成の記事一覧）](https://kinutani.hateblo.jp/entry/2022/12/15/184811)  


<br>


[ [基本](#pyxelゲームの処理の基本) | [コマンド抜粋](#コマンド抜粋) | [APIコード例](README.md#api) | [プログラム例](#ブログ記事で紹介したプログラム) | [テンプレート](#プログラムテンプレート) | [コード部品](#コード部品) ]  


<br>

  
## Pyxelゲームの処理の基本
Pyxelのゲームの処理の流れは基本的に「初期化処理を最初に行い，その後は update() と draw() を実行し続ける」になります。この流れを頭に入れてゲーム作成を行いましょう。  
![flow image](docs/images/pyxel_flow.png)  


<br>

  
## コマンド抜粋

| コマンド | 内容 |
|:---|:---|
| `pip install -U pyxel` | Windows Pyxelのインストール（アップデート） |
| `pyxel copy_examples` | サンプルコードコピー |
| `pyxel edit filename` | Pyxel Editor の起動 |
| `pyxel package appdir srcname` | Pyxel アプリケーションファイル (.pyxapp) 作成 |
| `pyxel app2html your_app.pyxapp` | Pyxel アプリを HTML ファイルに変換する |
| `python -m http.server` | PythonのWebサーバー起動<br>http://localhost:8000/test.html のようにアクセス |


<br>

  
## API

  APIの呼び出しコード例です。  

| 分類 | 項目 |
|:---:|:---|
|[システム](docs/api_system.md#pyxel-api-sample)| [変数](docs/api_system.md#variable) [init()](docs/api_system.md#init) [run()](docs/api_system.md#run) [show()](docs/api_system.md#show) [flip()](docs/api_system.md#flip) [quit()](docs/api_system.md#quit)|
|[リソース](docs/api_system.md#リソース)| [load()](docs/api_system.md#load)  |
|[入力](docs/api_system.md#入力)| [変数](docs/api_system.md#variable-1) [btn()](docs/api_system.md#btn) [btnp()](docs/api_system.md#btnp) [btnr()](docs/api_system.md#btnr) [mouse()](docs/api_system.md#mouse) [キー記述例](docs/api_system.md#keycode) |  
|[グラフィックス](docs/api_graphics.md#pyxel-api-sample)| [変数](docs/api_graphics.md#variable) [image()](docs/api_graphics.md#image) [tilemap()](docs/api_graphics.md#tilemap) [clip()](docs/api_graphics.md#clip) [camera()](docs/api_graphics.md#camera) [pal()](docs/api_graphics.md#pal) [cls()](docs/api_graphics.md#cls) [pget()](docs/api_graphics.md#pget) [pset()](docs/api_graphics.md#pset) <br> [line()](docs/api_graphics.md#line) [rect()](docs/api_graphics.md#rect) [rectb()](docs/api_graphics.md#rectb) [circ()](docs/api_graphics.md#circ) [circb()](docs/api_graphics.md#circb) [elli()](docs/api_graphics.md#elli) [ellib()](docs/api_graphics.md#ellib) [tri()](docs/api_graphics.md#tri) [trib()](docs/api_graphics.md#trib) <br> [fill()](docs/api_graphics.md#fill) [blt()](docs/api_graphics.md#blt) [bltm()](docs/api_graphics.md#bltm) [text()](docs/api_graphics.md#text) [表示色](docs/api_graphics.md#color) |
|[イメージクラス](docs/api_graphics.md#イメージクラス)| [変数](docs/api_graphics.md#variable-1) [set()](docs/api_graphics.md#set) [load()](docs/api_graphics.md#load) [save()](docs/api_graphics.md#save) [pget()](docs/api_graphics.md#pget-1) [pset()](docs/api_graphics.md#pset-1) |
|[タイルマップクラス](docs/api_graphics.md#タイルマップクラス)| [変数](docs/api_graphics.md#variable-2)  [set()](docs/api_graphics.md#set-1) [pget()](docs/api_graphics.md#pget-2) [pset()](docs/api_graphics.md#pset-2) |
|[オーディオ](docs/api_audio.md#pyxel-api-sample)| [sound()](docs/api_audio.md#sound) [music()](docs/api_audio.md#music) [play_pos()](docs/api_audio.md#play_pos) [play()](docs/api_audio.md#play) [playm()](docs/api_audio.md#playm) [stop()](docs/api_audio.md#stop) |
|[サウンドクラス](docs/api_audio.md#サウンドクラス)| [変数](docs/api_audio.md#variable) [set()](docs/api_audio.md#set) [set_notes()](docs/api_audio.md#set_notes) [set_tones()](docs/api_audio.md#set_tones) [set_volumes()](docs/api_audio.md#set_volumes) [set_effects()](docs/api_audio.md#set_effects) |
|[ミュージッククラス](docs/api_audio.md#ミュージッククラス)| [変数](docs/api_audio.md#variable-1) [set()](docs/api_audio.md#set-1) |
|[数学](docs/api_math.md#pyxel-api-sample)| [ceil()](docs/api_math.md#ceil) [floor()](docs/api_math.md#floor) [sgn()](docs/api_math.md#sgn) [sin()](docs/api_math.md#sin) [cos()](docs/api_math.md#cos) [atan2()](docs/api_math.md#atan2) [rseed()](docs/api_math.md#rseed) [rndi()](docs/api_math.md#rndi) [rndf()](docs/api_math.md#rndf) [nseed()](docs/api_math.md#nseed) [noise()](docs/api_math.md#noise) |


<br>


## ブログ記事で紹介したプログラム  

| No. | ソースコード | 内容 |記事|
|:---:|:---:|:---|:---:|
| 1 | [じゃんけんゲーム](pyxel/rps_game/) | クリック位置の取得 | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2022/10/29/155359) |  
| 2 | [アクションゲーム1](pyxel/ninja/) | 忍者のキャラクターをジャンプさせます。<br>タイルマップの使用 | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2022/11/27/092216) |  
| 3 | [アクションゲーム2](pyxel/penguinjump/) | ペンギンのキャラクターがステージクリアを目指します。<br>画面スクロール，ゲームの進行管理 | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2022/12/25/162239) |  
| 4 | [三目並べ](pyxel/TicTacToe/) | クラスを使ったプログラム | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2023/01/09/220920) |  
| 5 | [シューティングゲーム](pyxel/shooter_r/) | 公式サンプルプログラムを横方向のSTGに改造します | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2023/01/15/155601) |  
| 6 | [迷路ゲーム1](pyxel/maze/) | ウサギロボがお化けを避けてゴールを目指します<br>上下左右移動のアニメーション（クラス未使用版） | [![ブログ](docs/images/ico_BLOG.png)](https://blog.hatena.ne.jp/kinutani/kinutani.hateblo.jp/edit?entry=4207112889968552854) |  
| 7 | [迷路ゲーム2](pyxel/maze_random/) | アリスが迷路のゴールを目指します<br>迷路の自動生成　2点間の距離を調べる | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2023/03/10/222546) |  
| 8 | [日本語表示例](pyxel/bmpfont/) | ビットマップフォントの表示 | [![ブログ](docs/images/ico_BLOG.png)](https://kinutani.hateblo.jp/entry/2023/03/22/185042) |  


<br>


## ひな形等

<br>


### プログラムテンプレート  

| No. | リンク | 内容 |
|:---:|:---:|:---|
| 1 | [Appクラスのひな形](template/01_main.py) | Appクラスのコード |  
| 2 | [テストプログラム用](template/01a_simple.py) | クラスなし簡易版 |  
| 3 | [スクリーンショット用](template/02_screenshot.py) | show()で1回だけ表示 |  
| 4 | [イメージバンク画像出力](template/02a_savepng.py) | イメージバンクをPNGファイルで出力 |  
| 5 | [GIFアニメーションファイル用](template/03_animation.py) | flip()で表示ループ |  
    

<br>
  
  
### コード部品  


乱数（整数）  
``` python
pyxel.rndi(1,100)
```
マウスカーソル表示  
``` python
pyxel.mouse(True)
```
マウス座標取得
``` python
x = pyxel.mouse_x
y = pyxel.mouse_y
```
方向キー入力 （[キー記述例](docs/api_system.md#keycode)  ）
``` python
if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):

if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):

if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):

if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
```
``` python
if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):

if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):

if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):

if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
```
スペースキー入力  
``` python
if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
```
``` python
if pyxel.btnp(pyxel.KEY_SPACE,15,15) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A,15,15):
```
マウスクリック
``` python
if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
```
タイルマップ取得，設定  
``` python
xidx = 1 //8
yidx = 1 //8
tile = pyxel.tilemap(0).pget(xidx,yidx)
pyxel.tilemap(0).pset(xidx,yidx, (1,0) )
```
タイルマップ表示  
``` python
pyxel.camera()
pyxel.bltm(0,0, 0, self.scroll_x,self.scroll_y, pyxel.width,pyxel.height, 0)
pyxel.camera(self.scroll_x,self.scroll_y)
```
イメージ表示  （[透明色](docs/api_graphics.md#color)）   
``` python
pyxel.blt(self.x, self.y, 0, u,v, self.w, self.h, 0)
```
効果音再生  
``` python
pyxel.play(ch,sNo)
```
BGM再生・停止  
``` python
pyxel.playm(msc, loop=True)
pyxel.stop(ch)
```
#### ゲーム進行例
シーン番号  
``` python
SNO_TITLE    = 0
SNO_STAGESET = 10
SNO_PLAY     = 11
SNO_SFINISH  = 12
SNO_GAMEOVER = 13
SNO_END      = 20
```
シーン分岐  
``` python
if SNO_TITLE == self.scene:
    pass
elif SNO_STAGESET == self.scene:
    pass
elif SNO_PLAY == self.scene:
    pass
elif SNO_SFINISH == self.scene:
    pass
elif SNO_GAMEOVER == self.scene:
    pass
elif SNO_END == self.scene:
    pass
else:
    pass
```

<br>


[TOPに戻る](README.md#Pyxel-Game-Development)


# Author
E-mail benkyoubox@gmail.com  


