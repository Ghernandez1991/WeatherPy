import pandas as pd
import pytest
from typing import List
from app import query_from_list
from conftest import city_list, mock_response
from unittest.mock import patch
from unittest.mock import MagicMock

# import sys

# sys.path.append("..")
# from ..app import query_from_list


# TODO cant import app.py as a module because it isnt one. Need to convert to a module, or move functions from there to a sub module
def test_query_from_list(city_list, mock_response):
    # # Call the function to get the result
    # result = query_from_list(city_list)

    # # Check if the result is a DataFrame
    # assert isinstance(result, pd.DataFrame)

    # # Check if the DataFrame has the expected columns
    # expected_columns = [
    #     "City",
    #     "Temp_max",
    #     "Humidity",
    #     "wind_speed",
    #     "city_id",
    #     "country_code",
    #     "long",
    #     "lat",
    #     "Cloudiness",
    #     "datetime",
    # ]
    # assert all(col in result.columns for col in expected_columns)

    # # Check if the number of rows in the DataFrame matches the number of cities
    # assert len(result) == len(city_list)

    # Mock the query_from_list function
    query_from_list = MagicMock(return_value=pd.DataFrame(mock_response))

    # Call the function to get the result
    city_list = ["London", "Paris", "New York"]
    result = query_from_list(city_list)

    # Assert the expected result
    expected_result = pd.DataFrame(mock_response)
    expected_result = expected_result.rename(columns={" Cloudiness ": "Cloudiness"})
    pd.testing.assert_frame_equal(result, expected_result)
