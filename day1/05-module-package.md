このページでは、Pythonのモジュールとパッケージについて説明します。  
<br>
# モジュール
## モジュールとは
モジュールとは複数の処理を1つのファイルにまとめたものです。
## モジュールの実装例
以下2つのファイルがあると想定して話を進めます。
 - (ルート)
  - main.py（メインで起動するもの）  
  - my_module.py （モジュール）  
<br>
モジュールは以下の関数が定義されているとします。
```python
# my_module.py
def get_genius():
  return ["Yamazaki", "Kosuge"]
```
この場合に`main.py`から`my_module.py`を以下のように呼び出すことができます。
```python
import my_module
genius = my_module.get_genius()
```
`import`については`as`を用いて別名を定義することができます。
```python
import my_module as mm
genius = mm.get_genius()
```
また、`from`を使って、以下のようにインポートすることも可能です。
```python
from my_module import get_genius
genius = get_genius()
```
<br>
# パッケージ
パッケージは複数のモジュールを1つにまとめたものです。
## パッケージの実装例
以下のディレクトリ構成があるとしましょう。パッケージのディレクトリの中には`__init__.py`ファイルを置き、このディレクトリがPythonのパッケージであることを示します。
* (ルート)
    * main.py（メインで起動するもの）  
    * mypackage
        * \_\_init\_\_.py（空ファイルで良いが必須）
        * my_module1.py
        * my_module2.py  


mypackage以下のそれぞれのモジュールは以下の関数が定義されていることとしましょう。
```python
# my_module1.py
def get_genius():
  return "Yamazaki"
```
```python
# my_module2.py
def get_best_staff():
  return "Kuribayashi"
```
それらモジュールを`main.py`から用いる場合には、以下のように行います。
```python
# main.py
import mypackage.my_module1
import mypackage.my_module2

genius = mypackage.my_module1.get_genius()
staff = mypackage.my_module2.get_best_staff()
```
また上述のモジュールと同じく、インポートの方法はいろいろとあります。
```python
# エイリアスを用いる
import mypackage.my_module1 as mm1
import mypackage.my_module2 as mm1
```
```python
# fromを用いる
from mypackage import my_module1
from mypackage import my_module2

# また、以下のようにまとめて記述も可能
from mypackage import my_module1, my_module2
```
<br>
# \_\_main\_\_の処理
Pythonでは（モジュールとしてではなく）メインのプログラムとして呼び出された場合にのみ実行されるコードを書くことができます。
```python
# my_module1.pyの例

# モジュールとして提供する関数
def get_genius():
  return "Yamazaki"

# メインで呼び出された時にのみ実行されるコードはここに書く
if __name__ == "__main__":
  print("メインで呼び出された時に実行するコード")
```
モジュールとして機能を提供しつつメインとしても利用するものは、意識して分けて書くと良いです。