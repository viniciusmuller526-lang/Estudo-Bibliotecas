# Mini-Projeto Fullstack 📊

Projeto desenvolvido como **Marco 1** para demonstrar a construção de uma pipeline de dados simples, integrando tratamento de dados, banco de dados relacional, API no backend e exibição no frontend.

---

## 📌 Sobre o Projeto

A proposta principal foi começar tratando uma fonte de dados inconsistente, armazenar os dados de matrículas em um banco de dados, tratá-los no backend via consulta SQL (agrupando e contando os alunos ativos por curso) e disponibilizá-los em formato JSON através de uma API RESTful.

A interface consome essa API usando `fetch()` e manipula o DOM para exibir os cartões na tela sem precisar recarregar a página.

---

## 🛠️ Tecnologias

- **Backend:** Python 3 + Flask + Pandas + Mathplotlib
- **Banco de Dados:** SQLite3
- **Frontend:** HTML5, CSS3 e JavaScript

---

## ⚙️ Arquitetura e Fluxo de Dados

1. **Tratamento(`Pandas + Mathplotlib`):** Um arquivo .csv é tratado utilizando Pandas, então o código utiliza o mathplotlib para gerar gráficos baseados nos dados tratados, e então salva esses dados um arquivo escola.db.
2. **Persistência (`escola.db`):** A consulta SQL filtra as matrículas ativas, agrupa por curso e ordena do maior para o menor total de alunos (`GROUP BY` e `ORDER BY`).
3. **API (`App.py`):**
   - Rota `/` -> Renderiza a tela principal (`index.html`).
   - Rota `/cursos` -> Executa a query no SQLite e retorna os dados em JSON.
4. **Frontend (`index.html`):** O botão aciona a função em JavaScript que faz o `fetch("/cursos")`, trata a resposta e cria os elementos `<li>` estilizados como cartões.

---
