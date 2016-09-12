#
# 線形回帰（線形）の演習
#
# [演習2]
#　ここでは「y = ax + b」の回帰直線を用いて、線形回帰を実装します。
#　（ex1からの発展系です）。
# 
# [実装説明]
# 以下3つの関数を実装して、完成させてください。
#   ・hypothesis : 仮説関数の実装
#   ・compute_cost：コスト関数の実装
#   ・gradient_descent：最急降下法の実装
# 
# [注意]
# 今回は、Thetaが配列となります（Theta0とTheta1の値を持つ）。
#
# [演習の回答]
# この演習の回答は「ex2_answer.py」にあります。
# 
# では、幸運を祈ります！！！
# 
from pprint import pprint
import numpy as np
import common as cmn

def hypothesis(x_vals, Theta):
    """
        原点を通るように回帰直線を定義します。

        ここでは、引数で与えられた「x_vals」と「Theta」を用いて、
        仮説関数の実行結果（線形回帰の予測値）を返却してください。

        入力値：
            x_vals  : インプットデータ（[1,2,3]のような配列データ）
            Theta   : パラメータ（[10,10]などの配列）

        返却値：
            モデルの予測値（入力値と同じ配列形式）
    """
    #
    # TODO この関数を実装して下さい
    #
    # return -1
    hypo = [Theta[0] + x*Theta[1] for x in x_vals]
    return hypo

def compute_cost(x_vals, y_vals, Theta, hypothesis_func):
    """
        原点を通る回帰直線についてのコストを計算します

        引数で与えられた内容をもとに、予測モデルのコストを計算して返却します。

        入力値：
            x_vals          : インプットデータ（[1,2,3]のような配列データ）
            y_vals          : 入力値に対する実際の値（配列形式、要素数はx_valsと同じ）
            Theta           : パラメータ（「10」などの実数値）
            hypothesis_func : 仮説関数

        返却値：
            モデルのコスト（形式は実数を返す）
    """
    #
    # TODO この関数を実装して下さい
    #
    # return -1
    m = len(data)
    hypo = hypothesis_func(x_vals, Theta)
    cost = (1/2/m) * sum([(h-y)**2 for h, y in zip(hypo,y_vals)])
    return cost

def gradient_descent(x_vals, y_vals, Theta, hypothesis_func, alpha, iteration):
    """
        最急降下法を用いて、最適化を行います

        引数で与えられた内容をもとに、予測モデルのコストを計算して返却します。

        入力値：
            x_vals          : インプットデータ（[1,2,3]のような配列データ）
            y_vals          : 入力値に対する実際の値（配列形式、要素数はx_valsと同じ）
            Theta           : パラメータ（[10,10]などの配列）
            hypothesis_func : 仮説関数
            alpha           : Thetaを変化させる量を調整するパラメータ
            iteration       : 最急降下法を実施する回数

        返却値：
            最適化後のTheta値（配列で返却する）
    """
    #
    # TODO この関数を実装して下さい
    #
    print('-----------------\n#最急降下法')
    m = len(x_vals)
    for i in range(iteration):
        hypo = hypothesis_func(x_vals, Theta)
        # Theta0について
        delta = (1/m) * sum([(h-y) for h,x,y in zip(hypo,x_vals,y_vals)])
        Theta0 = Theta[0] - alpha * delta
        # Theta1について
        delta = (1/m) * sum([(h-y)*x for h,x,y in zip(hypo,x_vals,y_vals)])
        Theta1 = Theta[1] - alpha * delta
        # 値は同時に更新します
        Theta = [Theta0, Theta1]
        cost = compute_cost(x_vals, y_vals, Theta, hypothesis_func)
        print("cost=%f, Theta0=%f, Theta1=%f" % (cost, Theta[0], Theta[1]))
    return Theta


if __name__ == "__main__":

    # 01. データを読み込む
    #---------------------------------------------
    # 今回利用するデータを読み込みます
    data, x_vals, y_vals = cmn.load_data()
    # 上10件ほど、見てみましょう
    print('-----------------\n#今回利用するデータ（上10件）')
    pprint(data[:10])
    # データをグラフに表示します
    cmn.show(data)


    # 02. （最適化前）予測とコストを計算する
    #---------------------------------------------
    # 初期値のシータは10にしておきます（別の値でも良いです）
    # 「Theta0 = 10, Theta1 = 10」の意味です。
    Theta = [10, 10]
    # このシータを使って、上位10件のデータの予測を作ってみましょう
    hypo = hypothesis(x_vals, Theta)
    # 上位3件の予測結果を表示します（最適化前）
    print('-----------------\n#回帰直線（最適化前）（上3件）')
    pprint(hypo[:3])
    # 以下の値が表示されればOKです
    # [1310.0, 1310.0, 1530.0]

    # データと回帰直線をグラフに表示します
    cmn.show(data, x_vals, y_vals, Theta, hypothesis_func=hypothesis)
    
    # 初期コストを計算します
    cost = compute_cost(x_vals, y_vals, Theta, hypothesis_func=hypothesis)
    print('-----------------\n# コスト（最適化前）')
    print("cost=", cost)
    # 以下の値が表示されればOKです
    # cost= 99903174.68905473


    # 03. 回帰直線の最適化（最急降下法）
    #---------------------------------------------
    alpha = 0.00001
    iteration = 50
    Theta_optimized = gradient_descent(x_vals, y_vals, Theta, hypothesis, alpha, iteration)
    # 最適化後の状態をグラフに表示します
    cmn.show(data, x_vals, y_vals, Theta_optimized, hypothesis_func=hypothesis)


    # 04. 最適化後
    #---------------------------------------------
    # 上位3件の予測結果を表示します（最適化後）
    hypo = hypothesis(x_vals, Theta_optimized)
    print('-----------------\n#回帰直線（最適化後）（上3件）')
    pprint(hypo[:3])
    # 以下の値が表示されればOKです
    # [14319.03000935717, 14319.03000935717, 16740.5026091183]

    # 最適化後のコスト
    cost = compute_cost(x_vals, y_vals, Theta_optimized, hypothesis_func=hypothesis)
    print('-----------------\n# コスト（最適化後）')
    print("cost=", cost)
    # 以下の値が表示されればOKです
    # cost= 10575424.510240488












