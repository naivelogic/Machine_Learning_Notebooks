import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style        # make graphs look good
import pandas as pd      # data analysis library
import quandl

style.use('ggplot')

#start = dt.datetime(2018,1,1)
#end = dt.datetime.today()

#df = quandl.get('WIKI/TSLA', start_date="2015-01-01", end_date="2018-08-03")

# convert to csv
#df.to_csv('tsla.csv')

# read the csv
df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0)

#print(df.head())
print("Overall TSLA Open and High Prices \n" ,df[['Open', 'High']].head())

## Visualization - Print plot
#df['Adj. Close'].plot()
#plt.show()

## Manipulations
df['100ma'] = df['Adj. Close'].rolling(window=100, min_periods=0).mean()


# Open High Low Close 
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

df_ohlc = df['Adj. Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum() #average valume over 10 days

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #convert dates to numbeers

print("\n Open High Low Close Dataset: \n", df_ohlc.head())

# map ohlc

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
