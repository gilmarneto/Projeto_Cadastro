# data inicial: 04/10/2024

from flask import Flask, render_template, redirect, url_for
import os

#os.system('cls')

app = Flask(__name__)

# INDEX
@app.route('/')
def index():
    return render_template('index.html', titulo="Projeto Cadastro")
# CADASTRO
@app.route('/cadastro')
def cadastro():
    return render_template('form_cadastro.html')

# RODAR APLICAÇÃO
app.run(debug=True)