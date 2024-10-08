# data inicial: 04/10/2024

from flask import Flask, render_template, request, redirect, url_for
from class_create import Create
from class_read import Read

app = Flask(__name__)

# INDEX
@app.route('/')
def index():
    ler = Read()
    ler.ler_dados()
    return render_template('index.html', titulo="Projeto Cadastro", pessoas=ler.ler_dados())

# TELA DE CADASTRO
@app.route('/tela_cadastro')
def tela_cadastro():
    return render_template('form_cadastro.html')

# CADASTRAR PESSOA
@app.route('/cadastro', methods=['POST',])
def cadastro():
    nome = request.form['nome']
    idade = request.form['idade']
    profissao = request.form['profissao']
    cadastrar = Create(nome, idade, profissao)
    cadastrar.cadastro()
    return redirect('/')

# EXIBIR PESSOAS CADASTRADAS
@app.route('/exibir_pessoas')
def exibir_pessoas():
    pass
    return redirect('/')

# RODAR APLICAÇÃO
app.run(debug=True)