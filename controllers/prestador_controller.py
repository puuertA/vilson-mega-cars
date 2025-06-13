from models.prestador import Prestador

class PrestadorController:
    @staticmethod
    def listar():
        """Lista todos os prestadores"""
        return Prestador.listar_todos()

    @staticmethod
    def cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento):
        """Cadastra um novo prestador"""
        return Prestador.cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento)

    @staticmethod
    def buscar(idprestador):
        """Busca um prestador pelo ID"""
        return Prestador.buscar_por_id(idprestador)

    @staticmethod
    def atualizar(idprestador, nome_empresa, cidade, uf, cep, forma_pagamento):
        """Atualiza um prestador"""
        return Prestador.atualizar(idprestador, nome_empresa, cidade, uf, cep, forma_pagamento)

    @staticmethod
    def excluir(idprestador):
        """Exclui um prestador"""
        return Prestador.excluir(idprestador)

    @staticmethod
    def contar():
        """Conta o total de prestadores"""
        return Prestador.contar_total()