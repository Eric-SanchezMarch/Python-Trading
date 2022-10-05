# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:41:24 2021

@author: emakt
"""

import pandas_datareader.data as web
import datetime as dt
import mplfinance as mpf


start = dt.datetime(2020,12,8)
end = dt.datetime(2021,1,8)

df = web.DataReader('MSFT','yahoo',start,end) #Microsoft

mpf.plot(df,type='candle',style='charles',title='Microsoft daily',ylabel='Price ($)')

#
#-------------------|---------------- 218        Si la vela es verda:
#                   |                               
#                   |                               OPEN  = 214
#                 XXXXX                             HIGH  = 218
#-----------------XXXXX-------------- 216           LOW   = 210
#                 XXXXX                             CLOSE = 216.5
#                 XXXXX
#                 XXXXX
#-----------------XXXXX-------------- 214       Si la vela fos roja:
#                   |                               
#                   |                               OPEN  = 216.5
#                   |                               HIGH  = 218
#-------------------|---------------- 212           LOW   = 210
#                   |                               CLOSE = 214
#                   |
#                   |
#-------------------|---------------- 210
#
#
#

