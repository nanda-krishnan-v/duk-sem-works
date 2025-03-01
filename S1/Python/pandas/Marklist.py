import pandas as pd

data = {'Roll No':[1,2,3,4,5],'Name':['NKV','Sreedxv','zAnanth','Dilshad','Kartha'],
        'Subject':['Maths','Python','OS','DSA','Maths'],
        'Assignment':[29,28,26,27,30],
        'Project':[99,98,96,97,99]
        }

df = pd.DataFrame(data)
print(df)