import yfinance as yf
import numpy as np

import plotly.express as px



Stock_symbols = ['JILL','ELTK','ONVO','UAVS', 'AEY','OBLN']


def market_return(List, Start, End):
    """  Market Return for each stock"""    

    j = 0
    T = 44
    N = len(List)
    PORTFOLIO = np.zeros((T, N))

    for i in List:
        #print("Stock: ",i)
        stock_symbol = yf.Ticker(i)
        data = stock_symbol.history(start=Start, end=End)
        Price = (data['Open'] + data['Close']) / 2
        
        Return = Price.div(Price.shift(1)).dropna()
        Return = np.log(Return)
        
        PORTFOLIO[:,j] = Return
        j+=1

        #time_series_plot(Return)

    return PORTFOLIO


def time_series_plot(data):
    
    fig = px.line(data)
    fig.show()

print(market_return(Stock_symbols, '2019-07-01', '2019-09-04'))
#2019-07-01 .........24517
#2019-09-03 ..........24561

