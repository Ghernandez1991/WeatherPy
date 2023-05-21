#import dependencies
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from citipy import citipy
#import API key
from config import api_key
from datetime import date



def create_cities_df():
    #set file destination 
    output_data_file = "output_data/cities_2022.csv"
        #set lat and long range when finding the lists of cities
    lat_range = (-90, 90)
    lng_range = (-180, 180)
    #setting each response we get back from api to a list 
    lat_lngs = []
    temp_responses = []
    cities = []
    hum_responses = []
    cloud_responses = []
    wind_speed_res = []
    city_id_responses = []
    country_responses = []
    lat_lng_responses = []

    #Create a set of random lat and lng combinations
    lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
    lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
    lat_lngs = zip(lats, lngs)

    #Identify nearest city for each lat, lng combination
    for lat_lng in lat_lngs:
        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
        
    #If the city is unique, then add it to a our cities list
        if city not in cities:
            cities.append(city)

    # Print the city count to confirm sufficient count
    #len(cities)
    cities

    #create a data frame from the cities list
    #each column is just a list
    cities_df = pd.DataFrame({
        "Temp_max": [],
        "Humidity": [],
        " Cloudiness ": [], 
        "wind_speed": [],
        "city_id": [],
        "country_code": [],
        "long": [],
        "lat": []
    })
    #view blank dataframe    
    cities_df.head()
    #assign list cities to column name ['City_name']
    #add cities list as a column 
    cities_df['City_name'] = cities
        
    #check how many cities we have in the list    
    #cities_df.head()
    len(cities_df.City_name)

    return cities_df


def api_query(cities_df):

    #partial url 
    units = 'Imperial'
    url = "http://api.openweathermap.org/data/2.5/weather?"
    #query_url = f"{url}appid={api_key}&q={cities}&units={units}"
    query_url = f"{url}appid={api_key}&units={units}&q="
  
    
    
    # due to the limits of our API subscription, I m only running this once. The data from the earlier tests was using a list of 10 items
    #this uses a full list 
    # use iterrows to iterate through pandas dataframe
    for index, row in cities_df.iterrows():

        # get cityname from df
        city_name1 = row['City_name']



        # assemble url and make API request
        print(f"Retrieving Results for Index {index}: {city_name1}.")

        weather_data = requests.get(query_url + city_name1).json()
        # extract results
        try:
            results_lat = weather_data['coord']['lat']    
            country_code = weather_data['sys']['country']
            results_lng = weather_data['coord']['lon']
            city_id = weather_data['id']
            wind_speed = weather_data['wind']['speed']
            clouds = weather_data['clouds']['all']
            humidity = weather_data['main']['humidity']
            max_temp = weather_data['main']['temp']



            cities_df.loc[index, 'lat'] = results_lat
            cities_df.loc[index, 'country_code'] = country_code
            cities_df.loc[index, 'long'] = results_lng
            cities_df.loc[index, 'city_id'] = city_id
            cities_df.loc[index, 'wind_speed'] = wind_speed
            cities_df.loc[index, 'Cloudiness'] = clouds
            cities_df.loc[index, 'Humidity'] = humidity
            cities_df.loc[index, 'Temp_max'] = max_temp
        except (KeyError, IndexError):
            print("Missing field/result... skipping.")
        print("------------")
        time.sleep(3)
        
    #drop the duplicate cloudiness column that had no data
    clean_df1 = cities_df.drop([cities_df.columns[2]], axis='columns')
    clean_df2 = clean_df1[['City_name', 'Temp_max', 'Humidity', 'wind_speed', 'city_id', 'country_code', 'long', 'lat', 'Cloudiness']]
    final_clean_df = clean_df2.dropna()
    today = date.today()
    day = today.day
    month = today.month
    year = today.year
    
    #save file to csv
    final_clean_df.to_csv(f'data_{month}_{day}_{year}.csv')
    


if __name__ == '__main__':
    df = create_cities_df()
    print(df.columns)
    print(df.head())
    api_query(df)