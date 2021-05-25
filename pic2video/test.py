import numpy as np

x = 180
y = 48
z = 100
f = 30
matrix_1 = np.array([[f/10, 0, 0], [0, f/10, 0], [0, 0, 1]])
matrix_2 = np.array([[x / z], [y / z], [1]])

two_multi_res = np.dot(matrix_1, matrix_2)
print('two_multi_res: %s' % two_multi_res)
print(two_multi_res[0][0] * 37.8, two_multi_res[1][0] * 37.8)
# 5.4   1.44
# 37.8
# 204   54
