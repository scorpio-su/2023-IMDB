import matplotlib.pyplot as plt
import pandas as pd
import os


def plot_columns(df, mode="separate", save_folder="plots"):
    """
    Plot the columns of the DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame containing the data to plot.
        mode (str): 'separate' to plot each column individually,
                    'combined' to plot all columns in one plot.
    """
    # 如果指定的文件夹不存在，则创建它
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    if mode == "separate":
        for col in df.columns:
            plt.figure()
            df[col].plot(title=f"Plot of {col}")
            plt.xlabel("Index")
            plt.ylabel(col)
            # 保存图表
            plt.savefig(os.path.join(save_folder, f"{col}_plot.png"))
            # plt.show()

    elif mode == "combined":
        plt.figure()
        for col in df.columns:
            plt.plot(df.index, df[col], label=col)
        plt.title("Combined Plot")
        plt.xlabel("Index")
        plt.ylabel("Values")
        plt.legend()
        # 保存图表
        plt.savefig(os.path.join(save_folder, "combined_plot.png"))
        # plt.show()
    else:
        raise ValueError("Mode must be 'separate' or 'combined'")


# 主程式
def main():
    # CSV 文件列表
    file_names = ["a", "b", "c", "d"]
    number = "1"
    path = "./" + number + "/normalized_"
    start, bw = 11, 10
    for file_name in file_names:
        # 创建一个以文件名命名的文件夹来保存图表
        save_folder = "./" + number + "/" + file_name
        print(save_folder)
        # 讀取 CSV 文件
        file_name = path + file_name + ".csv"
        df = pd.read_csv(file_name)

        # 提取第 11 到第 20 行的數據
        df_slice = df.iloc[
            :, start : start + bw
        ]  # 10是第11行的索引，20是第21行的索引（不包含）
        # print(df_slice)
        # 打印當前處理的文件名
        print(f"Plotting data from {file_name}")

        # 绘制提取后的数据并保存到对应的文件夹
        plot_columns(df_slice, mode="combined", save_folder=save_folder)
        plot_columns(df_slice, save_folder=save_folder)


# 只在直接運行該腳本時執行 main 函數
if __name__ == "__main__":
    main()
