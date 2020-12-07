#! usr/bin/env python
# coding: utf-8
# 学习numpy中矩阵的代码笔记
# 2018年05月29日15:43:40
# 参考网站：http://cs231n.github.io/python-numpy-tutorial/
import numpy as np

# ==================矩阵的创建，增删查改，索引，运算=================================#

# ==================矩阵的创建，增删查改=================================#
# # 创建行向量
x = np.array([1,2,3])
# 修改某个值
x[0] = 0
# 注意下标索引从0开始，与MATLAB不一样
print(x)
print(x.shape)
print(type(x))

# 创建二维与多维矩阵
matrix = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [2, 3, 4]
])

# 取出某个元素
a01 = matrix[0][0]
print(a01)
# (3, 3)表示：(Row)3行(Columns)3列
print(matrix.shape)

# # # 创建特殊矩阵
# # 0矩阵
zeros = np.zeros((2,2))  # 注意，这里有两个小括号，并且返回浮点型数据，而不是整形
print(zeros)

# # 创建1矩阵
ones = np.ones([3, 3])  # 注意这里也是两个括号，其中里面的小括号也可是中括号，但是不建议使用
print(ones)
#
# # 创建元素相同（）的矩阵
full = np.full((2, 3), 4)  # 其中第一个括号表示矩阵大小，后面的数字表示填充的数字
print(full)
#
# # 创建对角数为1的矩阵
diag = np.eye(3, 3)  # 注意这里如果行列数不同，只会让行列下标相等的元素为1
print(diag)
#
# # 创建随机矩阵(值在0到1之间)，注意这个方式不可以重复，也就是随机不可以全部重现，每次运行都会不一样
random = np.random.random((2, 3))
print(random)
# 写到这里，我需要说明一点，就是如何确定括号的个数
# numpy下的方法肯定是有一个小括号的，且不可以改变
# 想要表达多维阵列，则需要输入一个元组（小括号）或者列表（中括号）来创建，这时就需要小括号或者中括号
# 如果是自己手敲出多维阵列，每一行需要中括号表示，用逗号分离每一行，然后外层再用一个中括号表示整个矩阵，然后再作为一个举证输入函数中



# =======================矩阵的索引，切片=========================#

metaMatrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 用逗号，而不能用空格

# # 单个元素的索引
# a = metaMatrix[0][0]
# b = metaMatrix[0,0] # 这里不能使用小括号
# print(a)
# print(b)
#
# # 切片操作
# a_ = metaMatrix[0:2,1]# 注意这里冒号后面的数是不索引的，如果缺省就是到最后，冒号前是可以得到的
# # 冒号后的数不索引，这时python的特点，与MATLAB不一样
# print(a_)
#
# # 注意切片操作后矩阵维度的变化
# a1 = metaMatrix[0:1,:]
# a2 = metaMatrix[0,:]
# b = metaMatrix[0,1]
# print(a1)
# print(a2)
# print(b)
# # 注意到这两行代码得到的数据是一样的，但是维度已经发生了变化
# print(a1.shape) #a1仍然是矩阵
# print(a2.shape) #a2则是一个行向量，相比原矩阵，这里就少了一个维度，这与MATLAB有点不同
# print(b.shape) #b是没有维度的，就是一个数而已
#
# # 利用已有矩阵创建新矩阵，方法比较多样化
# SrcMatrix = np.array([[1,2], [3, 4], [5, 6]])
# print(SrcMatrix)
# # 利用矩阵的方式索引原有矩阵
# matrix1 = SrcMatrix[[0,1],[1,1]]# 这时将两个中括号的对应元素组合起来进行索引，是单个元素索引的扩展
# # 进行单个元素索引，然后组合起来，并用np.array创建成np的数组
# matrix2 = np.array([SrcMatrix[0][1],SrcMatrix[1][1]])
# # 如果不用np.array来创建成np的矩阵，就会导致数据格式的变化,对应的操作就会发生变化
# matrix3 = [SrcMatrix[0][1],SrcMatrix[1][1]]
# print(matrix1)
# print(matrix2)
# print(matrix3)
# print(type(matrix1))
# print(type(matrix2))
# print(type(matrix3))
#
# # numpy矩阵的元素索引方式可以用于改变或者选择矩阵不同行的元素（不仅仅是同一列的数据）
# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# b = np.array([0,2,0,1])
# # 先介绍一下np.arrange（）函数，表示创建一个从起始值到结束值少1（前面提到过，python中经常不到这个值）的行向量，也可以设定步长
# c = a[np.arange(4),b] #其实就是相当于矩阵方式索引一个矩阵中的元素（这比MATLAB中更加自由一些）
# print(c)
# # 改变矩阵的指定元素
# a[np.arange(4),b] += 10
# print(a)
#
# # 布尔型阵列，可以用来索引一些满足特定条件的元素
# matrix = np.array([[1,2],[3,4],[5,6]])
# bool_id = matrix>2 # 也可以写成bool_id =(matrix>2),注意，写成中括号就是不同含义了
# print(bool_id)
# print(matrix[bool_id])
# # 可以将上面两行代码合成一行
# matrix_ = matrix[matrix>2]# 注意，这里得到的是一维向量
# print(matrix_)
#
# =========================numpy array的数据类型=======================================#
# # numpy的array的数据类型是自动识别的，但也可以指定
# # 如果输入为整形，则会给数据的类型定义为int64
# matrix1 = np.array([1,2,3])
# print(matrix1.dtype)
# # 如果输入的数据为小数点，则会给数据类型定义为float64
# matrix2 = np.array([1.0,2.0,3.0])
# print(matrix2.dtype)
# # 如果有浮点型也有整形数据，会赋值给占字节数多的数据类型,且对应为64的
# matrix3 = np.array([1,2.0])
# print(matrix3.dtype)
# # 也可以指定数据类型
# matrix4 = np.array([1,2],dtype=np.int8)
# print(matrix4.dtype)
# # 当数据本身和指定的数据类型不符合时,会将数据转化成指定的数据类型，有可能会发生溢出
# matrix5 = np.array([1,2000000,3.1],dtype=np.int8)
# print(matrix5)
# print(matrix5.dtype)


