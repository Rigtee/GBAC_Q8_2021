import pandas as pd

db1 = pd.read_csv('master_data/Anagrafica_ClubQ8.csv', sep=';')
db2 = pd.read_csv('master_data/Premi_ClubQ8.csv', sep=';')
db3 = pd.read_csv('master_data/Rifornimenti_Carburante_ClubQ8.csv', sep=';')

db1_head = db1.head(1000)
db2_head = db2.head(1000)
db3_head = db3.head(1000)

db1_head.to_csv('copy_master_data/Anagrafica_ClubQ8_red.csv', sep = ';')
db2_head.to_csv('copy_master_data/Premi_ClubQ8_red.csv', sep = ';')
db3_head.to_csv('copy_master_data/Rifornimenti_Carburante_ClubQ8_red.csv', sep = ';')

#Test using PyCharm