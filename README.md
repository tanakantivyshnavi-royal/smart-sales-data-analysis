import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load sales data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully\n")
        return df
    except FileNotFoundError:
        print("CSV file not found. Check the file name or path.")
        exit()


def clean_data(df):
    """Clean the dataset"""
    print("Cleaning data...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing values
    df = df.dropna()

    print("Data cleaning completed\n")
    return df


def analyze_data(df):
    """Perform basic sales analysis"""
    print("Analyzing data...\n")

    print("First 5 rows of data:")
    print(df.head(), "\n")

    print("Dataset Info:")
    print(df.info(), "\n")

    print("Summary Statistics:")
    print(df.describe(), "\n")

    # Example: total sales column (change column name if needed)
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        print(f"Total Sales: {total_sales}")
    else:
        print("Column 'Sales' not found in dataset")

    print()


def visualize_data(df):
    """Visualize sales trends"""
    if "Sales" in df.columns:
        plt.figure()
        df["Sales"].plot(kind="line")
        plt.title("Sales Trend")
        plt.xlabel("Index")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.show()
    else:
        print("No 'Sales' column available for visualization")


def main():
    file_path = "Google_Ready_Order.csv"

    df = load_data(file_path)
    df = clean_data(df)
    analyze_data(df)
    visualize_data(df)


if __name__ == "__main__":
    main()
