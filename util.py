# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:41:18 2016

@author: Ray
"""

import os
import pandas as pd

def famaFrench3Path(period, base_dir="D:/SpyderWorkspace/famaFrench3"):
    filename = "ff3data_" + period
    return os.path.join(base_dir, filename + ".csv")

def symbol2Path(symbol, base_dir="D:/SpyderWorkspace/famaFrench3/Data/"): #Returns path of csv given an asset symbol
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
    
def calcAssetReturns(df):
    #replace prices with returns
    x_returns = df.copy()
    x_returns[1:] = (df[1:]-df[:-1].values)/df[1:]*100
    #print(x_returns)
    x_returns.ix[0,:] = 0
    return x_returns
    
    
    
#def getAdjClose(symbols, dates): #Reads adjusted close prices for symbols in given list
#    df = pd.DataFrame(index=dates)
#    #Checks for SPY Benchmark
#    if 'SPY' not in symbols:
#        symbols.insert(0,'SPY')
#    #Adds Adj. Close prices to df
#    for  symbol in symbols:
#        dftmp = pd.read_csv(symbol2Path(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj.Close'], na_values=['nan'])
#        dftmp = dftmp.rename(columns={'Adj. Close' : symbol})
#        #Drop if SPY did not trade
#        if symbol == 'SPY':
#            df = df.dropna(subset=['SPY'])
#    
#    return df

           
def constructDataFrames(period, dates, symbols):
    df_final = pd.DataFrame(index=dates)
    df_FF = pd.read_csv(famaFrench3Path(period), index_col="Date", parse_dates=["Date"], na_values=['nan'])
#   print(df_FF)
    df_FF = df_FF.ix[dates]
#   print(df_final)
#   print(df_FF)
    df_final = df_final.join(df_FF)
#   print(df_final)
    
    for symbol in symbols:
        df_A = pd.read_csv(symbol2Path(symbol), index_col="Date", parse_dates=["Date"], usecols=["Date", "Close"], na_values=['nan'])
        df_A = df_A.rename(columns={'Close' : symbol})
        df_A = df_A.ix[dates]
        df_A = calcAssetReturns(df_A)
        df_final = df_final.join(df_A)
        df_final = df_final[1:]
        df_final.index.name = "Date"
    return df_final
    
    