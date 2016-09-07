"""
線形回帰分析（非線形）
データ元：http://archive.ics.uci.edu/ml/datasets/Automobile
"""
import sys
import math
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin_cg

def normalize(X):
    """データを正規化します"""
    ave = np.average(X, axis=0)
    std = np.std(X, axis=0)
    X_normalized = (X - ave) / std
    return X_normalized

def get_x(x, num_of_polynomial):
    """特徴Xを生成します"""
    x_result = np.zeros((x.shape[0], num_of_polynomial))
    for i in range(num_of_polynomial):
        x_result[:,i] = np.array(x ** i)
    return x_result

def show_graph(X, Theta=None, hypothesis_func=None, num_of_polynomial=None):
    """グラフを表示します"""
    min_x = np.amin(X[:,0])
    max_x = np.amax(X[:,0])
    min_y = np.amin(X[:,1])
    max_y = np.amax(X[:,1])
    # データ
    plt.plot(X[:,0], X[:,1], "ro")
    plt.draw()
    if hypothesis_func:
        # 目的関数
        # t  = np.arange(min_x-1, max_x+1, 0.01)
        t  = np.arange(0, max_x+10, 0.01)
        plt.plot(t, hypothesis_func(get_x(t,num_of_polynomial), Theta))
        plt.draw()
    # グラフ設定
    plt.ylabel('price')
    plt.xlabel('engine-size')
    plt.title('車の排気量と価格')
    # plt.axis([min_x-1, np.amax(X[:,0])+1, np.amin(X[:,1])-1, np.amax(X[:,1])+1])
    plt.axis([0, np.amax(X[:,0])+10, 0, np.amax(X[:,1])+1000])
    # グラフ表示
    plt.show()

def compute_cost(x, y, Theta, hypothesis_func):
    """コストを計算します"""
    m = x.shape[0]
    return np.sum((hypothesis_func(x, Theta) - y) ** 2) / 2 / m

def gradient_decent(x, y, Theta, hypothesis_func, alpha, iteration):
    """最急降下法でシータの最適化を行います"""
    # サイズ、入力値、答え
    m = x.shape[0]
    # y = y[:, None]
    # フィッティング
    for i in range(iteration):
        print('-----------')
        hypo = hypothesis_func(x, Theta)
        delta = np.dot((hypo - y[:, None]).T, x)
        Theta = Theta - (alpha / m) * delta.T
        # print(hypo.shape, delta.shape, Theta.shape)
        # print((alpha / m) * delta.T)
        print(Theta)
        cost = compute_cost(x, y, Theta=Theta, hypothesis_func=hypothesis)
        print("cost=", cost)

    # 返却
    return Theta

def hypothesis(x, Theta):
    """目的関数です"""
    return np.dot(x,Theta)

def normal_equation(x, y):
    return np.dot(np.dot(np.linalg.pinv(np.dot(x.T, x)), x.T), y[:,None])

if __name__ == "__main__":

    # 項目数
    num_of_polynomial = 5

    # データ取得
    X = np.loadtxt("./automobile_all.txt", delimiter=",")
    # X = normalize(X)

    # データを取り出す
    x = get_x(X[:, 0], num_of_polynomial)
    y = X[:, 1]

    print(x.shape)

    # Theta = normal_equation(x, y)
    # print(Theta)
# 
    # sys.exit(0)

    # 最適化する項目
    Theta = np.zeros(num_of_polynomial)[:,None]
    # print(Theta.shape)

    # データ表示（初期状態）
    show_graph(X, Theta=Theta, 
        hypothesis_func=hypothesis, num_of_polynomial=num_of_polynomial)

    # 初期コスト
    cost = compute_cost(x, y, Theta=Theta, hypothesis_func=hypothesis)
    print("Initial Cost = ", cost)

    # コスト最小化する
    # alpha = 0.00001 #5:0.0001, 6:0.00001
    # iteration = 50000
    # Theta = gradient_decent(x, y, Theta, hypothesis, alpha, iteration)
    Theta = normal_equation(x, y)
    # print(Theta)

    # コスト（最適化後）
    cost = compute_cost(x, y, Theta=Theta, hypothesis_func=hypothesis)
    print("Optimized Cost = ", cost)

    # データ表示（最適化後）
    show_graph(X, Theta=Theta, 
        hypothesis_func=hypothesis, num_of_polynomial=num_of_polynomial)

