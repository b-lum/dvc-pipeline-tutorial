import pandas as pd

df = pd.read_csv("data/transformed/events.csv")

df["duration_minutes"] = df["duration_seconds"].astype(float) / 60

df["date"] = pd.to_datetime(df["date"])

df["weekday"] = df["date"].dt.day_name()

df["date"] = df["date"].dt.strftime("%Y-%m-%d")

df.to_csv("data/features/events.csv", index=False)