# data: 04/10/2024

from class_pessoa import Pessoa
from pymongo import MongoClient

class Create(Pessoa):
    def __init__(self, nome='', idade=0, profissao='') -> None:
        super().__init__(nome, idade, profissao)

    def cadastro(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['projeto_cadastro']
        colecao = db['pessoas']

        colecao.insert_one({"nome":self.nome, "idade":self.idade, "profissao":self.profissao})

        print("cadastro realizado com sucesso.")

