#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:04:18 2017

@author: abhivora
"""

import pandas as pd
import datetime
#from datetime import date,time,datatime
#import calender 
 

def get_data(file_name):
 data = pd.read_csv(file_name)
 day = []
 sentiment= []
 for i,j in zip(data['sentiment'],data['time']):
        sentiment.append(i)
        day.append(j)
 return day,sentiment       
        

day,sentiment = get_data('news_6.csv')   

year = []
month =[]
new_day =[]
whole_date=[]
for i in range(len(day)):   # THIS LOOP REMOVES THE TIME AND THE UNWANTED CHARACTERS IN THE TIME COLUMN I.E TO KEEP ONLY THE DATE
       
     year.append(int(day[i][0:4]))   
     month.append(int(day[i][5:7]))
     new_day.append(int(day[i][8:10])) #Type casting to make compatible for the date to day function
     whole_date.append(day[i][0:10])  
     





weekday = [];                   # THIS PART HELPS US GET THE DAY From the date

DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
for i in range(len(day)):
    
  a=year[i]
  b=month[i]
  c=new_day[i]
  weekday.append(DayL[datetime.date(a,b,c).weekday()] + 'day')




  
#date_sentiment = dict()
#
#for line in list:
#    if line[0] in date_sentiment:
#        # append the new number to the existing array at this slot
#        date_sentiment[line[0]].append(line[1])
#    else:
#        # create a new array in this slot
#        date_sentiment[line[0]] = [line[1]]  
  
  

news_date_sentiment = {} # MADE A EMPTY DICTIONARY, WHERE THE KEY = DATE.
for i in whole_date:
    news_date_sentiment[i] = []

#print(news_date_sentiment) 

 
  


   
