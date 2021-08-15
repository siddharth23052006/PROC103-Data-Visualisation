import pandas as pd
import plotly.express as px

df = pd.read_csv("COVID_data.csv")
fig = px.scatter(df, x="date", y="cases", color="country", title="COVID cases by country over time")
fig.show()