#=========================矩阵的运算===================================#
#
# # 两种加法和减法，乘除
# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])
# sum1 = x + y# 直接使用加法
# sum2 = np.add(x,y)# 运用numpy的函数
# print(sum1)
# print(sum2)
#
# substract1 = x - y
# substract2 = np.subtract(x,y)
# print(substract1)
# print(substract2)
#
# prodution1 = x * y# 这是对应元素的乘法
# prodution2 = np.multiply(x,y)
# print(prodution1)
# print(prodution2)
#
# devide1 = x/y
# devide2 = np.divide(x,y)
# # 注意矩阵进行运算时，数据类型不改变，因此，需要注意溢出现象等
# print(devide1)
# print(devide2)
#
# # 矩阵的两种向量乘法（使用dot）
# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])
# multiDot1 = x.dot(y)
# multiDot2 = np.dot(x,y)
# print(multiDot1)
# print(multiDot2)
#
# # 矩阵运算基本函数
# x = np.array([[1,2],[3,4]])
# # 求和函数
# # 对所有元素求和
# sum_all = np.sum(x)
# # 对列求和
# sum_column = np.sum(x, 0)# 注意和MATLAB中的区分一下。
# # 对行求和
# sum_row = np.sum(x, 1)
# print(sum_all)
# print(sum_column)
# print(sum_row)
#
# # 矩阵的转置
# x = np.array([[1,2],[3,4]])
# transform = x.T
# print(transform)
#
# # broadcasting的应用，可以进行不同维度的矩阵算数运算
# # 考虑将一个常量行向量加到一个矩阵的每一行上
# # 下面会将x行向量加到y矩阵的每一行上(但是这个方法由于有显示循环，而显示循环比较慢一些，我们经常会采用其他方法)
# y = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# x = np.array([1, 0, 1])
# y_ = np.empty_like(y) # 创建一个和y相同维度的矩阵，但没有放内容，但是已经开辟了一块内存，其中的数据可能随机
# print(y_)
# for i in range(4):
#     y_[i,:] = y[i,:] + x
# print(y_)
# # 另一种方法是我们先将x复制3份，垂直放置，组成一个矩阵，再进行矩阵加法
# x_ = np.tile(x,(4,1))# np.tile表示复制,(4,1)表示将x作为元素，组成4*1的矩阵形式
# y__ = np.add(y,x_)
# print(y__)
# # 实际上，如果不对x进行处理，而直接将两者相加，如果x和y满足一些条件，x会自动复制
# # 条件是x和y在一个维度上相等，另一个维度上不一样并且可以通过复制可以实现维度相等，则会自动复制
# print(y+x)
# # 这里进行一个其他的测试
# print(x.T+y.T)# 可以看出可以实现列的复制
# 这里进行都不为向量的相加
# a1 = np.array([[1,2],[3,4],[5,6],[7,8]])
# a2 = np.array([[1,0],[0,1]])
# print(a1+a2)# 这里会出错，说明只能自动进行一维数据的复制，多维数据不支持自动复制，而需要显式复制
# # 同样的，加法，减法和除法也都适合上面的自动复制原理
 
# 将一个矩阵或者向量进行维度的调整
x1 = np.array([1,2,3])
y1 = np.array([1,2])
# 实现x1和y1转置的矩阵乘法，可以先将y1变成列向量
print(np.multiply(x1, np.reshape(y1,(2,1))))
# 试一下其他的维度变化
x2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.reshape(x2, (2,4)))
print(np.reshape(x2, (4,2)))# 基本上按照西安航后列的顺序进行
