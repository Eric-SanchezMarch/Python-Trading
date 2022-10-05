# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 01:00:31 2021

@author: emakt
"""


# 
# Trend following
# Deteccio de tendencia
# 
# 
# 
# 
# Cuan i aigue una vela cuyo hig sigue el major en los ultims 10 dies
# es una senyal de compra
# Cuan i aigue una vela cuyo low sigue el menor en los ultims 10 dies
# es una senyal de venta
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 



import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime
start = datetime(2000,10,1)
end = datetime (2020,10,1)
df = DataReader('INTC','yahoo',start,end)


window = 10
df['highest high'] = df['High'].rolling(window=window).max()
df['lowest low'] = df['Low'].rolling(window=window).max()

#Regles estrategia
df['Trigger'] = np.where(df['High']==df['highest high'],1,np.nan)
df['Trigger'] = np.where(df['Low']==df['lowest low'],-1,df['Trigger'])
df['Position'] = df['Trigger'].ffill().fillna(0)

df['Returns'] = df['Adj Close']/df['Adj Close'].shift(1)
df['Strategy'] = df['Returns'] ** df['Position'].shift(1)

plt.style.use('seaborn')
df[['Returns','Strategy']].dropna().cumprod().plot(figsize=(15, 6))