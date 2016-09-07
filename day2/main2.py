"""
線形回帰分析
データ元：http://archive.ics.uci.edu/ml/datasets/Automobile
"""
import sys
import math
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    """データを読み込みます"""
    return np.loadtxt("./automobile_all.txt", delimiter=",")

def show_graph(X, Theta=None, hypothesis_func=None):
    """グラフ表示"""
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
    m = X.shape[0]
    x = X[:, 0]
    x = np.c_[np.ones(len(x)),x]
    y = X[:, 1]
    return np.sum((hypothesis_func(x, Theta) - y) ** 2) / 2 / m
    # cost = 0
    # for i, x in enumerate(X):
    #     pred = x * theta
    #     real = y[i]
    #     print(pred, real, (pred-real), math.pow(pred-real, 2))
    #     cost += math.pow(pred - real, 2)
    # cost = cost / (2*len(X))
    # return cost

def gradient_decent(X, Theta, hypothesis_func, alpha, iteration):

    # 入力値（x0を追加）
    m = X.shape[0]
    x = X[:,0]
    x = np.c_[np.ones(len(x)), x]
    # 答え
    y = X[:,1][:,None]

    for i in range(iteration):
        hypo = hypothesis_func(x, Theta)
        delta = np.dot((hypo - y).T, x)
        print('-----------')
        # print(hypo.shape, y.shape, x.shape, delta.shape, Theta.shape)
        Theta = Theta - (alpha / m) * delta.T
        print(Theta[0], Theta[1])


        # hypo = X * theta;
        # delta = transpose(hypo - y) * X;
        # theta = theta - (alpha / m) * transpose(delta);










        # print(x.shape, Theta.shape, hypothesis_func(x, Theta).shape)
        # delta = np.sum(hypothesis_func(x, Theta) - y) * x / m
        # print(np.sum(hypothesis_func(x, Theta) - y, axis=0))




    
    # for i in range(iteration):

    #     delta = 0
    #     for j, x in enumerate(X):
    #         delta += (x*theta - y[j]) * x
    #         # print((x*theta - y[i]) * x)
    #     delta = delta / len(X)
    #     theta = theta - alpha*delta
    #     # print(delta, theta)
    #     print("\t(%d)theta=%f" % (i+1, theta))

    return Theta

def hypothesis(x, Theta):
    return np.dot(x,Theta)


if __name__ == "__main__":

    # データ取得
    X = np.loadtxt("./automobile_all.txt", delimiter=",")
    x = X[:, 0]
    y = X[:, 1]
    # x0を追加
    x = np.c_[np.ones(len(x)), x]

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



    # X = [d[0] for d in data]
    # y = [d[1] for d in data]

    # # グラフ表示
    # show_graph(data)

    # # 目的関数
    # h = lambda x,theta:x*theta
    # theta = 1
    # show_graph(data, h, theta)

    # # 初期コスト
    # initial_cost = compute_cost(X, y, theta)
    # print("initial_cost:", initial_cost)

    # # 最適化
    # alpha = 0.000001
    # iteration = 500
    # theta = gradient_decent(X, y, theta, alpha, iteration)
    # print("theta_optimized=", theta)

    # # 最適化後のコスト
    # optimized_cost = compute_cost(X, y, theta)
    # print("optimized_cost:", optimized_cost)

    # # グラフ表示
    # show_graph(data, h, theta)




# b = 0で最適化
##===============================

















