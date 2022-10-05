# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:12:28 2021

@author: emakt
"""

import pandas_datareader.data as web 
import datetime as dt
from numpy import where # 1 condicio, valor de la posicio columna cuan la con es cumplixe, el valor que pendra cuan no es cumplixe la condicio

start = dt.datetime(2015,1,1)   #Preus diaris!
end = dt.datetime(2021,1,1)

# .DataReader()
df = web.DataReader('KO','yahoo',start,end)

# Medias mobiles
# rolling - encara que vulguem una mitja el que volem es que ens faigue una 
#           mitja al llrg de les mostres, x exemple la movil curta sera 42
#           dies
#           A cada mostra ens mostrara la mitja de les anteriors 42 mostrers
#
# min_periods ens fa el calcul movil desde la primera mostra
# i la movil llarga la definim igual pero en mes dies.

df['42ma'] = df['Close'].rolling(window=42,min_periods=0).mean()
df['84ma'] = df['Close'].rolling(window=84,min_periods=0).mean()
# ma media movil = https://es.wikipedia.org/wiki/Media_m%C3%B3vil
# 42 dies equivalen a 2 mesos de borsa sense contar festius.

# 
# nem a crear una columna per identificar cuan la media movil curta esta
# per damun de la llarga, per lo que almacenara el valor entre la media movil
# curta i la media movil llarga
# 
# la crearem 
# 
# ESTRATEGIA
# VOLEM QUE CUAN LA MEDIA MOVIL CURTA ESTIGUE PER DAMUN LA LLARGA, VOLEM COMUNICAR UNA COMPRA 1
# AL CONTRARI, CUAN LA LLARGA ESTIGUE PER DAMUN VOLEM COMUNICAR UNA VENTA -1
# 
# CUAN TINGUEN EL PRIMER VALOR JAVORS NO OPERAREM 0
# 
# 


df['diferencia'] = df['42ma'] - df['84ma']
df['Regime'] = where(df["diferencia"]>0,1,0)
df["Regime"] = where(df['diferencia']<0,-1,df["Regime"])


# 
# dIBUIXAREM UNA GRAFICA EL PREU DE TANCAMENT DE APPLE JUNTAMENT AMB LES 2 MEDIES MOVILS
# EL PROPI PANDA JA TE UNA FUNCIO
# 

df[['Close','42ma','84ma']].plot(grid=True)




































