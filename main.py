from data_cleaning_and_validation.data_manipulation import DataManipulation
from pathlib import Path
import pandas as pd


df1 = Path("data/data2023-05-31_00-20-44.csv")
df2 = Path("data/data2023-06-04_09-20-34.csv")

print(df1, df2)
raw_path = Path("data/")
data_class_var = DataManipulation()
df = pd.read_csv(df1, index_col=0)
print(df.columns)


raw_path_2 = Path("/home/gshernandez/Desktop/weatherpy/WeatherPy")

schema_columns = df.columns
validation_suite = data_class_var.create_expectation_suite("suite1", schema_columns)


validation_results = data_class_var.validate_dataset(df, validation_suite)
