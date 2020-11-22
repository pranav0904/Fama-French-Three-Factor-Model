import yfinance as yf
import numpy as np


Stock_symbols = ['JILL','ELTK','ONVO','UAVS', 'AEY','OBLN','XRF','MLSS','MICT','SOLY','NMRD','INUV','VTGN',
                'MTSL','DXR','QADA','MYOV','BOSC','APTO','PESI','TITN','EYEG','CAPR','UROV','APDN','TTPH','ECOR','WYND','ZN',
                'OSN','HDSN','BDR','TBLT','PLM','DMRC','MOV','PVH','TLYS','CPAH','SDRL','RWLK','VEEV','OPRX','RAVE',
                'PFSW','SPWH','TMDX','DOOO','TC','NBY','WSTL','KEYS','DBI','RVLT','JASN','CNET','RVLV','REKR','SUMR',
                'MBOT','BDGE','FOLD','SRRA','IDN', 'PIXY','LYL','MHLD','NIO','SLS','NNVC', 'MYT','BYND','CREG',
                'TCCO','AAMC','OXBR','ANCN','BCRX','ALRN','RTW','LTBR','WWR','VTVT','MACK','NDRA','OTLK','MYT','BYND',
                'CREG','TCCO','AAMC','OXBR','ANCN','BCRX','ALRN','RTW','LTBR','WWR','HTHT','MACK']


def portfolio_return(List, Start, End):
    """  Portfolio Return for each stock"""    

    j = 0
    T = 44
    N = len(List)
    PORTFOLIO = np.zeros((T, N))

    for i in List:
        print("Stock: ",i)
        stock_symbol = yf.Ticker(i)
        data = stock_symbol.history(start=Start, end=End)
        Price = (data['Open'] + data['Close']) / 2
        
        Return = Price.div(Price.shift(1)).dropna()
        Return = np.log(Return)
        
        PORTFOLIO[:,j] = Return
        j+=1

    return PORTFOLIO


#print(portfolio_return(Stock_symbols, '2019-06-28', '2019-08-31'))
