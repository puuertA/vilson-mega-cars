from models.venda import Venda

class VendaController:
    @staticmethod
    def cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento):
        return Venda.cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento)

    @staticmethod
    def listar():
        return Venda.listar()

    @staticmethod
    def buscar_por_id(idvenda):
        return Venda.buscar_por_id(idvenda)

    @staticmethod
    def listar_itens(idvenda):
        return Venda.listar_itens(idvenda)
