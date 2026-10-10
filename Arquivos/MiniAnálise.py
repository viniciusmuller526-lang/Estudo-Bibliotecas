#Crux Sacra Sit Mihi lux

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/vinicius/Downloads/matriculas_escola.csv")

df["curso"] = df["curso"].str.upper().str.strip()

de_para = {

    "TECNICO EM ESTETICA": "TÉCNICO EM ESTÉTICA",
    "TECNICO EM CONTABILIDADE": "TÉCNICO EM CONTABILIDADE",
    "TECNICO EM LOGISTICA": "TÉCNICO EM LOGÍSTICA",
    "SEGURANCA DO TRABALHO": "TÉCNICO EM SEGURANÇA DO TRABALHO",
    "TECNICO EM INFORMATICA": "TÉCNICO EM INFORMÁTICA",
    "ENFERMAGEM": "TÉCNICO EM ENFERMAGEM",
    "TECNICO EM ENFERMAGEM": "TÉCNICO EM ENFERMAGEM",
    "TECNICO EM ADMINISTRACAO": "TÉCNICO EM ADMINISTRAÇÃO"

}

df["curso"] = df["curso"].replace(de_para)

matriculas_cursos = df["curso"].value_counts()

print(matriculas_cursos)

faturamento_por_curso = df.groupby("curso")["mensalidade"].sum()

print(faturamento_por_curso)

df["situacao"] = df["situacao"].str.upper().str.strip()

mudar = {

    "CONCLUIDO": "CONCLUÍDO"

}

df["situacao"] = df["situacao"].replace(mudar)
situacao = df["situacao"].value_counts()
print(situacao)

evadidos = df[df["situacao"] == "EVADIDO"]
evasao_curso = evadidos.value_counts("curso")

print(evasao_curso)

ativos = df[df["situacao"] == "CURSANDO"]
faturamento_ativos = ativos.value_counts("curso")
print(faturamento_ativos)

#df.to_csv("matriculas_tratadas.csv", index = False)

plt.figure()
evasao_curso.plot(kind="bar", color="tomato")
plt.title("Total de alunos evadidos por curso")
plt.xlabel("Curso")
plt.ylabel("Quantidade de evadidos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_alunos_por_curso.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 6))
faturamento_por_curso.plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribuição de faturamento histórico por curso")
plt.ylabel("")
plt.savefig('grafico_faturamento_historico.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 6))
faturamento_ativos.plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribuição de faturamento atual")
plt.ylabel("")
plt.savefig('grafico_faturamento_atual.png', bbox_inches='tight')
plt.show()