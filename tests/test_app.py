import pandas as pd
import pytest
from typing import List
from app import query_from_list  
from conftest import city_list

#TODO cant import app.py as a module because it isnt one. Need to convert to a module, or move functions from there to a sub module
def test_query_from_list(city_list):
    # Call the function to get the result
    result = query_from_list(city_list)
    
    # Check if the result is a DataFrame
    assert isinstance(result, pd.DataFrame)
    
    # Check if the DataFrame has the expected columns
    expected_columns = [
        "City", "Temp_max", "Humidity", "wind_speed", "city_id",
        "country_code", "long", "lat", "Cloudiness", "datetime"
    ]
    assert all(col in result.columns for col in expected_columns)
    
    # Check if the number of rows in the DataFrame matches the number of cities
    assert len(result) == len(city_list)
    
    # ... Add more specific assertions based on your function's behavior
    
