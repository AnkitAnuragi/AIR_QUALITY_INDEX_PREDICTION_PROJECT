# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:25:01 2022

@author: CCE
"""

import os
import time 
import requests
import sys

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url="https://en.tutiempo.net/climate/0{}-{}/ws-426670.html".format(month,year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}/ws-426670.html".format(month,year)
            texts=requests.get(url)
            text_utf=texts.text.encode("utf=8")
            if not os.path.exists("Html_Data/{}".format(year)):
                os.makedirs("Html_Data/{}".format(year))
            with open("Html_Data/{}/{}.html".format(year,month) , "wb") as f:
                    f.write(text_utf)
        sys.stdout.flush()



if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
