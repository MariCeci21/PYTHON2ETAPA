import requests
from flask import Flask, render_template, request

def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1} + {num2} = {resultado}'
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1} - {num2} = {resultado}'
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1} * {num2} = {resultado}'
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
            etapas = f'{num1} / {num2} = {resultado}'
        else:
            resultado = 'Erro: divisão po zero'
            etapas = 'Não é possivel dividir por zero.'
    else:
        resultado = 'Operação invalida'
        etapas = 'Aoperação selecionada é invalida.'
    
    return render_template('calculadoura.html', etapas=etapa, resultados=resultado)