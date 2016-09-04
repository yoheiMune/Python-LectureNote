"""
機械学習事始め：線形回帰分析

データ元：http://archive.ics.uci.edu/ml/datasets/Automobile
"""
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

# データ読み込み
data = [t.split(",") for t in open("../data.text").read().split("\n")]
data = [[int(d[0]), int(d[1])] for d in data]
pprint(data)

# グラフ表示
X = np.array(data)
x = X[:, 0]
y = X[:, 1]
plt.plot(x, y, "bo")
# TODO 軸のレンジ、軸の名前、ウィンドウの大きさ、プロットしたやつの色と形
plt.show()

# b = 0で最適化
##===============================

















