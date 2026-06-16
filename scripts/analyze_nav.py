import pandas as pd

df = pd.read_csv("data/raw/nav_history.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)