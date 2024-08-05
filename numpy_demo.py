import numpy as np

arr = np.array([[7,8,9], [4,5,6,]])
print(arr)
import numpy as np

a = np.array([1,2,3,4])
two_d = np.array([[1,2,3], [4,5,6], [7,8,9]])
a[0] = 12
b = a[1:]
b[0] = 23
# print(b[:])
# print(a[:])
print(two_d)
print(two_d[1,2])
print(two_d[1][2])