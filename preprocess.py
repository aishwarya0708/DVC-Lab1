import pandas as pd

df = pd.read_csv('data/CC_GENERAL.csv')
print(f"V1 shape: {df.shape}")

df_cleaned = df[df['tip'] > 2]
print(f"V2 shape after cleaning: {df_cleaned.shape}")

df_cleaned.to_csv('data/CC_GENERAL.csv', index=False)
print("Saved cleaned dataset!")