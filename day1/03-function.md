このページでは、Python関数について説明しています。
<br>
# 基本的な定義と呼び出し方
## 関数の定義
関数は`def`キーワードを使って定義します。
```python
def say_hello():
  print("Hello")
```
以下のように引数を受け取ることもできます。
```python
def say_hello(name):
  print("Hello, " + name)
```
また、値を返却することもできます。
```python
def get_message(name):
  return "Hello, " + name
```
## 関数の呼び出し
関数は以下のように利用することができます。
```python
say_hello()
say_hello("Yohei")
message = get_message("Mizuno")
```
<br>
# キーワード引数による値の指定
例えば以下のような、引数を取る関数があったとします。
```python
def get_message(name, age):
  return "%s is %d years old" % (name, age)
```
この場合に、以下のように値を指定して関数を呼び出すことができます。
```python
message = get_message(name="Kobayashi", age=33)
```
この指定をキーワード引数と呼び、例えば引数が10個以上ある時などに便利です（日付系の処理では引数が10個以上あることもよくあります）。
# デフォルト値の設定
また、関数の定義部分で、初期値を設定することができます。
```python
def get_message(name, age=20):
  return "%s is %d years old" % (name, age)
```
この場合、呼び出し側で`age`を省略して以下のように呼び出すことができます。
```python
message = get_message("Yohei")
message = get_message(name="Yohei")
```
とこんな感じで便利です。
<br>
# 他にも
ちょっと高度なこととして、以下のようなこともできますので参考まで。
 * [[Python] *を用いて位置引数をタプル化する](http://www.yoheim.net/blog.php?q=20160609)
 * [[Python] **を用いたキーワード引数の辞書化](http://www.yoheim.net/blog.php?q=20160610)
