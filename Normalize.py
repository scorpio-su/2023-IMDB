import os
import pandas as pd
import matplotlib.pyplot as plt


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def load_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"File does not exist: {file_path}")
        return None


def normalize_columns(data, start_column, end_column):
    columns_to_normalize = data.columns[start_column:end_column]
    for column in columns_to_normalize:
        mean = data[column].mean()
        std = data[column].std()
        data[column] = (data[column] - mean) / std


def update_headers(data, new_headers):
    data.columns = new_headers


def save_csv(data, output_file_path):
    data.to_csv(output_file_path, index=False)
    print(f"Normalization complete: {output_file_path}")


def process_files_in_folder(
    base_path,
    output_base_path,
    folder,
    filenames,
    start_column,
    end_column,
    new_headers,
):
    folder_path = os.path.join(base_path, str(folder))
    output_folder_path = os.path.join(output_base_path, str(folder))
    create_directory(output_folder_path)

    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        data = load_csv(file_path)

        if data is not None:
            normalize_columns(data, start_column, end_column)
            update_headers(data, new_headers)
            output_file_path = os.path.join(
                output_folder_path, f"normalized_{filename}"
            )
            save_csv(data, output_file_path)


def main():
    base_path = "C:\\Users\\614\\Desktop\\2024-pre-train"
    output_base_path = "C:\\Users\\614\\Desktop\\Normalize"
    folders = range(1, 14)
    filenames = ["a.csv", "b.csv", "c.csv", "d.csv"]
    start_column = 1
    end_column = 11

    # Example new headers; adjust as needed
    new_headers = [
        "id",
        "y01_Normalize",
        "y02_Normalize",
        "y03_Normalize",
        "y04_Normalize",
        "y05_Normalize",
        "y06_Normalize",
        "y07_Normalize",
        "y08_Normalize",
        "y09_Normalize",
        "y10_Normalize",
    ]

    create_directory(output_base_path)

    for folder in folders:
        process_files_in_folder(
            base_path,
            output_base_path,
            folder,
            filenames,
            start_column,
            end_column,
            new_headers,
        )


if __name__ == "__main__":
    main()
