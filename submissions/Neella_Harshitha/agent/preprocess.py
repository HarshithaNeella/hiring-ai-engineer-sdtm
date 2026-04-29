import pandas as pd

def preprocess_data(df):
    df.columns = [c.strip() for c in df.columns]
    return df