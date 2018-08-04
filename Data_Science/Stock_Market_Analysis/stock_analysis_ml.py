from collections import Counter
import numpy as np 
import pandas as pd 
import pickle

# Machine Learning 
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

'''
Can we get a machine to identify the patterns in SP500 pricing data?

We will look at:
- features: take pricing data and convert into percentage change for all companies
- labels: buy, sell, hold

Training objective: within a selected 7 day period, did price go:
- up + 2% (buy) 
- down - 2% (sell)
- neither? (hold)
'''


def process_data_for_labels(ticker):
    '''
    Create future Values
    '''

    hm_days = 7 
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker] #value in % change 

    df.fillna(0, inplace=True)
    return tickers, df

# process_data_for_labels('MSFT')

def buy_sell_hold(*args):
    '''
    Create targets for labels... is this company a buy, sell or hold
    Set requirement at 2% threshold as a metrics to determine the labels when looking at the
    percent change of any company over the next 7 days
    '''

    cols = [c for c in args]  
    #requirement = 0.02 

    # [y_train data] target classification
    for col in cols:
        if col > 0.025:  #buy
            return 1
        if col < -0.025: #sell
            return -1
    
    return 0                    #hold



def extract_featuresets(ticker):
    '''
    create a function to map the buy_sell_hold function new col to the df
    '''
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                                df['{}_1d'.format(ticker)],
                                                df['{}_2d'.format(ticker)],
                                                df['{}_3d'.format(ticker)],
                                                df['{}_4d'.format(ticker)],
                                                df['{}_5d'.format(ticker)],
                                                df['{}_6d'.format(ticker)],
                                                df['{}_7d'.format(ticker)]
                                                ))

    # determine spread of tickerts for a given week 
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread: ', Counter(str_vals))

    #prior na = 0
    df.fillna(0, inplace=True)

    # replace infinate changes with nans
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    # [X_train data] create feature sets - Percent Change for all companies
    df_vals = df[[ticker for ticker in tickers]].pct_change()   # normalize ticker price (% change from yesterday)
    df_vals = df.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    # Feature Sets (X) & Labels (y)
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values       # [y_train] Target classification 

    return X, y, df


def do_ml(ticker):
    '''
    Machine Learning function
    sentdex: https://www.youtube.com/watch?v=W4kqEvGI4Lg&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=12
    '''

    X, y = extract_featuresets(ticker)
    
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25 ) #25% of sample data is test data
    
    # Create Classifier Voting Method 
    #clf = neighbors.KNeighborsClassifier() # define classifier #Simple classifier
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())
                            ])


    clf.fit(X_train, y_train) #use classifier that fits input data to the target classifier
    confidence = clf.score(X_test, y_test) 
    
    # Print Accuracy
    print('Accurace: ', confidence)

    # Pass a large amout of feature sets to return a list of predictions
    predictions = clf.predict(X_test)
    # View the predictions & evaluate
    print('Predicted Spread: ', Counter(predictions))

    return confidence

do_ml('MSFT')






