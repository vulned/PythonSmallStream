import numpy as np, random

# 两个array运算，要求同形，无论数学运算还是比较运算

# 整除//

# 常用数学函数

# np.round, np.sqrt, np.squrae, np.exp, np.power, np.log2, np.log10, np.log


# 常用统计函数

# np.min, np.max, np.median, np.sum, np.std, np.var(arr, axis)

##arr02 = np.array([])
##k = 0
##v = 0
##
##for k in range(4):
##    for v in range(4):
##        arr02[k][v] = random.random()
##
##print(arr02)

arr02 = np.random.randint(10,size=[4, 4])

print(arr02)

sum = []
mean = []

for row in range(4):
    sum.append(np.sum(arr02[row,:]))
print(sum)

for col in range(4):
    mean.append(np.mean(arr02[:,col]))
print(mean)

# axis使用，胖0，瘦1
# 瘦子求行的和
row01 = arr02.sum(axis = 1)  # 数组对象方法
row02 = np.sum(arr02, axis = 1)  # numpy对象方法

print(row01, row02)

# 胖子求列平均值
col03 = arr02.mean(axis = 0)
col04 = np.mean(arr02, axis = 0)
print(col03, col04)
