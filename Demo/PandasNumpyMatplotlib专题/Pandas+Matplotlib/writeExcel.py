import pandas as pd

dataFrame01 = pd.DataFrame({
    'id':[1,2,3],
    'name':['张三', '李四', '王五'],
    'age':[30,28,30]
})

print(dataFrame01)
# 更改，替换自动索引
dataFrame01 = dataFrame01.set_index('id')
print(dataFrame01)
dataFrame01.to_excel('people.xlsx')
# 该文件位置提前创建excel文件夹
dataFrame01.to_excel('./excel/people.xlsx')
print('Done.')