# 随机取样本索引
import random
random.seed(1)
row, col = 4, 4
random_idxs = random.sample(range(len(data)), rows * cols)
