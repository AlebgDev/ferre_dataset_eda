import pandas as pd
import os

def load_dataset(file_name, sample_size=500000):
    """
    Load dataset from csv file
    """
    filepath = os.path.join('data', file_name)
    print(f"Loading dataset from {filepath}")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} not found")
    df = pd.read_csv(filepath, nrows=sample_size)
    print(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")
    return df
