import pandas as pd
from sqlalchemy import create_engine

#================================
#LOAD DATASET
#================================

file_path=r'C:/vscode/Uber_Eats_Project/data/Uber_Eats_data.csv'
df=pd.read_csv(file_path)

order_file_path=r'C:/vscode/Uber_Eats_Project/data/orders.json'
df1=pd.read_json(order_file_path)
print('Dataset Loaded Successfully')
print(df.head())
print(df1.head())

#================================
#DATA CLEANING
#================================

#Remove duplicates
df.drop_duplicates(inplace=True)
df1.drop_duplicates(inplace=True)

#remove rows with missing restaurent names
df.dropna(subset=['name'], inplace=True)
df1.dropna(subset=['order_id'], inplace=True)

#-----------------------------------
#clean rate column
#Example:4.2/5->4.2
#-----------------------------------

df['rate']=df['rate'].str.replace('/5','',regex=False)
df['rate']=df['rate'].str.replace('NEW','',regex=False)
df['rate']=df['rate'].str.replace('-','',regex=False)

df['rate']=pd.to_numeric(df['rate'], errors='coerce')
df['rate'].fillna(df['rate'].mean(), inplace=True)

#-----------------------------------
#clean votes column
#-----------------------------------

df['votes']=pd.to_numeric(df['votes'], errors='coerce')
df['votes'].fillna(df['votes'].mean(), inplace=True)

#-----------------------------------
#clean cost column
#-----------------------------------

cost='approx_cost(for two people)'
df[cost]=df[cost].astype(str)
df[cost]=df[cost].str.replace(',','',regex=False)
df[cost]=pd.to_numeric(df[cost], errors='coerce')
df[cost].fillna(df[cost].mean(), inplace=True)

#-----------------------------------
#Rename columns
#-----------------------------------
df.rename(columns={'approx_cost(for two people)':'approx_cost',
                'listed_in(type)':'listed_in_type',
                'listed_in(city)':'listed_in_city'},inplace=True)

#-----------------------------------
#fill missing values
#-----------------------------------
df.fillna('NA', inplace=True)

print('Data Cleaning Completed Successfully')
print(df.head())

#================================
#Connect MySQL Workbench
#================================

username='root'
password="RRRR"
host='localhost'
database='Uber_Eats_db'

engine=create_engine(
    f'mysql+pymysql://{username}:{password}@{host}/{database}')

#================================
#Upload Restaurants Data to MySQL
#================================
df.to_sql(
    name='restaurants',
    con=engine,
    if_exists='replace',
    index=False)

#================================
# Upload Orders Data to MySQL
#================================

df1.to_sql(
    name='orders',
    con=engine,
    if_exists='replace',
    index=False)


print('\nData inserted into MySQL successfully!')