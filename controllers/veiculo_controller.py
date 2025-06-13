from models.veiculo import Veiculo
from models.despesa import Despesa

class VeiculoController:
    @staticmethod
    def cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa=0):
        Veiculo.cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa)

    @staticmethod
    def listar():
        return Veiculo.listar()

    @staticmethod
    def buscar_por_id(idplaca):
        return Veiculo.buscar_por_id(idplaca)

    @staticmethod
    def atualizar_total_despesa(idplaca):
        total = Despesa.calcular_total_por_veiculo(idplaca)
        Veiculo.atualizar_total_despesa(idplaca, total)

    @staticmethod
    def contar_veiculos():
        """Conta o total de veículos no estoque"""
        from models.veiculo import Veiculo
        return Veiculo.contar_total()