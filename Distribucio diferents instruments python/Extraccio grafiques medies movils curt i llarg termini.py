# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:12:28 2021

@author: emakt
"""
#Este programa esta vectoritzat
import pandas_datareader.data as web 
import datetime as dt
from numpy import where # 1 condicio, valor de la posicio columna cuan la con es cumplixe, el valor que pendra cuan no es cumplixe la condicio

start = dt.datetime(2020,1,1)   #Preus diaris!
end = dt.datetime(2021,1,1)

# .DataReader()
df = web.DataReader('AAPL','yahoo',start,end)

# Medias mobiles
# rolling - encara que vulguem una mitja el que volem es que ens faigue una 
#           mitja al llrg de les mostres, x exemple la movil curta sera 42
#           dies
#           A cada mostra ens mostrara la mitja de les anteriors 42 mostrers
#
# min_periods ens fa el calcul movil desde la primera mostra
# i la movil llarga la definim igual pero en mes dies.

# ma 


# Declaracio COLUMNES medies movils
df['1ma'] = df['Close'].rolling(window=1,min_periods=0).mean()
df['2ma'] = df['Close'].rolling(window=2,min_periods=0).mean()
df['3ma'] = df['Close'].rolling(window=3,min_periods=0).mean()
df['5ma'] = df['Close'].rolling(window=5,min_periods=0).mean()
df['7ma'] = df['Close'].rolling(window=7,min_periods=0).mean()
df['42ma'] = df['Close'].rolling(window=42,min_periods=0).mean()
df['84ma'] = df['Close'].rolling(window=84,min_periods=0).mean()
df['126ma'] = df['Close'].rolling(window=126,min_periods=0).mean()
df['168ma'] = df['Close'].rolling(window=168,min_periods=0).mean()
df['252ma'] = df['Close'].rolling(window=252,min_periods=0).mean()
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


df['diferencia'] = df['42ma'] - df['252ma']
df['Regime'] = where(df["diferencia"]>0,1,0)
df["Regime"] = where(df['diferencia']<0,-1,df["Regime"])

df['diferencia2'] = df['42ma'] - df['126ma']
df['Regime2'] = where(df["diferencia2"]>0,1,0)
df["Regime2"] = where(df['diferencia2']<0,-1,df["Regime2"])

df['diferencia3'] = df['42ma'] - df['168ma']
df['Regime3'] = where(df["diferencia3"]>0,1,0)
df["Regime3"] = where(df['diferencia3']<0,-1,df["Regime3"])

df['diferencia4'] = df['42ma'] - df['252ma']
df['Regime4'] = where(df["diferencia4"]>0,1,0)
df["Regime4"] = where(df['diferencia4']<0,-1,df["Regime4"])
# 




# dIBUIXAREM UNA GRAFICA EL PREU DE TANCAMENT DE APPLE JUNTAMENT AMB LES 2 MEDIES MOVILS
# EL PROPI PANDA JA TE UNA FUNCIO
# 




# Generacio de grafica amb plot amb les medies movils:
        
#df[['Close','42ma','252ma']].plot(grid=True)    
df[['Close','1ma','2ma','3ma','5ma','42ma','42ma','84ma','126ma','168ma','252ma']].plot(grid=True)





# Si la media curta es situa per damun la llarga comprem accions
# si es situ al rebes vendrem accions de apple
# 
# iniciem un capital X que suposara el 100%
# incrementarem o decrementarem la nostra estrategia
#
# Increment relatiu = preu dia actual / preu dia anterior

 # columna market ens marca el preu relatiu de cada dia amb el preu del dia anterior
df['Market'] = df['Close']/df['Close'].shift(1)
 # columna estrategy ens marca el valor que incrementa cada dia es la variacio 
 # de preu tenin en compte la posicio
df['Strategy']=df['Market']**df['Regime'].shift(1)
# El shift definix la posicio al mercat al di anterior
df[['Market','Strategy']].cumprod().plot(grid=True) 
































