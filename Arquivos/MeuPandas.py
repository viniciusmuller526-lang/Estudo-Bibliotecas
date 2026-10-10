#Crux Sacra Sit Mihi Lux

import pandas as pd

dados = {

    "categoria": ["Bebida", "Alimento", "Alimento"],
    "produtos": ["Coca-Cola", "Pão", "Salgadinho"],
    "precos": [12, 8, 10]

}

df = pd.DataFrame(dados)

print(df)

df["preço_final"] = df["precos"] + 2

print(df)

produtos_caros = df[df["preço_final"] > 11]

print(produtos_caros)

media_precos = df["preço_final"].mean()

print(media_precos)

media_categoria = df.groupby("categoria")["preço_final"].mean()

print(media_categoria)