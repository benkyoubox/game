# Pyxel API sample

オーディオ，サウンドクラス，ミュージッククラス  
バージョン：Pyxel 2.4版  
  
## contents


| 分類 | 項目 |
|:---:|:---|
|[システム](api_system.md#システム)| [変数](api_system.md#variable) [init()](api_system.md#init) [run()](api_system.md#run) [show()](api_system.md#show) [flip()](api_system.md#flip) [quit()](api_system.md#quit)|
|[リソース](api_system.md#リソース)| [load()](api_system.md#load) [save()](api_system.md#save)  |
|[入力](api_system.md#入力)| [変数](api_system.md#variable-1) [btn()](api_system.md#btn) [btnp()](api_system.md#btnp) [btnr()](api_system.md#btnr) [mouse()](api_system.md#mouse) [キー記述例](api_system.md#keycode) |  
|[グラフィックス](api_graphics.md#グラフィックス)| [変数](api_graphics.md#variable) [image()](api_graphics.md#image) [tilemap()](api_graphics.md#tilemap) [clip()](api_graphics.md#clip) [camera()](api_graphics.md#camera) [pal()](api_graphics.md#pal) [dither()](api_graphics.md#dither) [cls()](api_graphics.md#cls) [pget()](api_graphics.md#pget) [pset()](api_graphics.md#pset) <br> [line()](api_graphics.md#line) [rect()](api_graphics.md#rect) [rectb()](api_graphics.md#rectb) [circ()](api_graphics.md#circ) [circb()](api_graphics.md#circb) [elli()](api_graphics.md#elli) [ellib()](api_graphics.md#ellib) [tri()](api_graphics.md#tri) [trib()](api_graphics.md#trib) <br> [fill()](api_graphics.md#fill) [blt()](api_graphics.md#blt) [bltm()](api_graphics.md#bltm) [text()](api_graphics.md#text) [表示色](api_graphics.md#color) |
|[イメージクラス](api_graphics.md#イメージクラス)| [変数](api_graphics.md#variable-1) [from_image()](api_graphics.md#from_image) [data_ptr()](api_graphics.md#data_ptr) [set()](api_graphics.md#set) [load()](api_graphics.md#load) [save()](api_graphics.md#save) [pget()](api_graphics.md#pget-1) [pset()](api_graphics.md#pset-1) |
|[タイルマップクラス](api_graphics.md#タイルマップクラス)| [変数](api_graphics.md#variable-2)  [set()](api_graphics.md#set-1) [pget()](api_graphics.md#pget-2) [pset()](api_graphics.md#pset-2) |
|[フォントクラス](api_graphics.md#フォントクラス)| [Font()](api_graphics.md#font) [text_width()](api_graphics.md#text_width) |
|[オーディオ](api_audio.md#オーディオ)| [変数](api_audio.md#variable)  [sound()](api_audio.md#sound) [music()](api_audio.md#music) [play_pos()](api_audio.md#play_pos) [play()](api_audio.md#play) [playm()](api_audio.md#playm) [stop()](api_audio.md#stop) |
|[サウンドクラス](api_audio.md#サウンドクラス)| [変数](api_audio.md#variable-1) [set()](api_audio.md#set) [set_notes()](api_audio.md#set_notes) [set_tones()](api_audio.md#set_tones) [set_volumes()](api_audio.md#set_volumes) [set_effects()](api_audio.md#set_effects) [mml()](api_audio.md#mml) [old_mml()](api_audio.md#old_mml) [save()](api_audio.md#save) [total_sec()](api_audio.md#total_sec) |
|[ミュージッククラス](api_audio.md#ミュージッククラス)| [変数](api_audio.md#variable-2) [set()](api_audio.md#set-1) [save()](api_audio.md#save-1) |
|[数学](api_math.md#pyxel-api-sample)| [ceil()](api_math.md#ceil) [floor()](api_math.md#floor) [sgn()](api_math.md#sgn) [sqrt()](api_math.md#sqrt) [sin()](api_math.md#sin) [cos()](api_math.md#cos) [atan2()](api_math.md#atan2) [rseed()](api_math.md#rseed) [rndi()](api_math.md#rndi) [rndf()](api_math.md#rndf) [nseed()](api_math.md#nseed) [noise()](api_math.md#noise) |


<br> 
  
- [Pyxel APIリファレンス](https://github.com/kitao/pyxel/blob/main//docs/README.ja.md) のAPI実行例です。  

<br>

- 公式サンプルは[04_sound_api.py](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api)を参照してください。  

<br>

- コード例で使用しているリソースファイル（[sample.pyxres](https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/assets/sample.pyxres)）は公式サイトからDownloadできます。

<br>
  
## オーディオ  
<br>

### variable  

|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| sounds | リスト Sound | [サウンドクラス](#サウンドクラス)のインスタンスのリスト (0-63)  | `pyxel.sounds[0].speed = 60` |  
| musics | リスト Music | [ミュージッククラス](#ミュージッククラス)のインスタンスのリスト (0-7)  | `pyxel.musics[msc].set([snd1], [snd2], [snd3])` |  

<br>


### sounds  
  ※ 非推奨関数  
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

> __Note__  
  Pyxel 2.0版から，サウンドのリストは `pyxel.sounds[0].speed = 60` のように操作できます。

<br>
  
### music()  
  ※ 非推奨関数  
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

> __Note__  
  Pyxel 2.0版から，ミュージックのリストは `pyxel.musics[msc].set([snd1], [snd2], [snd3])` のように操作できます。

<br>

### play_pos()  
  チャンネルch (0-3) のサウンド再生位置を(サウンド番号, 秒)のタプルとして取得します。再生停止時はNoneを返します。  
  `play_pos(ch)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| ch | u32 | チャンネル (0-3) |  
  
<br>

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| sound_no, sec | (u32, float) | ch再生中　(サウンド番号, 秒)のタプル <br> 停止時 None |  

<br>

``` python
import pyxel
pyxel.init(128, 64)
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

> __Note__  
  Pyxel 2.4版でplay_pos()の戻り値が (sound_no, sec) に変更になりました。  
  2.3版までは (サウンド番号 u32, ノート番号 u32) のタプルです。  

<br>

  
### play()  
  チャンネルch (0-3) でサウンドsnd (0-63) を再生します。  
  snd にはサウンド番号，複数サウンドのリスト，または MML 文字列を指定できます。  
  secで再生開始位置を秒単位で指定できます。loopにTrueを指定するとループ再生します。  
  再生終了後に以前の音に復帰させるにはresumeにTrueを指定します。  
  `play(ch, snd, [sec], [loop], [resume])`  
  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| ch | u32 | 演奏するチャンネル (0-3) |  
| snd | u32<br>リスト u32<br>str | サウンド (0-63)<br>サウンドのリスト<br>MML文字列 |  
| sec | float | 再生開始位置 |  
| loop | bool | 省略，またはFalse指定でループ再生なし |  
| resume | bool | Trueで再生終了後，直前に再生していたサウンドを復帰 |
  
<br>

　loop指定なしで1回だけ再生させる効果音に使いやすいAPI  

<br>
  

``` python
import pyxel
pyxel.init(128, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(0, 1, loop=True)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.play(0, 1, sec=2)
    return

def draw():
    pyxel.cls(0)
    pyxel.text(1,1,str(pyxel.play_pos(0)), 7)
    return

pyxel.run(update, draw)
```
  
<br>

> __Note__  
古いバージョン（Pyxel 2.3）では再生開始位置を tick (1 tick = 1/120 秒) で指定します。  
  `play(ch, snd, [tick], [loop], [resume])`  
  例 pyxel.play(0, 1, tick=240)  

<br>  
  
  
### playm()  
  ミュージックmsc (0-7) を再生します。secで再生開始位置を秒単位で指定できます。loopにTrueを指定するとループ再生します。  
  `playm(msc, [sec], [loop]) `  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| msc | u32 | ミュージック (0-7) |  
| sec | float | 再生開始位置 |   
| loop | bool | Trueを指定するとループ再生 |  

<br>

　ミュージック指定なのでBGM再生に使いやすいAPI  

<br>
  

``` python
import pyxel
pyxel.init(128, 64)
pyxel.load("sample.pyxres")

def update():
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.playm(0, loop=True)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.playm(0, sec=2, loop=True)
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

> __Note__  
古いバージョン（Pyxel 2.3）では再生開始位置を tick (1 tick = 1/120 秒) で指定します。  
  `playm(msc, [tick], [loop]) `   
  例 pyxel.playm(0, tick=240, loop=True)  
  

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
pyxel.init(128, 64)
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
| notes | リスト i8 | 音程 (0-127) のリスト。数値が大きいほど音程は高くなり、33 で'A2'(440Hz)になります。休符は-1 です。 | `pyxel.sounds[0].notes` |  
| tones | リスト u8 | 音色 (0:Triangle / 1:Square / 2:Pulse / 3:Noise) のリスト<br>レトロゲームサウンドでは，メロディー：Pulse/Square，ベース：Triangle，ドラム：Noise で用いることが多いそうです。 | `pyxel.sounds[0].tones` |  
| volumes | リスト u8 | 音量 (0-7) のリスト | `pyxel.sounds[0].volumes` |  
| effects | リスト u8 | エフェクト (0:None / 1:Slide / 2:Vibrato / 3:FadeOut / 4:Half-FadeOut / 5:Quarter-FadeOut) のリスト | `pyxel.sounds[0].effects` |  
| speed | u32| 再生速度。1 が一番速く、数値が大きいほど再生速度は遅くなります。120 で 1 音の長さが 1 秒になります。 | `pyxel.sounds[0].speed` |  

<br>

再生速度は `pyxel.sounds[0].speed = 30` のように代入が可能。  
各リストの直接代入 `pyxel.sounds[0].notes = data` は不可。（`pyxel.sounds[0].notes[0]=30` は可）  
各リストの更新はset()命令を使うとよい。  

<br>  

``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

print("notes")
for note in pyxel.sounds[0].notes:
    print(note,end=" ")
print("\n")
print("tones")
for tone in pyxel.sounds[0].tones:
    print(tone,end=" ")
print("\n")
print("volumes")
for volume in pyxel.sounds[0].volumes:
    print(volume,end=" ")
print("\n")
print("effects")
for effect in pyxel.sounds[0].effects:
    print(effect,end=" ")
print("\n")
print("speed")
print(pyxel.sounds[0].speed)

def update():
    return

def draw():
    pyxel.cls(0)
    return

pyxel.run(update, draw)
```
<br>  
  
  
### set()  
  文字列で音程，音色，音量，エフェクトを設定します。音色、音量，エフェクトの長さが音程より短い場合は，先頭から繰り返されます。  
  `set(notes, tones, volumes, effects, speed)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| notes | str | 音程 ドレミファソラシをcdefgabの表記で指定<br>「ド　（低い） c0 c1 c2 c3 c4 （高い）」<br>「ファのシャープ f#0 f#1 f#2 f#3 f#4」「シのフラット b-0 b-1 b-2 b-3 b-4」<br> 「休符 r」 |  
| tones | str | 音色 [T]riangle [S]quare [P]ulse [N]oise | 
| volumes | str | 音量 [0-7] | 
| effects | str | エフェクト [N]one [S]lide [V]ibrato [F]adeOut [H]alf-FadeOut [Q]uarter-FadeOut | 
| speed | u32 | 再生速度 1 が一番速く、数値が大きいほど再生速度は遅くなります。120 で 1 音の長さが 1 秒になります。 | 

<br>

　ブログ記事[音程の一覧](https://kinutani.hateblo.jp/entry/2023/02/05/205654)を参照してください。  


``` python
pyxel.sounds[0].set("c2d2e2f2g2a2b2c3", "p", "7", "n", 30)
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
pyxel.sounds[0].set_notes("c2d2e2f2g2a2b2c3")   # ドレミファソラシド
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
pyxel.sounds[0].set_tones("TTSS PPPN")
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
pyxel.sounds[0].set_volumes("7777 7531")
```
<br>  
  
  
### set_effects()  
  'NSVFHQ'の文字列でエフェクトを設定します。大文字と小文字は区別されず、空白は無視されます。  
  [N]one [S]lide [V]ibrato [F]adeOut [H]alf-FadeOut [Q]uarter-FadeOut    
  `set_effects(effects)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| effects | str | エフェクト 'NSVFHQ'の文字列 |  

<br>
 

``` python
pyxel.sounds[0].set_effects("NFNF NVVS")
```
<br>  
  
### mml()  
  MMLの文字列を渡すとMMLモードに移行し，その内容に沿ってサウンドが再生されます。  
  MMLモードではnotesやspeedなどの通常のパラメータは無視され，mml()で解除できます。  
  `mml(code)`  
  例 `pyxel.sounds[0].mml("T120 Q90 @1 V100 O5 L8 C4&C<G16R16>C.<G16 >C.D16 @VIB1{10,20,20} E2C2")`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| code | str | MMLの文字列 |  

<br>

``` python
import pyxel
pyxel.init(128, 128)

# mmlメソッドでMMLを登録
pyxel.sounds[0].mml( "T120 Q80 @0 V100 O4 L4 cdefgab>cdefgab>c" )

def update():
    if pyxel.btn(pyxel.KEY_1):
        # サウンドを再生 play(ch, snd, [sec], [loop], [resume])
        pyxel.play(0,0,loop=False)
    
    if pyxel.btn(pyxel.KEY_2):
        # play()の引数でMMLを指定することもできる
        pyxel.play(1,"O5 cdefedc2")
    return

def draw():
    pyxel.cls(0)
    pyxel.text(10,10,"Press 1 or 2 to play.",7)
    return

pyxel.run(update, draw)
```  

<br>  

MMLモード解除の例  
``` python
import pyxel
pyxel.init(128, 128)
pyxel.load("sample.pyxres")  # サンプルのサウンド読み込み

# mmlメソッドでMMLを登録
pyxel.sounds[0].mml( "T120 Q80 @0 V100 O4 L4 cdefgab>cdefgab>c" )

def update():
    if pyxel.btn(pyxel.KEY_1):
        # サウンドを再生 play(ch, snd, [sec], [loop], [resume])
        pyxel.play(0,0,loop=False)
    
    if pyxel.btn(pyxel.KEY_2):
        # MMLモード解除
        pyxel.sounds[0].mml()
    return

def draw():
    pyxel.cls(0)
    pyxel.text(10,10,"Press 1 to play. 2 clr.",7)
    return

pyxel.run(update, draw)
```  

<br> 

MMLのコマンドについては，下記を参考してください。  
  - 公式サイトFAQ [API仕様と使い方 － PyxelのMMLの使い方を教えてください](https://github.com/kitao/pyxel/blob/main/docs/faq-jp.md)    
  - ブログ記事 [Pyxel 2.4版のMMLで音楽を再生する](https://kinutani.hateblo.jp/entry/2025/07/07/230428)  

<br> 

### old_mml()  
  ※ Pyxel 2.4 で 2.3版の mml() を実行する場合はこのメソッドを使います。  
  MMLを使って関連パラメータを設定します。  
  例 `pyxel.sounds[0].old_mml("t120 @1 o3 q6 l8 x0:12345 c4&c<g16r16>c.<g16 v4 >c.&d16 x0 e2~c2~")`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| mml_str | str | MMLの文字列 |  

<br>

　2.3版でのMML使用については，ブログ記事[MMLで音楽データを設定する](https://kinutani.hateblo.jp/entry/2025/01/26/231136)を参照してください。 

<br>
  

### save()  
  サウンドを指定した秒数分再生したWAVファイルを作成します。FFmpegがインストールされている環境で，ffmepgにTrueを指定すると，MP4ファイルも作成します。  
  `save(filename, sec, [ffmpeg])`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| filename | str | ファイル名（拡張子は自動で付加） |  
| sec | float | 再生秒数 |  
| ffmpeg | bool | 省略するとWAVファイルを作成する。<br>Trueを指定するとWAVとMP4ファイルを作成する。 |  

<br>

``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

sec = pyxel.sounds[0].total_sec()
pyxel.sounds[0].save("snd0", sec) # snd0.wav
#pyxel.sounds[0].save("snd0", sec, ffmpeg=True) # snd0.wav , snd0.mp4

pyxel.quit()
```
<br>

### total_sec()  
  サウンドの再生時間を秒で返します。MMLで無限ループが使用されている場合は None を返します。   
  `total_sec()`  

| 戻り値 | 型 | 説明 |
|:---:|:---:|:---|  
| sec | float | 再生時間 (秒) <br>MMLで無限ループの場合 None |  

<br>



## ミュージッククラス  
<br>  

### variable  

|変数名|型|説明|記述例|
|:---:|:---:|:---|:---|
| seqs | リスト | サウンド (0-63) のリストをチャンネル数分連ねた 2 次元リスト | `pyxel.musics[0].seqs` | 


<br>
  
``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

i=0
for msc in pyxel.musics[0].seqs:
    print("ch{}:".format(i),end=" ")
    for snd in msc:
        print(snd,end=" ")
    print("\n")
    i+=1

pyxel.show()
```
  
　サンプルリソース ミュージック0 の seqs の表示結果
<pre>ch0: 0 1 
ch1: 2 3 
ch2: 4 
</pre>

<br>  

> __Note__  
snds_list は Pyxel 2.0で非推奨になりました。 seqs を使用してください。  

<br>  


### set()  
  チャンネルのサウンド (0-63) のリストを設定します。空リストを指定するとそのチャンネルは再生に使用しません。  
  `set(snds0, snds1, snds2, ...)`  

| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| snds0 | リスト | ch0 のサウンド |  
| snds1 | リスト | ch1 のサウンド |  
| snds2 | リスト | ch2 のサウンド |  
| snds3 | リスト | ch3 のサウンド |  

<br>

``` python
pyxel.musics[0].set([0, 1], [], [3])
```
<br>  
  
> __Note__  
set() の引数は Pyxel 2.0.2 で全チャンネル指定が必要なくなりました。  

<br>  

### save()  
  対象のミュージックを指定した秒数分再生したWAVファイルを作成します。FFmpegがインストールされている環境で，ffmepgにTrueを指定すると，MP4ファイルも作成します。  
  `save(filename, sec, [ffmpeg])`  


| 引数 | 型 | 説明 |
|:---:|:---:|:---|
| filename | str | ファイル名（拡張子は自動で付加） |  
| sec | float | 再生秒数 |  
| ffmpeg | bool | 省略するとWAVファイルを作成する。<br>Trueを指定するとWAVとMP4ファイルを作成する。 |  

<br>

``` python
import pyxel
pyxel.init(64, 64)
pyxel.load("sample.pyxres")

sec = 0
for snd_no in pyxel.musics[0].seqs[0]:
    sec += pyxel.sounds[snd_no].total_sec()

pyxel.musics[0].save("msc0", sec) # msc0.wav
#pyxel.musics[0].save("msc0", sec, ffmpeg=True) # msc0.wav , msc0.mp4

pyxel.quit()
```
<br>

> __Note__  
Pyxel 2.4 で save()の引数は再生回数 count 指定から，再生秒数 sec での指定に変更になりました。  

<br>

[ページの先頭に戻る](#pyxel-api-sample)　　[TOPに戻る](../README.md#pyxel-game-development)
