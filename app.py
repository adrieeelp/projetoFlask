from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/dashboard/sobre')
def sobre():
    return render_template('/dashboard/sobre.html')

@app.route('/alunos')
def lista_aluno():
    DB_PATH = "banco_escola_pweb2.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, cidade FROM alunos")
    lista = cursor.fetchall()
    conn.close()
    return render_template('alunos/lista.html', lista=lista)

@app.route('/professores')
def lista_professor():
    lista =[
            (1, "Elienne Bacelar", "elienne.bacelar@escola.com", "ATIVIDADE DE EXTENSÃO IV"),
            (2, "Erica Araujo", "erica.araujo@escola.com", "ERER AFRO-DIASPÓRICA INDÍGENA"),
            (3, "Seandra Macedo", "seandra.macedo@escola.com", "ESTÁGIO SUPERVISIONADO II"),
            (4, "Barros Anderson", "barros.anderson@escola.com", "INSTRUMENTAÇÃO PARA O ENSINO MÉDIO"),
            (5, "Thiago Soares", "thiago.soares@escola.com", "INTERAÇÃO HUMANO COMPUTADOR"),
            (6, "Jefferson Silva", "jefferson.silva@escola.com", "PROGRAMAÇÃO WEB"),
            (7, "Francisca Ocilma", "francisca.ocilma@escola.com", "TRABALHO DE CONCLUSÃO DE CURSO I"),
            (8, "Leonia Dantas", "leonia.dantas@escola.com", "TRABALHO DE CONCLUSÃO DE CURSO I"),
        ]
    return render_template('professores/lista.html', lista=lista)

@app.route('/dashboard/ajuda')
def ajuda():
    return render_template('/dashboard/ajuda.html')

@app.route('/dashboard/contato')
def contato():
    return render_template('/dashboard/contato.html')








if __name__ == '__main__':
    app.run(debug=True)
