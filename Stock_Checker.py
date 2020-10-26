# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:35:09 2020

@author: matt_
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open an instance of chrome and minimise window to get it out the way
driver = webdriver.Chrome('./chromedriver.exe')

# Load the NZX page for meridian energy
driver.get('https://www.nzx.com/instruments/MEL')

element = driver.find_element(By.NAME, "h1")
print(element)