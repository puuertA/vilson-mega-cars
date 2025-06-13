from models.prestador import Prestador

class PrestadorController:
    @staticmethod
    def cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento):
        Prestador.cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento)

    @staticmethod
    def listar():
        return Prestador.listar()