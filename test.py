# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:01:33 2017

@author: shubham
"""

import pandas as pd
import date


start_date=str(date.get_start_Date)
end_date=str(date.get_End_date)
print(type(start_date))
print(type(end_date))

df=pd.read_excel("C:\\Users\\shubham\\Desktop\\a.xlsx")
print(df[(df['Mapexipry'] >='20171121') & (df['Mapexipry'] <= '20171124')].head())
