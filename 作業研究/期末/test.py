import pandas as pd
import numpy as np
db = pd.read_excel(r'早餐們.xlsx',sheetname=0)
dnb=pd.read_excel(r'晚餐們.xlsx',sheetname=0)
CB=np.zeros((20,1))
CNB=np.zeros((57,1))
HB=np.zeros((20,1))
HNB=np.zeros((57,1))
dataB=np.array(db)
dataNB=np.array(dnb)
for j in range(len(CB[:,0])):
		for w in range(len(CB[0])):
			CB[j][w]=dataB[j][2]
			HB[j][w]=dataB[j][3]
for j in range(len(CNB[:,0])):
		for w in range(len(CNB[0])):
			CNB[j][w]=dataNB[j][2]
			HNB[j][w]=dataNB[j][3]
print(dataB)
print(dataNB)