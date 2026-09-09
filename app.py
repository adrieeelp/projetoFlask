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
    cursor.execute("SELECT id, nome, idade, cidade FROM aluno")
    lista = cursor.fetchall()
    conn.close()
    return render_template('alunos/lista.html', lista=lista)

@app.route('/professores')
def lista_professor():
    DB_PATH = "banco_escola_pweb2.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, disciplina FROM professor")
    lista = cursor.fetchall()
    conn.close()
    return render_template('professores/lista.html', lista=lista)

@app.route('/turmas')
def lista_turma():
    DB_PATH = "banco_escola_pweb2.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""select turma.id,turma.semestre,curso.nome_curso,professor.nome,professor.disciplina from turma
                    join curso on curso.id=turma.curso_id
                    join professor on professor.id=turma.professor_id""")
    lista = cursor.fetchall()
    conn.close()
    return render_template('turmas/lista.html', lista=lista)

@app.route('/dashboard/ajuda')
def ajuda():
    return render_template('/dashboard/ajuda.html')

@app.route('/dashboard/contato')
def contato():
    return render_template('/dashboard/contato.html')








if __name__ == '__main__':
    app.run(debug=True)
