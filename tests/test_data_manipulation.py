import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from unittest import TestCase

from conftest import dataframe
import pandas as pd
from pathlib import Path
import pytest

from conftest import dataframe, data_manipulation


def test_concat_dataframes(dataframe, data_manipulation):
    # Prepare test data
    df1, df2 = dataframe

    # Save the dataframes as CSV files in the "test_data" folder
    test_data_folder = Path("test_data")
    test_data_folder.mkdir(
        exist_ok=True
    )  # Create the "test_data" folder if it doesn't exist

    df1_path = test_data_folder / "df1.csv"
    df2_path = test_data_folder / "df2.csv"
    df1.to_csv(df1_path)
    df2.to_csv(df2_path)

    # Concatenate the dataframes
    result = data_manipulation.concat_dataframes(df1_path, df2_path)

    # Assert the concatenated dataframe has the expected values
    expected_df = pd.DataFrame({"A": [1, 2, 3, 7, 8, 9], "B": [4, 5, 6, 10, 11, 12]})
    pd.testing.assert_frame_equal(result, expected_df)

    # Clean up the CSV files
    df1_path.unlink()
    df2_path.unlink()
    test_data_folder.rmdir()  # Remove the "test_data" folder
