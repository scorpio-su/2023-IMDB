import os
import pandas as pd
import matplotlib.pyplot as plt


def create_output_folder(folder_path):
    """Create a folder if it doesn't exist."""
    os.makedirs(folder_path, exist_ok=True)


def read_csv_file(file_path):
    """Read and return a DataFrame from a CSV file."""
    return pd.read_csv(file_path)


def filter_data_by_target_variable(df, target_variable):
    """Filter the DataFrame for a specific target variable."""
    return df[df["target_variable"] == target_variable]


def plot_and_save(data, output_file_path, target_variable):
    """Plot MSE and R-squared values and save the plot."""
    r_squared_values = data["R-squared"]
    mse_values = data["MSE"]

    plt.figure(figsize=(10, 6))
    plt.plot(
        r_squared_values.values, marker="o", linestyle="-", color="b", label="R-squared"
    )
    plt.plot(mse_values.values, marker="s", linestyle="-", color="g", label="MSE")

    plt.title(f"MSE & R-squared values for {target_variable}")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.grid(True)
    plt.legend(loc="upper right", bbox_to_anchor=(1, 0.5))

    plt.savefig(output_file_path, bbox_inches="tight")
    print(f"Saved figure to {output_file_path}")


def process_target_variables(df, output_folder, target_variable_range):
    """Process each target variable and create corresponding plots."""
    for i in target_variable_range:
        target_variable = f"y{i:02d}_Normalize"
        filtered_data = filter_data_by_target_variable(df, target_variable)
        output_file_path = os.path.join(
            output_folder, f"MSE_R_squared_plot_{target_variable}.png"
        )
        plot_and_save(filtered_data, output_file_path, target_variable)


def process_files(file_paths, output_folder_base):
    """Process each CSV file and create plots."""
    for file_path in file_paths:
        df = read_csv_file(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_folder = os.path.join(output_folder_base, file_name)
        create_output_folder(output_folder)
        target_variable_range = range(1, 11)
        process_target_variables(df, output_folder, target_variable_range)


def main():
    base_dir = "C:\\Users\\614\\Desktop\\Normalize\\combine"
    file_names = [
        "combined_normalized_a_regression_results.csv",
        "combined_normalized_b_regression_results.csv",
        "combined_normalized_c_regression_results.csv",
        "combined_normalized_d_regression_results.csv",
    ]
    file_paths = [os.path.join(base_dir, file_name) for file_name in file_names]
    output_folder = base_dir

    process_files(file_paths, output_folder)


if __name__ == "__main__":
    main()
