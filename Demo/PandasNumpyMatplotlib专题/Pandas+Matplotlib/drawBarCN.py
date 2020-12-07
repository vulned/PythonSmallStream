import pandas as pd, matplotlib.pyplot as plt

# students = pd.read_excel('Students.xlsx')
students = pd.read_excel('学生.xlsx')
# print(students)
# inplace就地返回students，ascending默认从小到大
students.sort_values(by='分数', ascending=False, inplace=True)
# print(students)

# 添加中文字体
from matplotlib.font_manager import FontProperties
# 控制面板字体属性
font = FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf', size = 24)

plt.bar(students['姓名'], students.分数, color='green')
plt.title('分数排名', fontproperties = font, fontsize = 24)
plt.xlabel('姓名', fontproperties = font)
plt.ylabel('分数', fontproperties = font)

plt.xticks(students.姓名, fontproperties = font, rotation = '90')
plt.tight_layout()
plt.show()