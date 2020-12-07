import pandas as pd

students = pd.read_excel('Students.xlsx')
print(students)
# inplace就地返回students，ascending默认从小到大
students.sort_values(by='Score',ascending=False,inplace=True)
print(students)