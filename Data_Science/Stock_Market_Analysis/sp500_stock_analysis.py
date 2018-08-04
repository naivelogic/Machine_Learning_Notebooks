import bs4 as bs
import pickle       # using pickle to serialize S&P500 list
import requests
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np
import datetime as dt 
import os       # create new directorys
import pandas as pd 
import quandl

style.use('ggplot')

"""
Use BeautifulSoup to web scrap Wikipedia for listing for S&P500 Companies
"""

def save_sp500_tickers():
    #resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    resp = requests.get('https://www.slickcharts.com/sp500')
    soup = bs.BeautifulSoup(resp.text, "lxml") #text of soruce code
    table = soup.find('table', {'class':'table table-hover'})
    
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[2].text   #get Ticker Symple
        tickers.append(ticker)

    with open("sp500tickers.pickle", 'wb') as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers()


"""
Get data from S&P500 companies for analsyis
"""

def get_data_from_zachs(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", 'rb') as f:
            tickers = pickle.load(f) 

    # take stock data in own stock directory 
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    for ticker in tickers[6:102]: # exclude BRK.B tickers[5]
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = quandl.get('WIKI/'+ ticker, start_date="2015-01-01", end_date="2018-08-03")
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

#get_data_from_zachs()

"""
Complie all S&P500 and combine in to one dataframe
"""

def compile_data():
    with open("sp500tickers.pickle", 'rb') as f:
        tickers = pickle.load(f)
        tickers = tickers[:5] + tickers[6:102]

    main_df = pd.DataFrame()

    # iterate through the tickers and files
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns = {'Adj. Close':ticker}, inplace=True)

        df.drop(['Open','High','Low','Close','Volume','Ex-Dividend',
                'Split Ratio', 'Adj. Open', 'Adj. High', 'Adj. Low',
                'Adj. Volume'], 1, inplace=True)

        # join dataframe together with the Adj. Close + Ticker Name

        if main_df.empty:
            main_df = df
        else: 
            main_df = main_df.join(df, how='outer') #keep rows together

        if count % 10 == 0:
            print(count)


    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

#compile_data()

"""
Correlate S&P 500 table for relationships
"""
def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr() #generate the coorelation values of all the data in the df

    print(df_corr.head())

    data = df_corr.values # get values of the df (np array)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn) #heat mpate
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1) # color limits -1 min; +1 max

    plt.tight_layout()
    plt.show()

visualize_data()