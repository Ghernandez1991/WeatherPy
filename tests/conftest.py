import pytest
import pandas as pd

@pytest.fixture
def city_list():
    return ["London", "Paris", "New York"]



@pytest.fixture
def dataframe():
    one_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    two_df = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    return one_df,two_df
