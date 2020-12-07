import pandas as pd

df = pd.DataFrame(
    {'id':[1,3,5],'name':['a','b','c'],'age':[15, 18, 26]}
)
print(df)

df = df.set_index('id')
print(df)

df.to_excel(r'C:\Users\Whaldom\Desktop\test.xlsx')
