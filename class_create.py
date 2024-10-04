# data: 04/10/2024

from class_pessoa import Pessoa

class Create(Pessoa):
    def __init__(self, nome='', idade=0, profissao='') -> None:
        super().__init__(nome, idade, profissao)
