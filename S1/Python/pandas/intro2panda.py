import pandas as pd

# creating a sample dataframe with the elements and printing the value
df = [['Alex',10], [ 'James',20]]
data = pd.DataFrame(df,columns=['name','age'])

print(data)