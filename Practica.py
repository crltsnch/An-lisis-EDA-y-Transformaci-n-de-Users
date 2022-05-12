import pandas as pd

df= pd.read_csv("navegacion", ",")
df1=df["url_landing"].str.split("[=]", expand=True)


