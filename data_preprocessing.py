import pandas as pd

# Load and preprocess the sales data from the CSV file
def load_and_preprocess_sales_data(file_path):
    data = pd.read_csv(file_path)

    # Data Preprocessing (basic data cleaning)
    data.dropna(inplace=True)  # Handle missing values
    data.drop_duplicates(inplace=True)  # Handle duplicates

    # Save the preprocessed data to a new CSV file
    data.to_csv("Preprocessed_Sales_Data.csv", index=False)

    return data
