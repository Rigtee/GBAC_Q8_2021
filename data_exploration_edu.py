#Most of PREMI_Q8 data set is composed by categorical data so covariance and things like that are not insightful in this section
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('master_data/Premi_ClubQ8.csv', sep=;)
df_head = df.head(1000)
df_nan_sum = summarize_na(df) df_nan_sum # to check how many cels have no data in it
df = df.set_index(COD_PAN_DA_POS) # set directly the ID code as the index of the dataframe
# see the caategorical variables and the absolute variables
cols_focus_cat = [
    'LUOGO_PRENOTAZIONE_PREMIO',
    'CATEGORIA',
    'RAGGRUPPAMENTO_MERCEOLOGICO',
    'DESCRIZIONE',
]
cols_focus_num = [
    'PUNTI_RICHIESTI',
    'CONTRIBUTO_CLIENTE_CON_IVA',
]
cols_focus = cols_focus_cat + cols_focus_num
df[cols_focus_num].describe().transpose()
df[cols_focus_cat].astype(str).describe().transpose()
get_frequencies(df['CATEGORIA'], n_categories=2)
get_frequencies(df['LUOGO_PRENOTAZIONE_PREMIO'], n_categories=2)
get_frequencies(df['RAGGRUPPAMENTO_MERCEOLOGICO'], n_categories=7) # in this one, I don't know how many prices there are, but this might be extremely useful
get_frequencies(df['DESCRIZIONE'], n_categories=10) # in this one, I don't know how many prices there are, but this might be extremely useful
df['CATEGORIA'].value_counts()
df['LUOGO_PRENOTAZIONE_PREMIO'].value_counts()
df['RAGGRUPPAMENTO_MERCEOLOGICO'].value_counts()
df['DESCRIZIONE'].value_counts()

tmp = get_frequencies(df['CATEGORIA'], n_categories=2)['relative']
           cmap = cm.get_cmap('viridis')
           ax = tmp.plot(kind='pie',
title="More fuel or Rewards?", autopct='{:02.2f}%'.format,
legend=True,
labeldistance=None,
startangle=170,
colors=[cmap(i) for i in np.linspace(.25, .9, len(tmp
 ))],
ax.set(ylabel='NAME_FAMILY_STATUS')
plt.show()


tmp = get_frequencies(df['LUOGO_PRENOTAZIONE_PREMIO'], n_categories=2)['relative']
           cmap = cm.get_cmap('viridis')
           ax = tmp.plot(kind='pie',
title="Where the clients claim the rewards?", autopct='{:02.2f}%'.format,
legend=True,
labeldistance=None,
startangle=170,
colors=[cmap(i) for i in np.linspace(.25, .9, len(tmp
 ))],
ax.set(ylabel='NAME_FAMILY_STATUS')
plt.show()

tmp = get_frequencies(df['RAGGRUPPAMENTO_MERCEOLOGICO'], n_categories=10)['relative']
           cmap = cm.get_cmap('viridis')
           ax = tmp.plot(kind='pie',
title="More fuel or Rewards?", autopct='{:02.2f}%'.format,
legend=True,
labeldistance=None,
startangle=170,
colors=[cmap(i) for i in np.linspace(.25, .9, len(tmp
 ))],
ax.set(ylabel='NAME_FAMILY_STATUS')
plt.show()

tmp = get_frequencies(df['DESCRIZIONE'], n_categories=2)['relative']
           cmap = cm.get_cmap('viridis')
           ax = tmp.plot(kind='pie',
title="The most beloved Rewards", autopct='{:02.2f}%'.format,
legend=True,
labeldistance=None,
startangle=170,
colors=[cmap(i) for i in np.linspace(.25, .9, len(tmp
 ))],
ax.set(ylabel='NAME_FAMILY_STATUS')
plt.show()
#Change the name of the columns to better understand the data
df['DESCRIZIONE'] = REWARD
df['RAGGRUPPAMENTO_MERCEOLOGICO'] = MATERIAL_GROUPING
df['LUOGO_PRENOTAZIONE_PREMIO'] = REQUEST_PLACE
df['COD_PAN_DA_POS'] = CUSTOMER_CODE
df['CATEGORIA'] = CATEGORY
df['DATA_OPERAZIONE'] = TRANSACTION_DATE
df['CONTRIBUTO_CLIENTE_CON_IVA'] = CUSTOMER_CONTRIBUTION
df['PUNTI_RICHIESTI'] = REMAINING_POINTS




