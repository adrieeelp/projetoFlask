from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/dashboard/sobre')
def sobre():
    return render_template('/dashboard/sobre.html')

@app.route('/alunos')
def lista_aluno():
    lista =[
        (1, "Ana Beatriz Silva", 20, "Teresina"),
        (2, "Carlos Eduardo Lima", 22, "Parnaiba"),
        (3, "Mariana Souza", 19, "Picos"),
        (4, "Rafael Oliveira", 23, "Floriano"),
        (5, "Juliana Costa", 21, "Campo Maior"),
        (6, "Pedro Henrique", 20, "Oeiras"),
        (7, "Fernanda Gomes", 18, "Piripiri"),
        (8, "Lucas Almeida", 22, "Altos"),
        (9, "Bianca Rocha", 24, "Esperantina"),
        (10, "Matheus Ribeiro", 19, "Barras"),
    ]
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
