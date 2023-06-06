"""
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding"""
import pandas as pd 

URL = "https://data.nasa.gov/resource/y77d-th95.json"

def exctracting_data():
    try:
        """extrtacting the data using Given URL"""
        data = pd.read_json(URL)
        return data

    except Exception as e:
        raise e
    
def making_changes(data):
    try:
        """Making changes in given data to transform it into required data"""
        data = data.drop(["fall",":@computed_region_cbhk_fwbd",":@computed_region_nnqa_25f4"],axis=1)
        data = data.dropna()
        data['geolocation'] = data['geolocation'].apply(lambda x: x['coordinates'])
        data.columns = ['Name of Earth Meteorite','ID of Earth Meteorite','nametype','recclass','mass','year','reclat','recclong','point coordinates']
        return data

    except Exception as e:
        raise e
    
def saving_file(data):
    try:
        data.to_csv("nasa.csv",header=True,index=False)

    except Exception as e:
        raise e
    
data = exctracting_data()
data = making_changes(data=data)
saving_file(data=data)