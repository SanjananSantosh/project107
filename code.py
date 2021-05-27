import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.scatter(
            x=df.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            size="Percentage",color="attempt",
            orientation='h'))

fig.show()



