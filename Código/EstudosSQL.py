#Crux Sacra Sit Mihi Lux

import pandas as pd
import sqlite3

df = pd.read_csv("matriculas_tratadas.csv")
conexao = sqlite3.connect("escola.db")
df.to_sql("matriculas", conexao, if_exists="replace", index=False)
query = "SELECT curso, COUNT(curso) AS alunos_ativos, ROUND(AVG(mensalidade), 2) AS media_mensalidade, SUM(mensalidade) AS faturamento_total FROM matriculas WHERE situacao = 'CURSANDO' GROUP BY curso HAVING alunos_ativos > 15 ORDER BY faturamento_total DESC"
df_banco = pd.read_sql(query, conexao)
print(df_banco)
conexao.close()
