import pandas as pd
from data_cleaning import clean_data
from ranking import rank_laptops
from constants import weights

def find_best_laptops(csv_file):
    df = pd.read_csv(csv_file)
    df_clean = clean_data(df)
    ranked_df = rank_laptops(df_clean, weights)
    return ranked_df

best_laptops = find_best_laptops('all_laptops.csv')

best_laptops[['Name', 'Price', 'PriceScore', 'Processor Type', 'ProcessorScore', 
              'RAM', 'RAMScore', 'Hard Disk', 'StorageScore', 'Graphics Card', 
              'GraphicsScore', 'Screen Size', 'ScreenScore', 'TotalScore','NormalizedScore']].to_csv("best_laptops.csv", index=False)

