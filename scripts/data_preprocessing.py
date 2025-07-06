import pandas as pd
from pathlib import Path

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)

    print("Columns in the dataset:", data.columns.tolist())

    if 'date' not in data.columns:
        raise ValueError("The 'date' column is not found in the dataset.")

    data['date'] = pd.to_datetime(data['date'], format='mixed', dayfirst=True)

    
    data.ffill(inplace=True)

   
    sales_data = data.groupby('date').sum()

    return sales_data

if __name__ == "__main__":

    raw_data_path = Path('../data/Sales_data.csv')
    processed_data_path = Path('../data/processed_sales_data.csv')

 
    if not raw_data_path.exists():
        raise FileNotFoundError(f"The file {raw_data_path} does not exist.")

    sales_data = load_and_preprocess_data(raw_data_path)

    sales_data.to_csv(processed_data_path)
