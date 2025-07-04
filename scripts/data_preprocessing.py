import pandas as pd
from pathlib import Path

def load_and_preprocess_data(file_path):
    # Load data
    data = pd.read_csv(file_path)

    # Print column names to verify
    print("Columns in the dataset:", data.columns.tolist())

    # Check if 'date' column exists
    if 'date' not in data.columns:
        raise ValueError("The 'date' column is not found in the dataset.")

    # Convert date column to datetime with mixed format
    data['date'] = pd.to_datetime(data['date'], format='mixed', dayfirst=True)

    # Handle missing values
    data.ffill(inplace=True)

    # Aggregate data by date
    sales_data = data.groupby('date').sum()

    return sales_data

if __name__ == "__main__":
    # Define paths using pathlib
    raw_data_path = Path('../data/Sales_data.csv')
    processed_data_path = Path('../data/processed_sales_data.csv')

    # Check if the file exists
    if not raw_data_path.exists():
        raise FileNotFoundError(f"The file {raw_data_path} does not exist.")

    # Load and preprocess the data
    sales_data = load_and_preprocess_data(raw_data_path)

    # Save the processed data
    sales_data.to_csv(processed_data_path)
