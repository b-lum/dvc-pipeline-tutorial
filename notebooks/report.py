import marimo

app = marimo.App()

@app.cell
def _():
   import pandas as pd
   import matplotlib.pyplot as plt
   return pd, plt

@app.cell
def _(pd):
   df = pd.read_csv("data/features/events.csv")
   return df

@app.cell
def _(df, plt):
   fig, ax = plt.subplots()

   ax.hist(df["duration_minutes"], bins=30)
   ax.set_xlabel("Duration (minutes)")
   ax.set_ylabel("Frequency")
   ax.set_title("Distribution of Event Durations")

   fig