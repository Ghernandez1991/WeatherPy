import pytest
import pandas as pd
from data_cleaning_and_validation.data_manipulation import DataManipulation


@pytest.fixture
def city_list():
    return ["London", "Paris", "New York"]


@pytest.fixture
def dataframe():
    one_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    two_df = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]})
    return one_df, two_df


@pytest.fixture
def data_manipulation():
    return DataManipulation()


@pytest.fixture
def mock_response():
    mock_response = mock_response = [
        {
            "City": "London",
            "Temp_max": 64.72,
            "Humidity": 50,
            "wind_speed": 5,
            "city_id": 2643743,
            "country_code": "GB",
            "long": -0.1278,
            "lat": 51.5074,
            "Cloudiness": 75,
            "datetime": 1624017600,
        },
        {
            "City": "Paris",
            "Temp_max": 66.27,
            "Humidity": 60,
            "wind_speed": 7,
            "city_id": 2988507,
            "country_code": "FR",
            "long": 2.3522,
            "lat": 48.8566,
            "Cloudiness": 40,
            "datetime": 1624017600,
        },
        {
            "City": "New York",
            "Temp_max": 79.83,
            "Humidity": 70,
            "wind_speed": 9,
            "city_id": 5128581,
            "country_code": "US",
            "long": -74.0060,
            "lat": 40.7128,
            "Cloudiness": 90,
            "datetime": 1624017600,
        },
    ]
    return mock_response
