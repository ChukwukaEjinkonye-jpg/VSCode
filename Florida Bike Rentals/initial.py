#Libraries 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("FloridaBikeRentals.csv", encoding='latin1')
scaler = MinMaxScaler()

'''
Data Cleanup 

Changing Date to datetime format and drop any rows where Date is null
Chainging Temperature(°C) , Wind speed (m/s) , Solar Radiation (MJ/m2) , Rainfall(mm), Snowfall (cm) to int format
Changing columns' values to int format for faster processing and categorizing  
> df['Holiday']:    'No Holiday' ==> 0 | 'Holiday' ==> 1
> df['Functioning Day']     'No' ==> 0 | 'Yes' ==> 1
> df['Seasons']     'Winter' ==> 0 | 'Spring' ==> 1 | 'Summer' ==> 2 | 'Autumn' ==> 3
'''

df['Date'] = pd.to_datetime(df['Date'].str.replace('-', '/'), dayfirst=True, errors='coerce')
df.dropna(subset=['Date'], inplace=True)


df['Holiday'] = df['Holiday'].map({'No Holiday': 0, 'Holiday': 1})
df['Functioning Day'] = df['Functioning Day'].map({'No': 0, 'Yes': 1})
df['Seasons'] = df['Seasons'].map({'Winter': 0, 'Spring': 1, 'Summer': 2, 'Autumn': 3})

#Format to JSON 
df.to_json("bike_rental_cleaned.json", orient="records", lines=True)

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''



# df['Visibility (10m)'] = scaler.fit_transform(df[['Visibility (10m)']]) 
# df['Temperature(°C)'] = df['Temperature(°C)'] * 10

print(df.describe())
