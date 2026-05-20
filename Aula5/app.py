from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <h1>Atividade Jinja - Escolha um Exercício:</h1>
    <ul>
        <li><a href="/exercicio1">Exercício 1 (Olá, Nome)</a></li>
        <li><a href="/exercicio2">Exercício 2 (Nome e Idade)</a></li>
        <li><a href="/exercicio3">Exercício 3 (Dicionário Usuário)</a></li>
        <li><a href="/exercicio4">Exercício 4 (Lista de Alunos)</a></li>
        <li><a href="/exercicio5?nota=8">Exercício 5 (Condicional - Aprovado)</a></li>
        <li><a href="/exercicio5?nota=5">Exercício 5 (Condicional - Reprovado)</a></li>
    </ul>
    """


@app.route('/exercicio1')
def exercicio_1():
    return render_template('exercicio1.html', nome="Carlos")


@app.route('/exercicio2')
def exercicio_2():
    return render_template('exercicio2.html', nome="Bruno", idade=25)


@app.route('/exercicio3')
def exercicio_3():
    usuario_dados = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('exercicio3.html', usuario=usuario_dados)


@app.route('/exercicio4')
def exercicio_4():
    lista_alunos = ["Marcos", "Amanda", "Rafael", "Beatriz"]
    return render_template('exercicio4.html', alunos=lista_alunos)


from flask import request
@app.route('/exercicio5')
def exercicio_5():
    
    nota_aluno = float(request.args.get('nota', 0))
    return render_template('exercicio5.html', nota=nota_aluno)

if __name__ == '__main__':
    app.run(debug=True)