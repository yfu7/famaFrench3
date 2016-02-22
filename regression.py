# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:58:20 2016

@author: Ray
"""
import pandas as pd
from pandas.stats.api import ols
from util import constructDataFrames

def excessReturns(df,symbols):
    for symbol in symbols:
        df["xR"] = df[symbol] - df["RF"]
    return df
    
def linReg(df):
    print(df)
    factors = list(df.columns.values)[0:3]
    regression = ols(y=df['xR'], x=df[factors])
    print(regression)
    

def test():
    dates = pd.date_range('2005/12/01', '2010/12/01', freq='MS')
    symbols = ['FMAGX']
    period = "monthly"
    df_final = constructDataFrames(period, dates, symbols)
    excessReturns(df_final, symbols)
    linReg(df_final)
if __name__ == "__main__":
    test()