#
# 共通処理 - Python Lecture Day2
#
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    """線形回帰に利用するデータを読み込みます"""
    X = np.loadtxt("./automobile.txt", delimiter=",")
    return X.tolist(), X[:,0].tolist(), X[:,1].tolist()

def show(data, x_vals=None, y_vals=None, Theta=None, hypothesis_func=None):
    """グラフ表示を行います"""
    X = np.array(data)
    min_x = 0
    max_x = np.amax(X[:,0]) + 10
    min_y = 0
    max_y = np.amax(X[:,1]) + 1000
    # データをプロットします
    plt.plot(X[:,0], X[:,1], "ro")
    plt.draw()
    # 回帰直線の表示
    if hypothesis_func:
        t  = np.arange(min_x, max_x, 0.01)
        plt.plot(t, hypothesis_func(t.tolist(), Theta))
        plt.draw()
    # グラフ設定
    plt.ylabel('price')
    plt.xlabel('engine-size')
    plt.title('車の排気量と価格')
    plt.axis([min_x, max_x, min_y, max_y])
    # グラフ表示
    plt.show()
