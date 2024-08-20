import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def load_data(file_path):
    return pd.read_csv(file_path)


def perform_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r_squared = r2_score(y, y_pred)
    return model, y_pred, mse, r_squared


def save_model(model, output_folder, target):
    model_filename = os.path.join(
        output_folder, f"linear_regression_model_{target}.joblib"
    )
    joblib.dump(model, model_filename)
    print(f"Model saved to {model_filename}")


def save_plot(X, y, y_pred, output_folder, target):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color="blue", label="Actual")
    plt.plot(X, y_pred, color="red", linewidth=2, label="Predicted")
    plt.xlabel("Feature")
    plt.ylabel(target)
    plt.title(f"Linear Regression for {target}")
    plt.legend()
    image_filename = os.path.join(output_folder, f"linear_regression_plot_{target}.png")
    plt.savefig(image_filename)
    print(f"Plot saved to {image_filename}")
    plt.close()


def save_results_csv(results, output_folder, filename):
    results_df = pd.DataFrame(results)
    results_csv_path = os.path.join(output_folder, f"{filename}_regression_results.csv")
    results_df.to_csv(results_csv_path, index=False)
    print(f"Regression results saved to {results_csv_path}")


def process_files_in_folder(folder_path, filename, new_folder_name):
    file_path = os.path.join(folder_path, filename)
    output_folder = os.path.join(folder_path, new_folder_name)
    create_directory(output_folder)

    data = load_data(file_path)
    X = data[["id"]]
    target_columns = [f"y{str(i).zfill(2)}_Normalize" for i in range(1, 11)]
    individual_results = []

    for target in target_columns:
        if target in data.columns:
            y = data[target]
            model, y_pred, mse, r_squared = perform_regression(X, y)
            print(
                f"Regression results for {filename}: MSE={mse:.4f}, R-squared={r_squared:.4f}"
            )
            individual_results.append(
                {
                    "target_variable": target,
                    "MSE": f"{mse:.4f}",
                    "R-squared": f"{r_squared:.4f}",
                }
            )
            save_model(model, output_folder, target)
            save_plot(X, y, y_pred, output_folder, target)

    save_results_csv(individual_results, output_folder, new_folder_name)
    return {filename: [res["R-squared"] for res in individual_results]}


def generate_combined_r_squared_chart(r_squared_data, subfolders, base_path):
    plt.figure(figsize=(14, 8))
    for filename, r_squared_values in r_squared_data.items():
        plt.plot(subfolders, r_squared_values, marker="o", label=filename)
    plt.xlabel("Folder Number")
    plt.ylabel("R-squared")
    plt.title("R-squared Values for Folders 1 to 13")
    plt.legend()
    plt.grid(True)
    combined_chart_path = os.path.join(base_path, "combined_r_squared_chart.png")
    plt.savefig(combined_chart_path)
    plt.show()
    print(f"Combined R-squared chart saved to {combined_chart_path}")


def main():
    base_path = "C:\\Users\\614\\Desktop\\Normalize"
    subfolders = [str(i) for i in range(1, 14)]
    filenames = {
        "Regression_a": "normalized_a.csv",
        "Regression_b": "normalized_b.csv",
        "Regression_c": "normalized_c.csv",
        "Regression_d": "normalized_d.csv",
    }

    all_r_squared = {}
    for subfolder in subfolders:
        folder_path = os.path.join(base_path, subfolder)
        for new_folder_name, filename in filenames.items():
            r_squared_data = process_files_in_folder(
                folder_path, filename, new_folder_name
            )
            all_r_squared.update(r_squared_data)

    generate_combined_r_squared_chart(all_r_squared, subfolders, base_path)


if __name__ == "__main__":
    main()
