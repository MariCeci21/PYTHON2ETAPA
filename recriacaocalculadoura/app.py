from flask import Flask, render_template
from calculadoura import calcular

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('calculadoura.html', etapas = '', resultados = '')

@app.route('/calcular', methods = ['POST'])
def calcular_route():
    return calcular()

if __name__ == "__main__":
    app.run(debug=True)