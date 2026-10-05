from flask import Flask, render_template, request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turmas_dao import TurmaDAO
from dao.cursos_dao import CursoDAO
from urllib.parse import unquote

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

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    nome_limpo = unquote(nome)
    return render_template('saudacao/saudacao.html', valor_recebido=nome_limpo)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: '{senha}', Email: {email}"
    return render_template('/saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio1/<nome>')
def desafio1(nome):
    return render_template('desafio/desafio1.html', valor_recebido=nome)

@app.route('/login_desafio', methods=['POST'])
def login_desafio():
    nome = request.form['nome']
    nascimento = request.form['nascimento']
    cpf = request.form['cpf']
    mae = request.form['mae']
    return render_template('/desafio/dados.html', nome=nome, nascimento=nascimento, cpf=cpf, mae=mae)

@app.route('/dashboard/contato')
def contato():
    return render_template('/dashboard/contato.html')



if __name__ == '__main__':
    app.run(debug=True)
