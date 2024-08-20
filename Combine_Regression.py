import os
import pandas as pd


def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def combine_csv_files(base_path, folders, subfolders, filenames):
    """Combine CSV files from multiple folders and subfolders into a single file for each filename."""
    combine_folder = os.path.join(base_path, "combine")
    create_directory(combine_folder)

    for filename in filenames:
        combined_df = pd.DataFrame()
        for folder in folders:
            for subfolder in subfolders:
                file_path = os.path.join(base_path, str(folder), subfolder, filename)
                if os.path.exists(file_path):
                    try:
                        df = pd.read_csv(file_path)
                        combined_df = pd.concat([combined_df, df], ignore_index=True)
                    except pd.errors.EmptyDataError:
                        print(f"File {file_path} is empty.")
                    except pd.errors.ParserError:
                        print(f"Error parsing {file_path}.")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
                else:
                    print(f"File {file_path} does not exist.")

        output_file = os.path.join(combine_folder, f"combined_{filename}")
        if not combined_df.empty:
            combined_df.to_csv(output_file, index=False)
            print(f"Combined file saved as {output_file}")
        else:
            print(f"No data to combine for {filename}.")


def main():
    base_path = "C:\\Users\\614\\Desktop\\Normalize"
    folders = range(1, 14)  # Folders 1 to 13
    subfolders = ["normalized_a", "normalized_b", "normalized_c", "normalized_d"]
    filenames = [
        "normalized_a_regression_results.csv",
        "normalized_b_regression_results.csv",
        "normalized_c_regression_results.csv",
        "normalized_d_regression_results.csv",
    ]

    combine_csv_files(base_path, folders, subfolders, filenames)


if __name__ == "__main__":
    main()
