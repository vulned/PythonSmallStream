import numpy as np

arr1 = np.array([
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 7, 9],
    [12,14,16,18]
    ])
print (arr1)

# 一位数组元素获取4ways
age = np.array([13, 19, 22, 14, 19, 11])

# 下标，切片，间断索引
print(age[-1], age[0:3], age[[0, 3, 5]])

# 布尔索引（常用），or逻辑索引。因为6000w条，不能用肉眼
print(
    age[age < 18]
    )

# 取出18
print(arr1[3][3])

# 取第4行
print(arr1[3])
print(arr1[3,:])

# 取第2列
print(arr1[:,1])
