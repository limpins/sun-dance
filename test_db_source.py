""" Test individual source parsers """

import sys
import os.path
import urllib2
import pprint

from bs4 import BeautifulSoup
from yahoo_finance import Share

import pickle

import TerminalColors
tcol = TerminalColors.bcolors()


# Processor Classes:
from stockspotter.db.SourceHKEXProfile import SourceHKEXProfile
from stockspotter.db.SourceReuters import SourceReuters
from stockspotter.db.SourceWSJ import SourceWSJ
from stockspotter.db.SourceAAStocks import SourceAAStocks


from stockspotter.db.SourceYahoo import SourceYahoo
from stockspotter.db.SourceQuotesAlphaVantage import SourceQuotesAlphaVantage
from stockspotter.db.SourceQuotesQuandl import SourceQuotesQuandl

# ticker = 'ELECTCAST.NSE'
ticker = '1133.HK'
# ticker = 'MMM.NYSE'
# ticker = 'ZYNE.NASDAQ'
# ticker = 'FAX.AMEX'
# ticker = '4333.TYO'
ticker = '532540.BSE'

# ticker = '600298.SH' #shanghai
# ticker = '000898.SZ' #shenzen
stock_prefix = 'equities_db/test_db/'+ticker+'/'

s_aastocks = SourceAAStocks( ticker, stock_prefix, 5 )
s_aastocks.retrive_detailed_company_profile()


# s_hkex = SourceHKEXProfile( ticker, stock_prefix )
# s_hkex.download_url()
# s_hkex.parse()
# A = s_hkex.load_hkex_profile()
# B = s_hkex.load_dividends_data()
# print A['Market Capitalisation']

# s_reuters = SourceReuters(ticker, stock_prefix, 5 )
# s_reuters.download_url()
# s_reuters.parse(delete_raw=False)
# s_reuters.load_raw_file()
# s_reuters.parse_financials()


# s_quote = SourceQuotesAlphaVantage( ticker, stock_prefix , 1)
# s_quote = SourceQuotesQuandl( ticker, stock_prefix , 1)
# s_quote.retrive_www(n=1003, rm_raw=True)
# Q = s_quote.load()

# s_yahoo = SourceYahoo( ticker, stock_prefix, 1 )
# s_yahoo.download_quick_quote()
# s_yahoo.load_pickle()
# s_yahoo.download_historical_quote()
# qqq = s_yahoo.load_quote()



# s_wsj = SourceWSJ( ticker, stock_prefix, 1 )
# s_wsj.download_url()
# s_wsj.parse_financial_statements()

# s_wsj.parse()
# print s_wsj.ls( 'a', 'income_statement')
# # s_wsj.parse_profile()
# s_wsj.parse_financials()
# # A = s_wsj.load_json_income_statement( 'a.2015' )
# # B = s_wsj.load_json_balance_sheet( 'a.liabilities.2015' )
# # C = s_wsj.load_json_cash_flow_statement( 'a.investing.2015' )
# # D = s_wsj.load_json_cash_flow_statement( 'a.operating.2012' )
# E = s_wsj.load_json_profile()
# F = s_wsj.load_mututal_fund_owners()
# G = s_wsj.load_institutional_investors()
