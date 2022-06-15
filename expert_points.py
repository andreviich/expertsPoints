import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('data_1.csv', delimiter=';')
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
print(df)
#средний балл
sr = df.mean()
print("матожидание","\n",sr)
#дисперсия
var = df.var()
print("дисперсия","\n",var)
#стандартное отклонение
stand = df.std()
print("стандартное отклонение","\n",stand)
corl=np.sqrt(var)
print(corl)
l_gran_dov=sr-corl
r_gran_dov=sr+corl
df2=df2.assign(Левая_граница_доверительного_инервала= l_gran_dov)
df3=df3.assign(Правая_граница_доверительного_инервала= r_gran_dov)
df1 = df1.append(sr, ignore_index=True)
df1 = df1.append(var, ignore_index=True)
df1 = df1.append(stand, ignore_index=True)
df.hist()
plt.show()
print(df1)
print(df2)
print(df3)
