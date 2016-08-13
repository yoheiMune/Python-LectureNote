このページでは、Pythonの基本文法について説明します。
<br>
# if文
条件によって処理を分岐します。
## 基本形
`if`と`elif`と`else`を利用します。
```python
if name == "Yohei":
  print("Good")

elif name == "Yosuke":
  print("Super Good")

else:
  print("Excellent")
```
## 複数の条件の組み合わせ
複数の条件を組み合わせる場合には`and`や`or`を使います。
```python
if name == "Mizuno" and age == 32:
  print("Good")

elif name == "Kobayashi" or age = 30:
  print("Normal")
```
## if文と代入
以下のようにif文を用いて三項演算子のような実装を行うことができます。人によっては「直感的な実装だ」と言います。
```python
age = 29
judge = "young" if age < 30 else "elder"
```
<br>
# for文
指定した回数処理したり、要素を1つずつ処理することができます。
## 指定回数処理を行う
`range`を用いることで指定回数の処理が行えます。
```python
for i in range(0, 10):
  print(i)
```
## 要素数分の処理を行う
`list`や`set`など複数の要素を保持するものについて、要素1つずつ処理を行えます。
```python
for ch in ["a", "b", "c", "d", "e"]:
  print(ch)
```
## breakでループ停止
`break`を用いることでループを抜け出すことができます。
```python
for i in range(0, 10):
  if i == 5:
    break
```
<br>
# while文
条件に合致し続ける限りループ処理を行います。
```python
num = 10
for num >= 5:
  num -= 1
```
<br>
# passによる空行の主張
Pythonではコードブロックをインデントで表現しますが、以下のようにコードブロックに何もない場合はエラーとなります。
```python
if name == "Yohei":

```
エラー内容は以下です。
```python
IndentationError: expected an indented block
```
何も実装しないコードブロックを用意する場合、`pass`を記述することでエラーを回避できます。
```python
if name == "Yohei":
  pass
```
