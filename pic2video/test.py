import numpy as np

x = -40
y = -60
z = 120
f = 30
dpi = 37.8
matrix_1 = np.array([[f / 10, 0, 0], [0, f / 10, 0], [0, 0, 1]])
matrix_2 = np.array([[x / z], [y / z], [1]])

two_multi_res = np.dot(matrix_1, matrix_2)
print('two_multi_res: %s' % two_multi_res)
x0 = two_multi_res[0][0] * dpi
y0 = two_multi_res[1][0] * dpi
print(x0, y0)
# 37.8
# 189   -246
# -38  -57
frame = 300
delta_x = 189 + 38
delta_y = 246 - 57
print(delta_x, delta_y)
# 227  189
x = [189]
y = [-246]
for i in range(frame-1):
    x.append(x[-1] - delta_x / (frame-1))
    y.append(y[-1] + delta_y / (frame-1))
print(x)
print(y)

delta_x = 200 + 40
delta_y = 260 - 60
print(delta_x, delta_y)
# 220  0
x = [200]
y = [-260]
for i in range(frame - 1):
    x.append(x[-1] - delta_x / (frame-1))
    y.append(y[-1] + delta_y / (frame-1))
print(x)
print(y)
