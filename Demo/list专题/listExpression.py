list01 = range(1, 51)
print(list01)
print(len(list01))

result = []
iterableList = []
# 每个元素平方+1
# 列表，不能运算

for i in list01:
    resultNum = i ** 2 + 1
    result.append(resultNum)
print(result)

# 列表推导式（表达式）
# [exession for i in iterable if condition]
# iterableList.append([i ** 2 + 1 for i in list01 if i%2 != 0])
# 仅对奇数求平方+1
iterableList02 = [i ** 2 + 1 for i in list01 if i%2 != 0]
print(iterableList02)
print(len(iterableList02))
