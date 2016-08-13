このページでは、PythonによるHTTP通信を説明します。  
<br>
# 利用するモジュール
標準で組み込まれている以下のモジュールを利用します。
```python
import urllib.request
```
<br>
# 基本的な使い方
`urllib.request`モジュールを用いることで、簡単にHTTP通信を行うことができます。
```python
res = urllib.request.urlopen("http://www.yoheim.net")
html = res.read().decode("utf-8")
```
これでYoheiM.NETのトップページからHTMLを取得できました。  
<br>
# GETパラメータをつける
上記の実装に加え、以下のように実装することでGETパラメータを付与することができます。
```python
import urllib.request
import urllib.parse
data = {
    "name": "Yohei",
    "age": 32
}
p = urllib.parse.urlencode(data)
url = "http://www.yoheim.net/?" + p
res = urllib.request.urlopen(url)
html = res.read().decode("utf-8")
```
<br>
# POST通信を行う
今まではGET通信でしたが、以下のように実装することでPOST通信を行うことができます。
```python
import urllib.request
import urllib.parse
data = {
    "name": "yohei",
    "age": 30,
    "comment": "あああ"
}
# ここでエンコードして文字→バイトにする！
data = urllib.parse.urlencode(data).encode("utf-8")
res = urllib.request.urlopen("http://www.yoheim.net/", data=data)
html = res.read().decode("utf-8")
```
ちょっとだけ複雑になりましたが、これくらいのコード量で簡単にPOST通信を行うことができます。  
<br>
# withキーワードを用いたリソース管理
`with`を用いることでコードブロックの処理が終わった場合に、自動的にリソースをクローズしてくれます。
```python
with urllib.request.urlopen("http://www.yoheim.net") as res:
   html = res.read().decode("utf-8")
```
<br>
# さらに詳しく
以下のブログにもう少し詳しく記載していますので参考になれば。
 * [[Python] HTTP通信でGetやPostを行う](http://www.yoheim.net/blog.php?q=20160204)
