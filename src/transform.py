import os
import pandas as pd

df = pd.read_csv("data/clean/events.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["date"] = df["timestamp"].dt.strftime("%Y-%m-%d")

os.makedirs("data/transformed", exist_ok=True)
df.to_csv("data/transformed/events.csv", index=False)
