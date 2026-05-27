from flask import Flask, render_template, request
from calculadoura import calcular

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        return calcular()
    return render_template('calculadoura.html', etapas = '', resultados = '')

if __name__ == "__main__":
    app.run(debug=True)
