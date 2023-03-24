# Pyxel API sample（非公式）

[Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のコード例

更新日：2023-03-22
バージョン：Pyxel 1.9版

## contents
下記import文でPyxelをインポートしたときのAPI実行例
``` python
import pyxel
```
[システム,リソース,入力,数学](api_system.md)   
[グラフィックス,イメージクラス,タイルマップクラス](api_.md)   
[オーディオ,サウンドクラス,ミュージッククラス](api_.md) 

## システム

- width,height 画面の幅と高さ
``` python
sw = pyxel.width
sh = pyxel.height
print("width=",sw,"height=",sh)
```

- frame_count 経過フレーム数
``` python
pyxel.text(10, 10, "Hello, Pyxel!", pyxel.frame_count % 16)
```

- init() Pyxel アプリケーション初期化 画面サイズとタイトル指定
``` python
pyxel.init(240, 160, title="Pyxel App")
```
- init() Pyxel アプリケーション初期化 動作フレームレート60fps，終了キー（なし）に指定
``` python
pyxel.init(240, 160, title="Pyxel App", fps=60, quit_key=pyxel.KEY_NONE)
```
- init() Pyxel アプリケーション初期化 画面表示の倍率，画面キャプチャの倍率，画面キャプチャ動画の録画時間指定
``` python
pyxel.init(128, 64, display_scale=5,capture_scale=5,capture_sec=10)
```
- run() Pyxel アプリケーションを開始
``` python
# このブロックで1つのアプリのコード例です
import pyxel
pyxel.init(64, 64)

def update():
    pass
    return

def draw():
    pyxel.cls(0)
    return

pyxel.run(update, draw)
```
- show() 画面を表示してEscキーが押されるまで待機
``` python
# このブロックで1つのアプリのコード例です
import pyxel
pyxel.init(64, 64)
pyxel.text(10, 10, "Test", 7)
pyxel.show()
```

- flip() 画面を 1 フレーム更新（Webでは使用不可）
``` python
# このブロックで1つのアプリのコード例です
import pyxel
pyxel.init(64, 64)
while(True):
    pyxel.cls(0)
    pyxel.text(10,10, "Test", pyxel.frame_count % 16)
    pyxel.flip()
```

- quit() Pyxel アプリケーションを終了
``` python
def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    return
```
  
## リソース

## 入力

## 数学
