"""Question 7 -
Using the data from Question 4, write code to analyze the data and answer the following questions Note -
1. Draw plots to demonstrate the analysis for the following questions for better visualizations
2. Write code comments wherever required for code understanding
Insights to be drawn -
● Get all the Earth meteorites that fell before the year 2000
● Get all the earth meteorites co-ordinates who fell before the year 1970
● Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more
than 10000kg"""

import pandas as pd 
data_set = "nasa.csv"

def import_data():
    try:
        data = pd.read_csv(data_set)
        return data

    except Exception as e:
        raise e
    
def Q1(data):
    try:
        data['year'] = data['year'].apply(lambda x : int(str(x).split("-")[0]))
        return data[data['year']<2000]['Name of Earth Meteorite']

    except Exception as e:
        raise e
    
def Q2(data):
    try:
        data['year'] = data['year'].apply(lambda x : int(str(x).split("-")[0]))
        return data[data['year']<2000]['point coordinates']

    except Exception as e:
        raise e
    
def Q3(data):
    try:
        return data[data['mass']>10000]['Name of Earth Meteorite']

    except Exception as e:
        raise e
    

data = import_data()
print(f"Q1.Get all the Earth meteorites that fell before the year 2000\n {Q1(data=data)}")
print(f"Q2.Get all the earth meteorites co-ordinates who fell before the year 1970\n {Q2(data=data)}")
print(f"Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg\n {Q3(data=data)}")
