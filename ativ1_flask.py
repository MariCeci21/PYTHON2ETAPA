from flask import Flask

app = Flask(__name__)

@app.route('/')
def explicacao_decorater():
    return 'Olá Janaina! Decorators em Python são funções especiais que permitem modificar, estender ou envolver o comportamento de outras funções ou métodos de forma limpa e reutilizável, sem alterar seu código original. Um decorator em Python serve para modificar ou estender o comportamento de funções, métodos ou classes sem alterar o seu código original.'

if __name__ == '__main__':
    app.run(debug=True)