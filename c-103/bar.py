import pandas as pd
import plotly_express as px

db = pd.read_csv("data.csv")
fig = px.bar(db,x="Country",y="InternetUsers")
fig.show()