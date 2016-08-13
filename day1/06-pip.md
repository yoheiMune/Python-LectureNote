このページでは、Pythonのパッケージマネージャーであるpipを説明します。  
<br>
# pipとは
pipとはパッケージマネージャーの1つで、このツールを使うことで簡単に外部のモジュールを導入することができます。Rubyでいうgem、Node.jsでいうnpmに相当します。  
<br>
# pipによるインストール
pipを用いてパッケージのインストールを行うことができます。
```sh
$ pip install --upgrade beautifulsoup4
```
また、以下のようにバージョンを指定してインストールすることもできます。
```sh
pip install Flask==0.10.1
```
バージョン指定は時々使います（古いものじゃなきゃうごかないぞーとなった時に一時しのぎで）。  
<br>
# アンインストール
アンインストールは以下のように行います。
```sh
$ pip uninstall Flask
```
<br>
# pipによるパッケージ検索
pipでインストール可能なモジュールを検索することができます。
```sh
$ pip search pycrypto
```
<br>
# アップグレード
インストール済みのモジュールは`--upgrade`オプションを指定して最新バージョンにすることができます。<br>
```sh
$ pip install --upgrade pycrypto
```
<br>
# インストール済みのパッケージ
インストール済みの一覧を以下で表示することができます。
```sh
$ pip list
```
<br>
# ヘルプ
pipのヘルプは`help`コマンドで見ることができます。
```sh
# pip全体のヘルプ
$ pip help

# pipのコマンドのヘルプ
# pip [コマンド名] help
pip install help # インストールコマンドのヘルプ
```