# data: 25/10/2024

from bson import ObjectId
from pymongo import MongoClient

class Delete:
    def __init__(self, id):
        self.id = id

    def excluir_pessoa_selecionada(self):
        id_string = self.id
        id_objeto = ObjectId(id_string)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['projeto_cadastro']
        colecao = db['pessoas']
        excluir_pessoa = colecao.delete_one({'_id':id_objeto})

        print(excluir_pessoa.raw_result)

