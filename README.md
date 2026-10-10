# Painel de Cursos 📊

Projeto desenvolvido como **Marco 1** para demonstrar a construção de uma pipeline de dados simples, integrando banco de dados relacional, API no backend e exibição dinâmica no frontend.

---

## 📌 Sobre o Projeto

A proposta principal foi pegar dados de matrículas armazenados no banco de dados, tratá-los no backend via consulta SQL (agrupando e contando os alunos ativos por curso) e disponibilizá-los em formato JSON através de uma API RESTful.

A interface consome essa API de forma assíncrona usando `fetch()` e manipula o DOM para exibir os cartões na tela sem precisar recarregar a página.

---

## 🛠️ Tecnologias

- **Backend:** Python 3 + Flask
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3 e JavaScript (Vanilla / Fetch API)

---

## ⚙️ Arquitetura e Fluxo de Dados

1. **Persistência (`escola.db`):** A consulta SQL filtra as matrículas ativas, agrupa por curso e ordena do maior para o menor total de alunos (`GROUP BY` e `ORDER BY`).
2. **API (`App.py`):**
   - Rota `/` -> Renderiza a tela principal (`index.html`).
   - Rota `/cursos` -> Executa a query no SQLite e retorna os dados em JSON.
3. **Frontend (`index.html`):** O botão aciona a função em JavaScript que faz o `fetch("/cursos")`, trata a resposta e cria os elementos `<li>` estilizados como cartões.

---
