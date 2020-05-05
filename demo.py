import numpy as np
from km_matcher import KMMatcher



'''
weights = np.array([
    [2, 3, 0, 3],
    [0, 4, 4, 0],
    [5, 6, 0, 0],
    [0, 0, 7, 0]

    # [-2, -6, -4],
    # [-3, -1, -2],
    # [-5, -4, -3]

    # [3, 0, 4],
    # [2, 1, 3],
    # [0, 0, 5]

]).astype(np.float32)
'''

matcher = KMMatcher([
    [2, 3, 0, 3],
    [0, 4, 4, 0],
    [5, 6, 0, 0],
    [0, 0, 7, 0]
])

matcher.solve(verbose=True)



import time

n, m = 10, 1000000

weights = np.random.randn(n, m)

st = time.time()
matcher = KMMatcher(weights)
best = matcher.solve()
ed = time.time()

print('time consuming of size ({}, {}) is {:.4f} seconds'.format(n, m, ed - st))



