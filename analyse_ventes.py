import pandas as pd

df = pd.read_csv("data/ventes.csv")

def ca(quantite, prix):
    return quantite * prix

print(f"Le Chiffre d'affaire total est de : {(ca(df['quantite'], df['prix_unitaire'])).sum():.2f} €.")