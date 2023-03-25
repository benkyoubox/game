# Pyxel API sample

更新日：2023-03-25  
バージョン：Pyxel 1.9版  
  
## contents
- [システム](api_system.md#システム), [リソース](api_system.md#リソース), [入力](api_system.md#入力)  
- [グラフィックス](api_graphics.md#グラフィックス), [イメージクラス](api_graphics.md#イメージクラス), [タイルマップクラス](api_graphics.md#タイルマップクラス)   
- [オーディオ](api_audio.md#オーディオ), [サウンドクラス](api_audio.md#サウンドクラス), [ミュージッククラス](api_audio.md#ミュージッククラス)   
- [数学](api_math.md)  
  
[Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。  
（公式サンプルは[04_sound_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api)を参照してください）  
  
  
※下記import文でPyxelをインポートしたときのAPIの呼び出し記述になります。
``` python
import pyxel
```
  
## オーディオ

- sound(snd)  
  サウンドsnd (0-63) を操作します。([サウンドクラス](#サウンドクラス)を参照のこと)
  
- music(msc)  
  ミュージックmsc (0-7) を操作します。([ミュージッククラス](#ミュージッククラス)を参照のこと)
  
- play_pos(ch)  
  チャンネルch (0-3) のサウンド再生位置を(サウンド番号, ノート番号)のタプルとして取得します。再生停止時はNoneを返します。
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(0, [0,1])
    return

def draw():
    pyxel.cls(0)
    pyxel.text(1,1,str(pyxel.play_pos(0)), 7)
    return

pyxel.run(update, draw)
```
  
- play(ch, snd, [tick], [loop])  
  チャンネルch (0-3) でサウンドsnd (0-63) を再生します。sndがリストの場合順に再生されます。再生開始位置はtick (1 tick = 1/120 秒) で指定できます。loopにTrueを指定するとループ再生します。
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(0, 1, loop=True)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.play(0, 1, tick=240)
    return

def draw():
    pyxel.cls(0)
    pyxel.text(1,1,str(pyxel.play_pos(0)), 7)
    return

pyxel.run(update, draw)
```
  
- playm(msc, [tick], [loop])  
  ミュージックmsc (0-7) を再生します。再生開始位置はtick (1 tick = 1/120 秒) で指定できます。loopにTrueを指定するとループ再生します。
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.playm(0, loop=True)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.playm(0, tick=240, loop=True)
    return

def draw():
    pyxel.cls(0)
    pyxel.text(1, 1,str(pyxel.play_pos(0)), 7)
    pyxel.text(1,11,str(pyxel.play_pos(1)), 7)
    pyxel.text(1,21,str(pyxel.play_pos(2)), 7)
    return

pyxel.run(update, draw)
```
  
- stop([ch])  
  指定したチャンネルch (0-3) の再生を停止します。stop()で全チャンネルの再生を停止します。
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.playm(0, loop=True)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.stop()
    return

def draw():
    pyxel.cls(0)
    pyxel.text(1, 1,str(pyxel.play_pos(0)), 7)
    pyxel.text(1,11,str(pyxel.play_pos(1)), 7)
    pyxel.text(1,21,str(pyxel.play_pos(2)), 7)
    return

pyxel.run(update, draw)
```
  
## サウンドクラス
- notes  
  音程 (0-127) のリスト。数値が大きいほど音程は高くなり、33 で'A2'(440Hz)になります。休符は-1 です。
  
- tones  
  音色 (0:Triangle / 1:Square / 2:Pulse / 3:Noise) のリスト  
  レトロゲームサウンドでは，メロディー：Pulse/Square，ベース：Triangle，ドラム：Noise で用いることが多いそうです。  
  
- volumes  
  音量 (0-7) のリスト
  
- effects  
  エフェクト (0:None / 1:Slide / 2:Vibrato / 3:FadeOut) のリスト
  Fで音を分離できます。
  
- speed  
  再生速度。1 が一番速く、数値が大きいほど再生速度は遅くなります。120 で 1 音の長さが 1 秒になります。

``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

print("notes")
for note in pyxel.sound(0).notes:
    print(note,end=" ")
print("\n")
print("tones")
for tone in pyxel.sound(0).tones:
    print(tone,end=" ")
print("\n")
print("volumes")
for volume in pyxel.sound(0).volumes:
    print(volume,end=" ")
print("\n")
print("effects")
for effect in pyxel.sound(0).effects:
    print(effect,end=" ")
print("\n")
print("speed")
print(pyxel.sound(0).speed)

def update():
    return

def draw():
    pyxel.cls(0)
    return

pyxel.run(update, draw)
```
  
- set(notes, tones, volumes, effects, speed)  
``` python
pyxel.sound(0).set("c2d2e2f2g2a2b2c3", "p", "7", "n", 30)
```
　音程はドレミファソラシをcdefgabの表記で指定します。ブログ記事[音程の一覧](https://kinutani.hateblo.jp/entry/2023/02/05/205654)を参照してください。
  
- set_notes(notes)  
  'CDEFGAB'+'#-'+'0123'または'R'の文字列で音程を設定します。大文字と小文字は区別されず、空白は無視されます。
``` python
pyxel.sound(0).set_notes("c2d2e2f2g2a2b2c3")   # ドレミファソラシド
```
  
- set_tones(tones)  
  'TSPN'の文字列で音色を設定します。大文字と小文字は区別されず、空白は無視されます。
``` python
pyxel.sound(0).set_tones("TTSS PPPN")
```
  
- set_volumes(volumes)  
  '01234567'の文字列で音量を設定します。大文字と小文字は区別されず、空白は無視されます。
``` python
pyxel.sound(0).set_volumes("7777 7531")
```
  
- set_effects(effects)  
  'NSVF'の文字列でエフェクトを設定します。大文字と小文字は区別されず、空白は無視されます。
``` python
pyxel.sound(0).set_effects("NFNF NVVS")
```


## ミュージッククラス
- snds_list  
  サウンド (0-63) のリストをチャンネル数分連ねた 2 次元リスト
``` python
i=0
for msc in pyxel.music(0).snds_list:
    print("ch{}:".format(i),end=" ")
    for snd in msc:
        print(snd,end=" ")
    print("\n")
    i+=1
```
<pre>ch0: 0 1 

ch1: 2 3 

ch2: 4 

ch3: 
</pre>
  
- set(snds0, snds1, snds2, snds3)  
  全チャンネルのサウンド (0-63) のリストを設定します。空リストを指定するとそのチャンネルは再生に使用しません。
``` python
pyxel.music(0).set([0, 1], [2, 3], [4], [])
```
  
  

[TOPに戻る](api_audio.md)
