# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 00:07:22 2021

@author: emakt
"""

# Regim tendencial
#    trend foyowing -> es basa en posicionarse a fabor de la direccio creixent del preu
# Regim cicle
#   revision a la media -> el preu aura de tornar a un preu intermedi
#
# En cuan el preu s'ancamine en una direccio lo que farem sera posicionarnos
# en fabor de la direccio oposada
#
# Normalment s'analitza quina de les 2 estrategies funciona millor 
# per  un instrument financer particular
#
#
# Farem una estrategia de regresio a la mitja del instrument.
# Cuan el preu es situe per damun de la mitja o pendrem com una venta 
# Una senyal de compra sera el contrari

# de cuants dies volem fer la mitja i de cuanta distancia?

import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime
start = datetime(2020,1,1)
end = datetime (2021,1,1)
data = DataReader('MSFT','yahoo',start,end)
data['Price'] = data['Adj Close']

SMA = 25  #Media movil
data['SMA'] = data['Price'].rolling(window=SMA).mean()

N =2
data['STD'] = N*data['Price'].rolling(window=SMA).std()
data['SMA+STD'] = data['SMA'] + data['STD']
data['SMA-STD'] = data['SMA'] - data['STD']

plt.style.use('seaborn')
data[['Price','SMA+STD','SMA-STD']].plot(figsize=(10,6))
data['Position'] = np.where(data['Price'] > data['SMA+STD'], -1,0 )
data['Position'] = np.where(data['Price'] < data['SMA-STD'], 1,data['Position'])
data['Position'] = data['Position'].fillna(0)

data['Returns'] = data['Price']/data['Price'].shift(1)
data['Strategy'] = data ['Returns'] ** data['Position'].shift(1)
data[['Returns','Strategy']].dropna().cumprod().plot(figsize=(10,6))