import pandas as pd

df = pd.read_csv("data.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df = df.drop_duplicates()

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Report")
print("-------------------")
print("Rows:", len(df))
print("Missing Values:")
print(df.isnull().sum())
print(df.describe())
