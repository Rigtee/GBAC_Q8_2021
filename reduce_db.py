import pandas as pd

db1 = pd.read_csv('master_data/Anagrafica_ClubQ8.csv', sep=';')

db1_head = db1.head(1000)

db1_head.to_csv('copy_master_data/Anagrafica_red.csv')

