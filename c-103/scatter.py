import pandas as pd
import plotly_express as px

db = pd.read_csv("data.csv")
fig = px.scatter(db,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
fig.show()