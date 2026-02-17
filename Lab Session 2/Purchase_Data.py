import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase Data")
X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
y = df["Payment (Rs)"].to_numpy()
print("X matrix:\n", X)
print("y vector:\n", y)
df["Class"] = df["Payment (Rs)"].apply(lambda x: "RICH" if x > 200 else "POOR")

model = LogisticRegression()
model.fit(X, df["Class"])
print("Classifier trained successfully.")
