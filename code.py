import pandas as pd
import numpy as np

df = pd.read_csv("vgchartz_2024.csv")

sales_columns = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']

for col in sales_columns:
df[col] = pd.to_numeric(df[col], errors='coerce')
average_value = df[col].mean()
original_blank_count = df[col].isna().sum()
df[col] = df[col].fillna(average_value)
df[col] = df[col].round(2)
print(f"Filled {original_blank_count} blank cells in {col} with average: {average_value:.2f}")
#updated column
print("\nSales columns updated successfully!")
df[['title'] + sales_columns]

#filling critic_score nulls

df['critic_score'] = pd.to_numeric(df['critic_score'], errors='coerce')
average_score = df['critic_score'].mean()
original_blank_count = df['critic_score'].isna().sum()
df['critic_score'] = df['critic_score'].fillna(average_score)
df['critic_score'] = df['critic_score'].round(1)
#updated column
print(f"Filled {original_blank_count} blank cells with average score: {average_score:.1f}")
df[['title', 'critic_score']]
