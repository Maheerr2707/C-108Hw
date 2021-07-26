import pandas as pd
import csv
import plotly.figure_factory as ff


df = pd.read_csv("data.csv")

roll_no = df["Marks In Percentage"].tolist()

fig = ff.create_distplot([df["Marks In Percentage"].tolist()], ["Marks In Percentage"])
fig.show()