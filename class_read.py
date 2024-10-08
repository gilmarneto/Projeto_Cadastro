# data: 04/10/2024

from class_pessoa import Pessoa
from pymongo import MongoClient


class Read():
    def ler_dados(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['projeto_cadastro']
        colecao = db['pessoas']
        ler = colecao.find()
        print(ler)
        print("leitura dos dados realizada com sucesso.")
        return ler

