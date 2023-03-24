# Pyxel API sample（非公式）

更新日：2023-03-24  
バージョン：Pyxel 1.9版  
  
## contents
・[システム](api_system.md#システム), [リソース](api_system.md#リソース), [入力](api_system.md#入力)  
・[グラフィックス](api_graphics.md#グラフィックス), [イメージクラス](api_graphics.md#イメージクラス), [タイルマップクラス](api_graphics.md#タイルマップクラス)   
・[オーディオ](api_audio.md#オーディオ), [サウンドクラス](api_audio.md#サウンドクラス), [ミュージッククラス](api_audio.md#サウンドクラス)   
・[数学](api_math.md)  
  
[Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。  
※下記import文でPyxelをインポートしたときのAPIの呼び出し記述になります。
``` python
import pyxel
```
  
## システム

- width,height  
  画面の幅と高さ
``` python
sw = pyxel.width
sh = pyxel.height
print("width=",sw,"height=",sh)     # print文はIDLEシェル等への出力でデバッグに利用できます
```
  
- frame_count  
  経過フレーム数
``` python
pyxel.text(10, 10, "Hello, Pyxel!", pyxel.frame_count % 16)
```
  
- init()  
  Pyxel アプリケーションを画面サイズ (width, height) で初期化します。  
  
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
  
- run()  
  Pyxel アプリケーションを開始
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
  
- show()  
  画面を表示してEscキーが押されるまで待機
``` python
import pyxel
pyxel.init(64, 64)
pyxel.text(10, 10, "Test", 7)
pyxel.show()
```

- flip()  
  画面を 1 フレーム更新（Webでは使用不可）
``` python
import pyxel
pyxel.init(64, 64)
while(True):
    pyxel.cls(0)
    pyxel.text(10,10, "Test", pyxel.frame_count % 16)
    pyxel.flip()
```
  
- quit()  
  Pyxel アプリケーションを終了
``` python
def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    return
```
  
## リソース
- load(filename, [image], [tilemap], [sound], [music])  
  リソースファイル (.pyxres) を読み込みます。  
  
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
  
## 入力
- mouse_x, mouse_y  
  現在のマウスカーソル座標  (Pyxel Web ではスマホタッチ位置を取得可)
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
  
- mouse_wheel  
  現在のマウスホイールの値
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
  
- btn(key)  
  keyが押されていたらTrue、押されていなければFalseを返します。
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
   
- btnp(key, [hold], [repeat])  
  そのフレームにkeyが押されたらTrue、押されなければFalseを返します。
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
・holdとrepeatを指定すると、holdフレーム以上ボタンを押し続けた時にrepeatフレーム間隔でTrueが返ります。
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
   
・keyの例(詳細は[キー定義一覧](https://github.com/kitao/pyxel/blob/main/python/pyxel/__init__.pyi)参照)
| コード例 | キー |
|:---|:---|
| pyxel.KEY_SPACE | スペースキー |
| pyxel.KEY_RETURN | Enterキー |
| pyxel.KEY_0 | 数字キー 0 |
| pyxel.KEY_A | 文字キー A |
| pyxel.MOUSE_BUTTON_LEFT | マウス左ボタン<br>スマホ画面タップ(Web) |
| pyxel.MOUSE_BUTTON_RIGHT | マウス右ボタン |
| pyxel.KEY_KP_1 | テンキー数字 1 |
| pyxel.KEY_KP_ENTER | テンキーEnterキー |  
  
- mouse(visible)  
  visibleがTrueならマウスカーソルを表示し、Falseなら非表示にします。マウスカーソルが非表示でも座標は更新されます。
``` python
pyxel.mouse(True)    # 以降False指定されるまで表示
```
  
