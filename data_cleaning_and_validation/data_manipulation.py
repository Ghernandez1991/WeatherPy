import pandas as pd
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import great_expectations as ge
from great_expectations.dataset import PandasDataset
from typing import List
import great_expectations as ge
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.core.expectation_validation_result import (
    ExpectationSuiteValidationResult,
)


@dataclass
class DataManipulation:
    def concat_dataframes(self, df1_path: Path, df2_path: Path) -> pd.DataFrame:
        """
        Function takse in two paths which point to pandas dataframes and concats them.
        Returns- A single dataframe of the two dataframes concatinated together
        """
        df1 = pd.read_csv(df1_path, index_col=0)
        df2 = pd.read_csv(df2_path, index_col=0)

        concatenated_df = pd.concat([df1, df2])
        concatenated_df.to_csv("data/combined_df_all.csv")
        return concatenated_df

    def concat_all_frames(self, raw_path: Path) -> pd.DataFrame:
        """
        Function takes in a Path object pointing to the raw folder where the data lands after being created from the API
        The function iterates over all objects in the path, and concats them together into one frame.
        Returns a single dataframe

        """
        all_frames = []
        for file in raw_path.glob("*"):
            current_df = pd.read_csv(file, index_col=0)
            all_frames.append(current_df)
        concatenated_df = pd.concat(all_frames)
        concatenated_df.to_csv("data/all_data.csv")
        return concatenated_df

    def move_from_raw_to_processed(self, raw_path: Path):
        # go through all files in raw path
        # move files from that path to processed
        return None

    def great_expectations_init(self, raw_path: Path) -> None:
        """Sets up great expectations in raw_path, which is expected to be your root directory
        Args- raw_path - Path object representing the root of your directory
        Returns- None
        """
        import great_expectations as gx

        context = gx.data_context.FileDataContext.create(raw_path)

    def create_expectation_suite(
        self, suite_name: str, schema_list: List[str]
    ) -> ExpectationSuite:
        """
        Function creates an expectation suite to use against a future dataset.
        args- suite_name- string of what you want to name the suite
        schema_list- a list of columns you want to apply the rules to.
        returns ExpectationSuite object

        """
        suite = ExpectationSuite(suite_name)

        # Add expectations to the suite
        expectation_configurations = []
        for column in schema_list:
            # rule expects that every column in schema_list would exist in the dataset being examined
            expectation_configurations.append(
                ExpectationConfiguration(
                    expectation_type="expect_column_to_exist",
                    kwargs={"column": column},
                )
            )
            # expects that every column in the dataset does not have null values
            expectation_configurations.append(
                ExpectationConfiguration(
                    expectation_type="expect_column_values_to_not_be_null",
                    kwargs={"column": column},
                )
            )
            # Add more expectations for each column as needed

        # Add the expectation configurations to the suite
        suite.expectations = expectation_configurations

        return suite

    def validate_dataset(
        self, df: pd.DataFrame, expectation_suite: ExpectationSuite
    ) -> ExpectationSuiteValidationResult:
        """
        function takes in the given dataframe and expectation_suite, and runs the expectations against the dataframe.
        returns the results of that validation
        """
        dataset = ge.dataset.PandasDataset(df, expectation_suite=expectation_suite)
        # Validate the dataset against the expectation suite
        validation_results = dataset.validate(
            result_format={"result_format": "COMPLETE", "include_result": True}
        )
        return validation_results
