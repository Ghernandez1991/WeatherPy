from data_cleaning_and_validation.data_manipulation import DataManipulation
from pathlib import Path


def main():
    data_manipulation_class = DataManipulation()
    validated_path = Path(f"validated_data/")
    df = data_manipulation_class.concat_all_frames(validated_path)
    for file in validated_path.glob("*"):
        print(file.parts[-1])
        data_manipulation_class.move_to_processed_from_validated(file.parts[-1])


if __name__ == "__main__":
    main()
