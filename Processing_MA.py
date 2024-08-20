import os
import pandas as pd
import matplotlib.pyplot as plt


def create_directory(path):
    """Ensure the directory exists; create it if it does not."""
    if not os.path.exists(path):
        os.makedirs(path)


def load_csv(file_path):
    """Load CSV file into a DataFrame."""
    return pd.read_csv(file_path, index_col=0)


def calculate_moving_average(data, window_size):
    """Calculate the moving average."""
    return data.rolling(window=window_size).mean()


def plot_moving_average(
    original_data, moving_average, output_file, column, window_size
):
    """Plot the moving average and save it as a PNG file."""
    plt.figure(figsize=(12, 6))
    plt.plot(original_data, label="Original Data", color="blue")
    plt.plot(
        moving_average, label=f"Moving Average (window={window_size})", color="red"
    )
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(f"Column {column} - Moving Average")
    plt.legend()
    plt.savefig(output_file, format="png")
    plt.close()


def process_file(folder_path, file_name, output_folder_path, window_size):
    """Process a single file, calculate the moving average, and save the plot."""
    file_path = os.path.join(folder_path, file_name)
    df = load_csv(file_path)

    for column in df.columns:
        original_data = df[column]
        moving_average = calculate_moving_average(original_data, window_size)

        output_dir = os.path.join(output_folder_path, f"{file_name[:-4]}_MA_plots")
        create_directory(output_dir)

        output_file = os.path.join(
            output_dir, f"{column}_{window_size}_moving_average.png"
        )
        plot_moving_average(
            original_data, moving_average, output_file, column, window_size
        )


def main():
    base_path = "C:\\Users\\614\\Desktop\\2024-pre-train"
    output_base_path = "C:\\Users\\614\\Desktop\\Normalize"
    folders = [str(i) for i in range(1, 14)]
    files = ["a.csv", "b.csv", "c.csv", "d.csv"]
    window_size = 50

    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        output_folder_path = os.path.join(output_base_path, folder)
        create_directory(output_folder_path)

        for file_name in files:
            process_file(folder_path, file_name, output_folder_path, window_size)

    print("All plots have been saved.")


if __name__ == "__main__":
    main()
