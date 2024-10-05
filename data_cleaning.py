import pandas as pd
import numpy as np

def clean_data(df):
    df = df.dropna(subset=['Price', 'Processor Type', 'RAM'])
    df['Price'] = df['Price'].str.replace('৳', '').str.replace(',', '').astype(float)
    df['RAM'] = df['RAM'].str.extract('(\d+)').astype(float)
    df['Storage Capacity'] = df['Hard Disk'].str.extract('(\d+)').astype(float)
    df.loc[df['Hard Disk'].str.contains('TB', case=False), 'Storage Capacity'] *= 1024
    return df
