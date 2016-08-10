このページではPythonの変数定義と型変換について説明します。  
<br>
<br>
# 変数の定義
変数の定義は、以下のように行い、`type`を用いることで型を調べることができます。  
## 文字列
```
my_name = "Yohei Munesada"
print(my_name)
print(type(my_name)) # <class 'str'>
```
## 数値
```
age = 30
print(type(age)) # <class 'int'>

load_average = 0.65
print(type(load_average)) # <class 'float'>
```
## リスト
```
chars = [“A”, “B”, “C”]
print(type(chars)) # <class ‘list’>
```
## Range
```
my_range = range(0, 10)
print(type(my_range)) # <class ‘range’>
```
<br />
<br />
# 変数の型変換
異なる型同士で結合したり比較する場合には、型変換が必要です。  
## 異なる型同士を結合するとエラー
```
name = "Yohei"
age = 30
message = name + age
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'int' object to str implicitly
```
## 異なる型を結合する時には、型変換を行う
```
message = name + str(age)
```
## 異なる型同士で比較してもダメ
```
age1 = 30
border = "32"
ok = age1 <= border
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: int() <= str()
```
## 異なる型を結合する場合にも、型変換が必要
```
ok = age1 <= int(border)
```
