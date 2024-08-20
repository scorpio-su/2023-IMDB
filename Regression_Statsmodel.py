import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    """Load the CSV data from the given file path."""
    return pd.read_csv(file_path)


def prepare_data(data, y_col, X_col):
    """Prepare the dependent and independent variables for regression."""
    X = data[X_col]
    Y = data[y_col]
    X = sm.add_constant(X)
    return X, Y


def perform_regression(X, Y):
    """Perform the regression analysis and return the results."""
    model = sm.OLS(Y, X)
    results = model.fit()
    return results


def print_regression_results(results):
    """Print the regression results in a formatted manner."""
    print("迴歸分析結果：")
    print(f"決定係數 (R-squared): {results.rsquared:.4f}")

    print("\n迴歸係數及其統計指標：")
    coefficients = results.params
    p_values = results.pvalues
    std_errors = results.bse

    for i in range(len(coefficients)):
        print(f"變數: {coefficients.index[i]}")
        print(f"  迴歸係數: {coefficients[i]:.4f}")
        print(f"  標準誤差: {std_errors[i]:.4f}")
        print(f"  P值: {p_values[i]:.4f}\n")


def plot_data(data, x_vars, y_vars):
    """Create and display the regression plot."""
    sns.pairplot(data, x_vars=x_vars, y_vars=y_vars, height=5, aspect=0.8, kind="reg")
    plt.show()


def main(file_path):
    """Main function to execute the regression analysis and plotting."""
    data = load_data(file_path)
    X, Y = prepare_data(data, y_col="id", X_col="y01_Normalized")
    results = perform_regression(X, Y)
    print_regression_results(results)
    plot_data(data, x_vars=["id"], y_vars=["y01_Normalized"])


if __name__ == "__main__":
    file_path = "C:\\Users\\614\\Desktop\\Normalize\\1\\normalized_a.csv"
    main(file_path)
