from data_cleaning_and_validation.data_manipulation import DataManipulation
from pathlib import Path
import pandas as pd


# create path objects for data
df1 = Path("data/data2023-05-31_00-20-44.csv")
df2 = Path("data/data2023-06-04_09-20-34.csv")

# create path object to data directory
raw_path = Path("data/")
# instiantiate data manipulation class
data_class_var = DataManipulation()
# read in df 1 path, keeping the first column as the index
df = pd.read_csv(df1, index_col=0)

print(df.dtypes)
print(df.columns)

# create absolute path to your home directory for great expectations
raw_path_2 = Path("/home/gshernandez/Desktop/weatherpy/WeatherPy")
# get a list of columns
schema_columns = df.columns
# create expectations
validation_suite = data_class_var.create_expectation_suite("suite1", schema_columns)

# process the df and validate the rules
validation_results = data_class_var.validate_dataset(df, validation_suite)

data_class_var.review_results(validation_results)

# data_class_var.move_to_validated("data2023-05-31_00-20-44.csv")
# data_class_var.move_to_raw("data2023-05-31_00-20-44.csv")
