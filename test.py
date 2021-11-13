#Hey

test = 1
test2 = 2

import pandas as pd


df = pd.read_csv('/Users/eduardomaia/Downloads/Data/Anagrafica_ClubQ8.csv',sep=;)
df.shape

df.head

#Identifying Data types
df.dtypes
def summarize_na(df: pd.DataFrame) -> pd.DataFrame:
    nan_count = df.isna().sum()
    return pd.DataFrame({'nan_count': nan_count,
                         'nan_pct': nan_count / len(df) * 100
                         }
                        )[nan_count > 0]
df_nan_sum = summarize_na(df)
df_nan_sum

df.set_index('COD_PAN_DA_POS', inplace= True )
df.index

#Transform the variable sex into a dummy variable
df_dc = pd.get_dummies(df, columns=['sex'])

#Divide the data set into Categorical and Numerical Variables
cols_focus_cat = [
    'REGIONE'
    'PROVINCIA',
    'COMUNE',
    'TIPO_CARTA',
]

cols_focus_num = [
    'SEX',
    'DATA_NASCITA',
    'DATA_BATTESIMO',
    'SALDO PUNTI',
]

cols_focus = cols_focus_cat + cols_focus_num

df[cols_focus_num].describe().transpose()

#Compare Sex Distribution
tmp = df['SEX'].value_counts()
cmap = cm.get_cmap('viridis')
ax = tmp.plot(kind='bar',
              title='gENDER dISTRIBUTION',
              color=[cmap(.25), cmap(.9)],
              )
ax.set(xlabel='SEX')
plt.show()

#Age Among Clients
tmp = -df['DAYS_BIRTH'] / 365
cmap = cm.get_cmap('viridis')
ax = tmp.plot(kind='hist',
              title='Distribution of age ',
              bins=10,
              density=False,
              rwidth=.9,
              color=cmap(.25),
              )
ax.set(xlabel='Age (in years)')
plt.show()






