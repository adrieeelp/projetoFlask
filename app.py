from flask import Flask, render_template
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turmas_dao import TurmaDAO
from dao.cursos_dao import CursoDAO


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/dashboard/sobre')
def sobre():
    return render_template('/dashboard/sobre.html')

@app.route('/alunos')
def lista_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('alunos/lista.html', lista=lista)

@app.route('/professores')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professores/lista.html', lista=lista)

@app.route('/turmas')
def lista_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turmas/lista.html', lista=lista)

@app.route('/cursos')
def lista_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('cursos/lista.html', lista=lista)

@app.route('/dashboard/ajuda')
def ajuda():
    return render_template('/dashboard/ajuda.html')

@app.route('/dashboard/contato')
def contato():
    return render_template('/dashboard/contato.html')








if __name__ == '__main__':
    app.run(debug=True)
