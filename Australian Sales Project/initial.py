import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('AusApparalSales4thQrt2020.csv')

######Data CleanUp 

#Cleaning  duplicate, incorrect, and missing data
null_values = df.isnull().sum() # null values are 0 , there are no null values in the dataset
date_values = df['Date'].value_counts() # No incorrect data found in Date column
time_values = df['Time'].value_counts() # No incorrect data found in Time column 
state_values = df['State'].value_counts() # No incorrect data found in State column
group_values = df['Group'].value_counts() # No incorrect data found in Group column

duplicates = df[['Date' , 'Time' , 'State' , 'Group']].duplicated().sum() #No duplicates found in dataset

#Changing Date column to datetime datatype
replacements = {"Oct" : "10" , "Nov" : "11" , "Dec" : "12" , "-" : "/"}

for old , new in replacements.items():
    df['Date'] = df['Date'].str.replace(old , new)

df['Date'] = pd.to_datetime(df['Date'] , dayfirst=True, errors='coerce')
df.dropna(subset=['Date'] , inplace=True)

for col in ['Time' , 'State' , 'Group']:
    df[col] = df[col].astype('category')


bins = [1, 17, 33, 49, 65]
labels = ['2–17', '18–33', '34–49', '50–65']
df['Unit_Binned'] = pd.cut(df['Unit'], bins=bins, labels=labels, right=True)

 





