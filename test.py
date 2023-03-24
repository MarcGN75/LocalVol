import pandas as pd
import numpy as np

def conv(x, y):
    if y >= 15:
        return (33.8*np.sin(1.65*(x-0.89))+33.9)/0.19
    else:
        return x


dico = {'A': [1, 2, 3],
        'B': [10, 20, 30]}
df = pd.DataFrame(data=dico)
print(df)
df['C'] = [0, 0, 0]
print(df)
df['C']=df.apply(lambda x: conv(x['A'], x['B']), axis=1)

print(df)
