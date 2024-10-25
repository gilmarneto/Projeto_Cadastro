# data: 17/10/2024

from bson import ObjectId
from pymongo import MongoClient
from class_pessoa import Pessoa

class Update(Pessoa):
    def __init__(self, nome, idade, profissao, id):
        super().__init__(nome, idade, profissao)
        self.id = id

    def atualizar_dados_selecionados(self):
        id_string = self.id
        id_objeto = ObjectId(id_string)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['projeto_cadastro']
        colecao = db['pessoas']
        editar = colecao.replace_one(
            {"_id":id_objeto},
            {
                "nome": self.nome,
                "idade": self.idade,
                "profissao": self.profissao
            }
        )
        if editar.modified_count == 1:
            print("dados alterados com sucesso.")
        else:
            print("nenhum dado alterado!")