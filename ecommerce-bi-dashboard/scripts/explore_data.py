import pandas as pd

try:
    # Load dataset with ISO-8859-1 encoding
    df = pd.read_csv('data/OnlineRetail.csv', encoding='ISO-8859-1')
    
    # Basic exploration
    print("Dataset Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nFirst 5 Rows:\n", df.head())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nData Types:\n", df.dtypes)

    # Save a sample for reference
    df.head(100).to_csv('data/sample_retail_data.csv', index=False)
    print("Sample saved: data/sample_retail_data.csv")
except Exception as e:
    print(f"Error loading dataset: {e}")