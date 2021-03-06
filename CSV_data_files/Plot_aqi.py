# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:52:25 2022

@author: CCE
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2013.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average

    
def avg_data_2014():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2014.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average
    
    
    
def avg_data_2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2015.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average
    
    
    
def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2016.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average
    
    
    

def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2017.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average
    
    
    

def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv("aqi2018.csv",chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1
        
        average.append(avg)
    return average
    
    
if __name__=="__main__":
    list2013=avg_data_2013()
    list2014=avg_data_2014()
    list2015=avg_data_2015()
    list2016=avg_data_2016()
    list2017=avg_data_2017()
    list2018=avg_data_2018()
    plt.plot(range(0,365),list2013,label="2013 data")
    plt.plot(range(0,364),list2014,label="2014 data")
    plt.plot(range(0,365),list2015,label="2015 data")
    plt.legend(loc=1)
    plt.show()
    


