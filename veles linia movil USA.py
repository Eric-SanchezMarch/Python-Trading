from pandas_datareader.data import DataReader
from datetime import datetime
import mplfinance as mpf

start = datetime(2019,10,8)
end = datetime(2021,1,8)

df = DataReader('USA','yahoo',start,end)
df['ma'] = df['Close'].rolling(window=10,min_periods=0).mean()


mc = mpf.make_marketcolors(up='tab:green',down='tab:red',wick={'up':'green','down':'red'})

s = mpf.make_mpf_style(base_mpl_style='seaborn', mavcolors=['orange'],marketcolors=mc)
mpf.plot(df,type='candle',style=s,mav=5,title='USA')

# LA LINIA NARANJA REPRESENTA LA LINIA MOVIL DELS 5 ULTIMS DIES  // mav=5