"""
機械学習事始め：線形回帰分析

データ元：http://archive.ics.uci.edu/ml/datasets/Automobile
"""
import math
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    """データを読み込みます"""
    data = [t.split(",") for t in open("../data.text").read().split("\n")]
    data = [[int(d[0]), int(d[1])] for d in data]
    return data

def show_graph(data, h=None, theta=None):
    """グラフ表示"""
    X = np.array(data)
    x = X[:, 0]
    y = X[:, 1]
    plt.plot(x, y, "ro")
    plt.draw()
    if h:
        x_min = 0
        x_max = np.amax(x)
        y_from = h(0,theta)
        y_to = h(x_max,theta)
        plt.plot([x_min, x_max], [y_from, y_to])
        # plt.plot([1,4])
        plt.draw()
    # TODO 軸のレンジ、軸の名前、ウィンドウの大きさ、プロットしたやつの色と形
    plt.ylabel('price')
    plt.show()

def compute_cost(X, y, theta):
    cost = 0
    for i, x in enumerate(X):
        pred = x * theta
        real = y[i]
        print(pred, real, (pred-real), math.pow(pred-real, 2))
        cost += math.pow(pred - real, 2)
    cost = cost / (2*len(X))
    return cost

def gradient_decent(X, y, theta, alpha, iteration):

    print("\ttheta=", theta)
    
    for i in range(iteration):

        delta = 0
        for j, x in enumerate(X):
            delta += (x*theta - y[j]) * x
            # print((x*theta - y[i]) * x)
        delta = delta / len(X)
        theta = theta - alpha*delta
        # print(delta, theta)
        print("\t(%d)theta=%f" % (i+1, theta))

    return theta


if __name__ == "__main__":

    # データ取得
    data = load_data()
    X = [d[0] for d in data]
    y = [d[1] for d in data]

    # グラフ表示
    show_graph(data)

    # 目的関数
    h = lambda x,theta:x*theta
    theta = 1
    show_graph(data, h, theta)

    # 初期コスト
    initial_cost = compute_cost(X, y, theta)
    print("initial_cost:", initial_cost)

    # 最適化
    alpha = 0.000001
    iteration = 500
    theta = gradient_decent(X, y, theta, alpha, iteration)
    print("theta_optimized=", theta)

    # 最適化後のコスト
    optimized_cost = compute_cost(X, y, theta)
    print("optimized_cost:", optimized_cost)

    # グラフ表示
    show_graph(data, h, theta)




# b = 0で最適化
##===============================

















