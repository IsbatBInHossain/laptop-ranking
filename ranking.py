import pandas as pd
from data_cleaning import clean_data
from processor_scoring import score_processor_type, score_intel_processor, score_amd_processor, score_apple_processor, score_by_core_count
from component_scoring import score_price, score_ram, score_screen, score_storage, score_graphics
from constants import tolerance

def score_processor_generation(processor):
    if not isinstance(processor, str):
        return 0
    gen = processor.lower()
    return (score_intel_processor(gen) or 
            score_amd_processor(gen) or 
            score_apple_processor(gen) or 
            score_by_core_count(gen) or 0)

#  Ranking laptops based on weighted scores
def rank_laptops(df, weights):
    df['ProcessorScore'] = df['Processor Type'].apply(score_processor_type) * 0.3 + df['Processor Type'].apply(score_processor_generation) * 0.7
    df['RAMScore'] = df['RAM'].apply(score_ram)
    df['StorageScore'] = df.apply(lambda x: score_storage(x['Disk Type'], x['Storage Capacity']), axis=1)
    df['GraphicsScore'] = df['Graphics Card'].apply(score_graphics)
    df['ScreenScore'] = df['Screen Size'].apply(score_screen)
    df['PriceScore'] = df['Price'].apply(lambda x: score_price(x, tolerance, df['Price'].min(), df['Price'].max()))
    
    df['TotalScore'] = sum(df[score] * weight for score, weight in weights.items())
    df['NormalizedScore'] = (df['TotalScore'] - df['TotalScore'].min()) / (df['TotalScore'].max() - df['TotalScore'].min()) * 100

    return df.sort_values('NormalizedScore', ascending=False)
