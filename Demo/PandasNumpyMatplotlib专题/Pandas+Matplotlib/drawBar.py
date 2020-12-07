import pandas as pd, matplotlib.pyplot as plt

students = pd.read_excel('Students.xlsx')
# print(students)
# inplace就地返回students，ascending默认从小到大
students.sort_values(by='Score', ascending=False, inplace=True)
# print(students)

# 前两个参数使用了两种不同写法，均可
plt.bar(students['Name'], students.Score, color='green')
plt.title('Students Score', fontsize = 24)
plt.xlabel('Name')
plt.ylabel("Score")

plt.xticks(students.Name, rotation = '90')
# 紧凑型布局
plt.tight_layout()
# plt.show()
imgname = 'data.jpg'
plt.savefig(imgname)
# 想显示中文需要做其他操作