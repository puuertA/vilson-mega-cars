from models.compra import Compra

class CompraController:
    @staticmethod
    def cadastrar(idplaca, idcliente, data, valor_pago, forma_pagamento):
        Compra.cadastrar(idplaca, idcliente, data, valor_pago, forma_pagamento)

    @staticmethod
    def listar():
        return Compra.listar()