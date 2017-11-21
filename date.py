# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:22:16 2017

@author: shubham
"""
#load Datatime library
import datetime

#give current date
def get_start_Date():
    start_date=datetime.datetime.now()
    print(start_date.strftime("%Y-%m-%d"))
    
def get_End_date():
    end_date=datetime.datetime.today()
    day_value=datetime.datetime.weekday(end_date)
    if(day_value == 4):
        end_date=datetime.datetime.now() + datetime.timedelta(days=3)
    print(end_date.strftime("%Y-%m-%d"))
    
get_start_Date()    
get_End_date()