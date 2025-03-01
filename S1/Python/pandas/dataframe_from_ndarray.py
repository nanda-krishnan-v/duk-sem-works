import pandas as pd
import numpy as np

array = np.array([[1,1,1],
                 [2,4,8],
                 [3,9,27],
                 [4,16,64]])

index_values = ['first','second','third','fourth']
column_values = ['number','square','cube']

df = pd.DataFrame(array,index=index_values,columns=column_values)
print(df)