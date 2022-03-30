import os

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots

"""

thingName  thingType   tvoc  hum   eco2   tmp                timestamp
"""
data_dir_contenet = os.listdir("./data_goes_here")
csv_fp = "./data_goes_here/"
for fn in data_dir_contenet:
    if fn.endswith(".csv"):
        csv_fp += fn
        break
df = pd.read_csv(filepath_or_buffer=csv_fp)
df = df.drop(columns=["thingName","thingType"])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by="timestamp")

df: pd.DataFrame = df[df["timestamp"] > "2022-03-23"]

# smooth = 1
# for col in df.columns:
#     if col not in ["timestamp"]:
#         df[col] = df[col].rolling(window=smooth, min_periods=3).mean()
# df = df.tail(200)

# Plot
# fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["tvoc"],
    name="tvoc"
),
)

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["hum"],
    name="hum"
),
secondary_y=True)

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["eco2"],
    name="eco2"
))


fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["tmp"],
    name="tmp"
),
secondary_y=True
)
fig.show()
