import pandas as pd
import numpy as np
# index = 0
# l = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
#     0,
#     0,
#     1,
#     0,
#     0,
# ], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# x = pd.DataFrame(l)

# for i, row in x.iterrows():
#     if sum(row) == 1:
#         print('row: {}'.format(i))

# for i, column in x.iteritems():
#     if sum(column) == 1:
#         print('colunn: {}'.format(i))

x = [1, 1, 2]
l = [1, 2, 3]
x.append(l)
print(len(x) - 1)
