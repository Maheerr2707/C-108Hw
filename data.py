import pandas as pd
import csv
import plotly.figure_factory as ff


df = pd.read_csv("data.csv")

roll_no = df["Marks In Percentage"].tolist()

fig = ff.create_distplot([roll_no],["Marks In Percentage"],show_hist=False)
fig.show()