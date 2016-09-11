"""
線形回帰分析
データ元：http://archive.ics.uci.edu/ml/datasets/Automobile
"""
import sys
import math
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def show_graph(X, Theta=None, hypothesis_func=None):
    """グラフを表示します"""
    # データ
    plt.plot(X[:,0], X[:,1], "ro")
    plt.draw()    
    if hypothesis_func:
        # 目的関数
        max_x = np.amax(X[:, 0]) + 100
        t  = np.arange(0, max_x, 0.1)
        plt.plot(t, hypothesis_func(np.c_[np.ones(len(t)),t], Theta))
        plt.draw()
    # グラフ設定
    plt.ylabel('price')
    plt.xlabel('engine-size')
    plt.title('車の排気量と価格')
    plt.axis([0, np.amax(X[:,0])+100, 0, np.amax(X[:,1])+10000])
    # グラフ表示
    plt.show()

def compute_cost(X, Theta, hypothesis_func):
    """コストを計算します"""
    m = X.shape[0]
    x = np.c_[np.ones(m), X[:,0]]
    y = X[:,1]
    return np.sum((hypothesis_func(x, Theta) - y) ** 2) / 2 / m

def gradient_decent(X, Theta, hypothesis_func, alpha, iteration):
    """最急降下法でシータの最適化を行います"""
    # サイズ、入力値、答え
    m = X.shape[0]
    x = X[:,0]
    x = np.c_[np.ones(len(x)), x]
    y = X[:,1][:,None]
    # フィッティング
    for i in range(iteration):
        hypo = hypothesis_func(x, Theta)
        delta = np.dot((hypo - y).T, x)
        Theta = Theta - (alpha / m) * delta.T
        print('-----------')
        print(Theta[0], Theta[1])
    # 返却
    return Theta

def hypothesis(x, Theta):
    """目的関数です"""
    return np.dot(x,Theta)

if __name__ == "__main__":

    # データ取得
    X = np.loadtxt("./automobile_all.txt", delimiter=",")

    # 最適化する項目
    Theta = np.array([1, 10])[:,None]

    # データ表示（初期状態）
    show_graph(X, Theta=Theta, hypothesis_func=hypothesis)

    # 初期コスト
    cost = compute_cost(X, Theta=Theta, hypothesis_func=hypothesis)
    print("Initial Cost = ", cost)

    # コスト最小化する
    alpha = 0.00001
    iteration = 100
    Theta = gradient_decent(X, Theta, hypothesis, alpha, iteration)
    print(Theta)

    # コスト（最適化後）
    cost = compute_cost(X, Theta=Theta, hypothesis_func=hypothesis)
    print("Optimized Cost = ", cost)

    # データ表示（最適化後）
    show_graph(X, Theta=Theta, hypothesis_func=hypothesis)

