このページではPythonの基本文法について説明します。
<br>
# if文
条件によって分岐して処理を行います。
## 基本形
`if`と`elif`と`else`を利用します。
```
if name == "Yohei":
  print("Good")

elif name == "Yosuke":
  print("Normal")

else:
  print("Bad")
```
## 複数の条件の組み合わせ
複数の条件を組み合わせる場合には`and`や`or`を使います。
```
if name == "Mizuno" and age == 32:
  print("Good")

elif name == "Kobayashi" or age = 30:
  print("Normal")
```
## if文と代入
以下のようにif文を用いて三項演算子のような実装を行うことができます。人によっては「直感的な実装だ」と言います（僕はそっち派です）。
```
age = 29
judge = "young" if age < 30 else "elder"
```
<br>
# for文
指定回数や要素数分の処理を行います。
## 指定回数処理を行う
`range`を用いることで指定回数の処理が行えます。
```
for i in range(0, 10):
  print(i)
```
## 要素数分の処理を行う
`list`や`set`など複数の要素を保持するものについて、要素1つずつ処理を行えます。
```
for ch in ["a", "b", "c", "d", "e"]:
  print(ch)
```
## breakでループ停止
`break`を用いることでループを抜け出すことができます。
```
for i in range(0, 10):
  if i == 5:
    break
```
<br>
# while文
条件に合致し続ける限りループ処理を行います。
```
num = 10
for num >= 5:
  num -= 1
```
<br>
<br>
# passによる空行の主張
Pythonではコードブロックをインデントで表現しますが、以下のようにコードブロックに何もない場合はエラーとなります。
```
if name == "Yohei":

```
エラー内容は以下です。
```
IndentationError: expected an indented block
```
何も実装しないコードブロックを用意する場合、`pass`を記述することでエラーを回避できます。
```
if name == "Yohei":
  pass
```
