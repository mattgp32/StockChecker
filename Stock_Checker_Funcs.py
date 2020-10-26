# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:38:49 2020

@author: matt_
"""

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots, show


"""Function to pull out stock values from the NZX website"""
def get_stock_price(url, search_phrase, company_name, stocks_held):
    r = requests.get(url)
    soup = soup = BeautifulSoup(''.join(r.text))
    text = soup.get_text('|', strip=True)
    location = str.find(text, search_phrase)
    start = location + len(search_phrase)
    value_string = text[start + 1: start + 6]
    if text[start] == '-':
        return_val = None
    else:
        value_float = float(value_string)
        return_val = (company_name, value_float, stocks_held)
    return return_val

def write_csv(array):
    if array[0] == None:
        pass
    else:
        currentDT = datetime.datetime.now()
        file = open("Stock_Values.txt", "a+")
        for tup in array:
            file.write(str(tup[0]) + ',' + str(tup[1]) + ',' + str(tup[2]) + ',' + str(currentDT.date()) + ',' + str(currentDT.time()) + '\n')
        file.close()
    return None

def create_graphing_array(company, dataframe):
    array = []
    company_names = dataframe['Company'].values
    share_value = dataframe['Value'].values
    date = dataframe['Date'].values
    time = dataframe['Time'].values
    for i in range(len(company_names)):
        if company_names[i] == company:
            array.append((date[i] + " " + time[i], share_value[i]))
    return array

def create_date_array(array):
    date_array = []
    for entry in array:
        date = datetime.datetime.strptime(entry[0], "%Y-%m-%d %H:%M:%S.%f")
        date_array.append(date)
    return date_array

def create_value_array(array):
    value_array = []
    for entry in array:
        value_array.append(entry[1])
    return value_array

def plot_stock_values(csv_data, company = None):
    if company != None:
        graphing_array = create_graphing_array(company, csv_data)
        date_array = create_date_array(graphing_array)
        value_array = create_value_array(graphing_array)
        plt.plot_date(date_array, value_array, xdate=True)
        plt.xlabel('Date')
        plt.ylabel('Value (NZ$)')
        plt.title(company)
    else:
        graphing_array = create_graphing_array('Meridian Energy', csv_data)
        date_array = create_date_array(graphing_array)
        mvalue_array = create_value_array(graphing_array)
        
        graphing_array = create_graphing_array('Kathmandu Holdings Limited', csv_data)
        kvalue_array = create_value_array(graphing_array)
        
        graphing_array = create_graphing_array('Z Energy Limited', csv_data)
        zvalue_array = create_value_array(graphing_array)
        
        graphing_array = create_graphing_array('NZ Top 50 Smartshares ETF', csv_data)
        ssvalue_array = create_value_array(graphing_array)
    
        fig, axs = plt.subplots(2, 2,sharex=True)
        axs[0,0].plot_date(date_array, mvalue_array, 'tab:cyan', xdate=True)
        axs[0,0].set_title('Meridian Energy')
        axs[0,1].plot_date(date_array, kvalue_array, 'tab:green', xdate=True)
        axs[0,1].set_title('Kathmandu Holdings Limited')
        axs[1,0].plot_date(date_array, zvalue_array, 'tab:orange', xdate=True)
        axs[1,0].set_title('Z Energy Limited')
        axs[1,1].plot_date(date_array, ssvalue_array, 'tab:blue', xdate=True)
        axs[1,1].set_title('NZ Top 50 Smartshares ETF')
        fig.tight_layout()
        i = 0
        for ax in axs.flat:
            if i == 2 or i == 3:
                ax.set(xlabel='Date')
            else:
                pass
            ax.set_xticks([date_array[0], date_array[-1]])
            ax.set(ylabel='Value NZ$')
            i = i + 1
            
          
    return None

