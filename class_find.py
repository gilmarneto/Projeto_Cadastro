# data: 18/10/2024

from bson import ObjectId
from pymongo import MongoClient

class Find:
    def __init__(self, id=''):
        self.id = id
        
    def nome_pessoa(self):
        id_string = self.id
        id_objeto = ObjectId(id_string)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['projeto_cadastro']
        colecao = db['pessoas']
        find = colecao.find_one({'_id':id_objeto})
        return find
