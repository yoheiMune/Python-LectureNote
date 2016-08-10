このページでは、Pythonのモジュールとパッケージについて説明します。
<br>
# モジュール
## モジュールとは
モジュールとは複数の処理を1つのファイルにまとめたものです。
## モジュールの実装例
以下2つのファイルがあると想定して話を進めます。
 - (ルート)
    - my_module.py （モジュール）
    - main.py（メインで起動するもの）
<br>
モジュールは以下の関数が定義されているとします。
```python
# my_module.py
def get_genius():
  return ["Yamazaki", "Kosuge"]
```
この場合に`main.py`から`my_module.py`を以下のように利用します。
```python
import my_module
genius = my_module.get_genius()
```
`import`については`as`を用いて別名を定義することができます。
```python
import my_module as mm
genius = mm.get_genius()
```
また、`from`と合わせて使うことで以下のようにインポートすることも可能です。
```python
from my_module import get_genius
genius = get_genius()
```
<br>
# パッケージ
パッケージは複数のモジュールを1つにまとめたものです。
## パッケージの実装例
以下のディレクトリ構成を想定しています。









__main__