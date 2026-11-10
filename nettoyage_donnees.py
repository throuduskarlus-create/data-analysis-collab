import pandas as pd

df = pd.read_csv("data/ventes.csv")

print("Nombre de lignes :", len(df))

print(df.head(5))