# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:59:12 2020

@author: matt_
"""

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import Stock_Checker_Funcs as scf
import matplotlib.pyplot as plt
import sys

stocks_array = []
orig_inv_val = 1580
    

"""Put share value and company data intle a tuple and then append onto the stocks array """
stocks_array.append(scf.get_stock_price('https://www.nzx.com/instruments/MEL',
                'Meridian Energy Limited Bonds|MEL|',
                'Meridian Energy',72.472293))

if stocks_array[0] == None:
    sys.exit('MARKET VALUES ON NZX HAVE BEEN RESET OVERNIGHT, PLEASE WAIT FOR MARKETS TO REOPEN BEFORE TRYING AGAIN')

stocks_array.append(scf.get_stock_price('https://www.nzx.com/instruments/KMD',
                'Company Announcements|KMD|',
                'Kathmandu Holdings Limited',210.235290))

stocks_array.append(scf.get_stock_price('https://www.nzx.com/instruments/ZEL',
                'Z Energy Limited Bonds|ZEL|',
                'Z Energy Limited',160.483870))

stocks_array.append(scf.get_stock_price('https://www.nzx.com/instruments/FNZ',
                '|Dividends|Company Announcements|FNZ|',
                'NZ Top 50 Smartshares ETF',153.945740))

scf.write_csv(stocks_array)

csv_data = pd.read_csv('Stock_Values.txt')

scf.plot_stock_values(csv_data)



    



