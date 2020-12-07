x_left = [[1.0, 2], [3, 4.0], [5.0, 6]]

aMove = 1.00
bMove = -2.00
xMove = []
i = 0

# 取值计算
for i in x_left:
  # xMove = aMove * x_left[0][0] + bMove
  # xMove = aMove * x_left[i][0] + bMove
  xMove.append(aMove * i[0] + bMove)
print(xMove)

for i in x_left:
  print(x_left)

print(x_left[1][1])

x_left.append([8, 10])
print(x_left)
x_left[0][0] = 15
print(x_left)

# Matrix赋值
for i in range(len(x_left)):
    x_left[i][0] = 1
    x_left[i][1] = 1
print(x_left)
