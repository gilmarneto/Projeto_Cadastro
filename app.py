# data inicial: 04/10/2024

from flask import Flask, render_template, request, redirect, url_for
from class_create import Create
from class_read import Read
from class_update import Update
from class_delete import Delete
from class_find import Find

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
    return render_template('form_cadastro.html', acao='cadastro', dados_pessoa_selecionada='')

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
    return redirect('/')

# PESSOA SELECIONADA
@app.route('/alterar_dados')
def pessoa_selecionada():
    id_pessoa_selecionada = request.args.get('id')
    pessoa = Find(id_pessoa_selecionada)
    return render_template('form_cadastro.html', acao='atualizar_dados', dados_pessoa_selecionada=pessoa.nome_pessoa())

# EDITAR DADOS DA PESSOA SELECIONADA
@app.route('/atualizar_dados', methods=['POST',])
def atualizar_dados():
    id = request.form['_id']
    nome = request.form['nome']
    idade = request.form['idade']
    profissao = request.form['profissao']
    atualizar = Update(nome, idade, profissao, id)
    atualizar.atualizar_dados_selecionados()
    return redirect('/')

# EXCLUIR PESSOA SELECIONADA
@app.route('/excluir_pessoa')
def excluir_pessoa():
    id_pessoa = request.args.get('id')
    deletar = Delete(id_pessoa)
    deletar.excluir_pessoa_selecionada()
    return redirect('/')

# RODAR APLICAÇÃO
app.run(debug=True)