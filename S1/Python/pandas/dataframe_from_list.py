import pandas as pd

data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data,index = ['row1','row2','row3'],columns =['c1','c2','c3'])

print(df)

data2 = [['Alex',10], [ 'James',20]]
df1 = pd.DataFrame(data2,columns=['name','age'])
print(df1)