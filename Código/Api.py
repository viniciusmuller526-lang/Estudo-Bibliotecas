#Crux Sacra Sit Mihi Lux

from flask import Flask, jsonify, render_template
import sqlite3

api = Flask(__name__) 

@api.route("/")

def home():

    return render_template("index.html")

@api.route("/cursos")

def listar_cursos():

    conectar = sqlite3.connect("escola.db")

    conectar.row_factory = sqlite3.Row

    cursor = conectar.cursor()

    cursor.execute("SELECT curso, COUNT(curso) AS alunos_ativos FROM matriculas WHERE situacao = 'CURSANDO' GROUP BY curso ORDER BY alunos_ativos DESC")

    dados = [dict(linha) for linha in cursor.fetchall()]

    conectar.close()

    return jsonify(dados)

if __name__ == "__main__":

    api.run(debug = True)
