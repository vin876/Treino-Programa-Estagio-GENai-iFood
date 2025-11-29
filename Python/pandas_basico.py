import pandas as pd

# LER CSV
df = pd.read_csv("../data/entregas_exemplo.csv")

# PRIMEIRAS LINHAS
print(df.head())

# ESTATÍSTICAS
print(df.describe())

# FILTRAR
atrasadas = df[df["tempo_entrega"] > 40]
print("Entregas atrasadas:")
print(atrasadas)
