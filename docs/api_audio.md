# Pyxel API sample

オーディオ，サウンドクラス，ミュージッククラス  
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
|[数学](api_math.md#pyxel-api-sample)| [ceil()](api_math.md#ceil) [floor()](api_math.md#floor) [sgn()](api_math.md#sgn) [sin()](api_math.md#sin) [cos()](api_math.md#cos) [atan2()](api_math.md#atan2) [rseed()](api_math.md#rseed) [rndi()](api_math.md#rndi) [rndf()](api_math.md#rndf) [nseed()](api_math.md#nseed) [noise()](api_math.md#noise) |


<br> 
  
- [Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。  

<br>

- 公式サンプルは[04_sound_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api)を参照してください。  

<br>

- コード例で使用しているリソースファイル（[sample.pyxres](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/assets/sample.pyxres)）は公式サイトからDownloadできます。

<br>
  
## オーディオ  
<br>


### sound()  
  サウンドsnd (0-63) を操作します。([サウンドクラス](#サウンドクラス)を参照のこと)  
  `sound(snd)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| snd | u32 | サウンド (0-63) |  
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| サウンド | Sound | 指定したサウンドのオブジェクト |  

<br>
  
### music()  
  ミュージックmsc (0-7) を操作します。([ミュージッククラス](#ミュージッククラス)を参照のこと)  
  `music(msc)`


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| msc | u32 | ミュージック (0-7) |  

<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| ミュージック | Music | 指定したミュージックのオブジェクト |  

<br>
   
### play_pos()  
  チャンネルch (0-3) のサウンド再生位置を(サウンド番号, ノート番号)のタプルとして取得します。再生停止時はNoneを返します。  
  `play_pos(ch)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| ch | u32 | チャンネル (0-3) |  
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| snd, ノート番号 | (u32, u32) | ch再生中　(サウンド番号, ノート番号)のタプル <br> 停止時 None |  

<br>

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
<br>  

  
### play()  
  チャンネルch (0-3) でサウンドsnd (0-63) を再生します。sndがリストの場合順に再生されます。再生開始位置はtick (1 tick = 1/120 秒) で指定できます。loopにTrueを指定するとループ再生します。  
  `play(ch, snd, [tick], [loop])`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| ch | u32 | 演奏するチャンネル (0-3) |  
| snd | u32 | サウンド (0-63) |  
| tick | u32 | 再生開始位置 |  
| loop | bool | 省略，またはFalse指定でループ再生なし |  

<br>

　loop指定なしで1回だけ再生させる効果音に使いやすいAPI  

<br>
  

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
<br>  
  
  
### playm()  
  ミュージックmsc (0-7) を再生します。再生開始位置はtick (1 tick = 1/120 秒) で指定できます。loopにTrueを指定するとループ再生します。  
  `playm(msc, [tick], [loop]) `  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| msc | u32 | ミュージック (0-7) |  
| tick | u32 | 再生開始位置 |  
| loop | bool | Trueを指定するとループ再生 |  

<br>

　ミュージック指定なのでBGM再生に使いやすいAPI  

<br>
  

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
    pyxel.text(1,31,str(pyxel.play_pos(3)), 7)
    return

pyxel.run(update, draw)
```
<br>  
  
  
### stop()  
  指定したチャンネルch (0-3) の再生を停止します。stop()で全チャンネルの再生を停止します。  
  ` stop([ch])`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| ch | u32 | 停止するチャンネル (0-3)<br>省略時は全チャンネル停止 |  

<br>

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
    pyxel.text(1,31,str(pyxel.play_pos(3)), 7)
    return

pyxel.run(update, draw)
```
<br>  
  
  
## サウンドクラス  
<br>  

### variable  

|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| notes | リスト i8 | 音程 (0-127) のリスト。数値が大きいほど音程は高くなり、33 で'A2'(440Hz)になります。休符は-1 です。 | pyxel.sound(0).notes |  
| tones | リスト u8 | 音色 (0:Triangle / 1:Square / 2:Pulse / 3:Noise) のリスト<br>レトロゲームサウンドでは，メロディー：Pulse/Square，ベース：Triangle，ドラム：Noise で用いることが多いそうです。 | pyxel.sound(0).tones |  
| volumes | リスト u8 | 音量 (0-7) のリスト | pyxel.sound(0).volumes |  
| effects | リスト u8 | エフェクト (0:None / 1:Slide / 2:Vibrato / 3:FadeOut) のリスト<br> Fで音を分離できます。 | pyxel.sound(0).effects |  
| speed | u32| 再生速度。1 が一番速く、数値が大きいほど再生速度は遅くなります。120 で 1 音の長さが 1 秒になります。 | pyxel.sound(0).speed |  

<br>

再生速度は `pyxel.sound(0).speed = 30` のように代入が可能。  
各リストの直接代入 `pyxel.sound(0).notes = data` は不可。（`pyxel.sound(0).notes[0]=30` は可）  
各リストの更新はset()命令を使うとよい。  

<br>  

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
<br>  
  
  
### set()  
  文字列で音程、音色、音量、エフェクトを設定します。音色、音量、エフェクトの長さが音程より短い場合は、先頭から繰り返されます。  
  `set(notes, tones, volumes, effects, speed)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| notes | str | 音程 ドレミファソラシをcdefgabの表記で指定<br>「ド　（低い） c0 c1 c2 c3 c4 （高い）」<br>「ファのシャープ f#0 f#1 f#2 f#3 f#4」「シのフラット b-0 b-1 b-2 b-3 b-4」<br> 「休符 r」 |  
| tones | str | 音色 [T]riangle [S]quare [P]ulse [N]oise | 
| volumes | str | 音量 [0-7] | 
| effects | str | エフェクト [N]one [S]lide [V]ibrato [F]adeOut | 
| speed | u32 | 再生速度 1 が一番速く、数値が大きいほど再生速度は遅くなります。120 で 1 音の長さが 1 秒になります。 | 

<br>

　ブログ記事[音程の一覧](https://kinutani.hateblo.jp/entry/2023/02/05/205654)を参照してください。  


``` python
pyxel.sound(0).set("c2d2e2f2g2a2b2c3", "p", "7", "n", 30)
```
<br>  
  

### set_notes()  
  'CDEFGAB'+'#-'+'0123'または'R'の文字列で音程を設定します。大文字と小文字は区別されず、空白は無視されます。  
  `set_notes(notes)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| notes | str | 音程 'CDEFGAB'+'#-'+'0123'または'R'の文字列 |  

<br>

``` python
pyxel.sound(0).set_notes("c2d2e2f2g2a2b2c3")   # ドレミファソラシド
```
<br>  
  
  
### set_tones()  
  'TSPN'の文字列で音色を設定します。大文字と小文字は区別されず、空白は無視されます。  
  `set_tones(tones)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| tones | str | 音色 'TSPN'の文字列 |  

<br>

``` python
pyxel.sound(0).set_tones("TTSS PPPN")
```
<br>  
  
  
### set_volumes()  
  '01234567'の文字列で音量を設定します。大文字と小文字は区別されず、空白は無視されます。  
  `set_volumes(volumes)`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| volumes | str | 音量 '01234567'の文字列 |  

<br>
 

``` python
pyxel.sound(0).set_volumes("7777 7531")
```
<br>  
  
  
### set_effects()  
  'NSVF'の文字列でエフェクトを設定します。大文字と小文字は区別されず、空白は無視されます。  
  `set_effects(effects)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| effects | str | エフェクト 'NSVF'の文字列 |  

<br>
 

``` python
pyxel.sound(0).set_effects("NFNF NVVS")
```
<br>  
  


## ミュージッククラス  
<br>  

### variable  

|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| snds_list | リスト | サウンド (0-63) のリストをチャンネル数分連ねた 2 次元リスト | pyxel.music(0).snds_list | 

<br>
  
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

i=0
for msc in pyxel.music(0).snds_list:
    print("ch{}:".format(i),end=" ")
    for snd in msc:
        print(snd,end=" ")
    print("\n")
    i+=1

pyxel.show()
```
  
　サンプルリソース ミュージック0 の snds_list の表示結果
<pre>ch0: 0 1 
ch1: 2 3 
ch2: 4 
ch3: 
</pre>

<br>  

### set()  
  全チャンネルのサウンド (0-63) のリストを設定します。空リストを指定するとそのチャンネルは再生に使用しません。  
  `set(snds0, snds1, snds2, snds3)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| snds0 | リスト | ch0 のサウンド |  
| snds1 | リスト | ch1 のサウンド |  
| snds2 | リスト | ch2 のサウンド |  
| snds3 | リスト | ch3 のサウンド |  

<br>

``` python
pyxel.music(0).set([0, 1], [2, 3], [4], [])
```
<br>  
  

[ページの先頭に戻る](#pyxel-api-sample)　　[TOPに戻る](../README.md#pyxel-game-development)
