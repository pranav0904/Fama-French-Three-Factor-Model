from EQ_01 import market_return

import numpy as np 
import pandas as pd 

FAMA_FRENCH_3 = pd.read_csv("Data/F-F_Research_Data_Factors_daily.csv",names=['Mkt-RF','SMB','HML','RF'], skiprows=24516, nrows=44)
#FAMA_FRENCH_3 = FAMA_FRENCH_3[]
#2019-07-01 .........24517
#2019-08-30 ..........24560


MKT = FAMA_FRENCH_3['Mkt-RF'] - FAMA_FRENCH_3['RF']
SMB = FAMA_FRENCH_3['SMB']
HML = FAMA_FRENCH_3['HML']

Stock_Symbols = ['JILL','ELTK','ONVO','UAVS', 'AEY','OBLN','XRF','MLSS','MICT','SOLY','NMRD','INUV','VTGN',
                'MTSL','DXR','QADA','MYOV','BOSC','APTO','PESI','TITN','EYEG','CAPR','UROV','APDN','TTPH','ECOR','WYND','ZN',
                'OSN','HDSN','BDR','TBLT','PLM','DMRC','MOV','PVH','TLYS','CPAH','SDRL','RWLK','VEEV','OPRX','RAVE',
                'PFSW','SPWH','TMDX','DOOO','TC','NBY','WSTL','KEYS','DBI','RVLT','JASN','CNET','RVLV','REKR','SUMR',
                'MBOT','BDGE','FOLD','SRRA','IDN', 'PIXY','LYL','MHLD','NIO','SLS','NNVC', 'MYT','BYND','CREG',
                'TCCO','AAMC','OXBR','ANCN','BCRX','ALRN','RTW','LTBR','WWR','VTVT','MACK','NDRA','OTLK','MYT','BYND',
                'CREG','TCCO','AAMC','OXBR','ANCN','BCRX','ALRN','RTW','LTBR','WWR','HTHT','MACK']

PORTFOLIO = market_return(Stock_Symbols, '2019-06-28', '2019-08-31')

[T, N] = PORTFOLIO.shape # 44 100

''' Continue... '''
