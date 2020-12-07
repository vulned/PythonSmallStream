import numpy as np
a = 3
b = 5

x_list  = [[9.96, 2968.08], [9.17, 2388.64], [7.78, 1515.02]]
for x in x_list:
    print('记住x在for in循环中的数据类型，是会变的：' + str(type(x)))
    y01 = a * x[0] + b
    print(y01)

    y02 = a * x[1] + b
    print(round(y02, 2))


for i in range(0, len(x_list)):
    x_list[i][0] += 1
print(x_list)

x_list_Np = np.array(x_list)
for i in range(0, len(x_list_Np)):
    x_list_Np[i][0] += 1
print(x_list_Np)
