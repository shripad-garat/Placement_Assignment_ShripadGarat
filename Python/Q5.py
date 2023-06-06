"""Question 5 -
Write a program to download the data from the given API link and then extract the following data with
proper formatting
Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
Note - Write proper code comments wherever needed for the code understanding"""
import requests, json
import pandas as pd 
API_URL = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

def remove_html_tags(text):
   try:
        """Remove html tags from a string"""
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
   except Exception as e:
       raise e

def extract_API_data():
    try:
        resp = requests.get(API_URL)
        data = resp.json()
        raw_data = pd.DataFrame(data['_embedded']['episodes'])
        req_dat = ['id','url','name','season','number','type','airdate','airtime','runtime','rating','summary','image']
        unfin_data = raw_data[req_dat]
        return unfin_data


    except Exception as e:
        raise e
    

def making_data_frame(unfin_data):
    try:
        unfin_data['average rating'] = unfin_data['rating'].apply(lambda x: x['average'])
        unfin_data.drop('rating',axis=1,inplace=True)
        unfin_data['medium image link'] = unfin_data['image'].apply(lambda x: x['medium'])
        unfin_data['Original image link'] = unfin_data['image'].apply(lambda x: x['original'])
        unfin_data.drop('image',axis=1,inplace=True)
        unfin_data['summary'] = unfin_data['summary'].apply(lambda x: str(x))
        unfin_data['summary'] = unfin_data['summary'].apply(lambda x: remove_html_tags(x))
        return unfin_data

    except Exception as e:
        raise e
    
def saving_file(data):
    try:
        data.to_csv("tv.csv",header=True,index=False)

    except Exception as e:
        raise e
    
data = extract_API_data()
data = making_data_frame(unfin_data=data)
saving_file(data=data)