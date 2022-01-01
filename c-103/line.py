import pandas as pd
import plotly_express as px

db = pd.read_csv("line_chart.csv")
fig = px.line(db,x="Year",y="Per capita income",color="Country",title = "Per Capita Income")
fig.show()