import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data_2.csv', delimiter=';')
dfsorted=df.sort_values(axis=1,by=[0])
dff = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
srednevzv=[]
mediana = dfsorted[["Витя"]]
disp2=dfsorted.var(axis=0)
dfsorted = dfsorted.append(disp2, ignore_index=True)
dfsorted.iloc[5] =dfsorted.iloc[5].apply(lambda x: 1/x)
summ5=dfsorted.iloc[5].sum()
dfsorted.iloc[5] =dfsorted.iloc[5].apply(lambda x: x/summ5)
df1 = df1.assign(Наименование = ["макдоналдс","кфс","Ролл-Х","крошка картошка","бургер кинг"])
df1 = df1.assign(Медиана = mediana)
for i in range(dfsorted.shape[0]-1):
    operator = dfsorted.iloc[5]
    period = operator.mul(dfsorted.iloc[i])
    itog=period.sum(axis=0)
    srednevzv.append(itog)

df2 = df2.assign(Коэф_компитентности_в_процентах= dfsorted.iloc[5])

dff = dff.assign(Наименование = ["макдоналдс","кфс","Ролл-Х","крошка картошка","бургер кинг"])
dff = dff.assign(средневзвешенные_ранги= srednevzv)
print(df)
print(df1,"\n")

print(df2,"\n")
print(dff,"\n")
df.T.plot.bar()
plt.legend(["макдоналдс","кфс","Ролл-Х","крошка картошка","бургер кинг"])
plt.show()
hist = df.hist(bins=3)
