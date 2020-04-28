# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:55:21 2020

@author: Aaron Fehir 

Objective: to make a script that will play an annoying sound if you have
            recently browsed a url containing a given string.

"""

# Libraries ##### 
from playsound import playsound
import browserhistory as bh 
import re
import time

# Accessing chrome's  browser history 
chrome =  bh.get_browserhistory()["chrome"]

# Creata a list of urls that match the pattern provided 
url_list  =[]

for i in range(0, len(chrome)):
    website = chrome [i][0] 
    if re.search(r'(L/L)inked(i|I)n', website):
        url_list.append(website)

# Play an airhorn sound if any results match
if len(url_list) > 8:
    playsound("C:/Users/User/DownLoads/airhorn.wav")
else:
    time.sleep(500)
