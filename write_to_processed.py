from data_cleaning_and_validation.data_manipulation import DataManipulation
from pathlib import Path


def main():
    data_manipulation_class = DataManipulation()
    validated_path = Path(f"validated_data/")
    try:
        df = data_manipulation_class.concat_all_frames(validated_path)
    except ValueError:
        print("no files to concat")
        pass
    for file in validated_path.glob("*"):
        print(file.parts[-1])
        data_manipulation_class.move_to_processed_from_validated(file.parts[-1])

    db_path = Path("weather.db")
    csv_path = Path("processed_data/all_data.csv")
    table_name = "all_weather_data"
    data_manipulation_class.write_csv_to_sqlite(csv_path, db_path, table_name)


if __name__ == "__main__":
    main()
