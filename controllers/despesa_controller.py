from models.despesa import Despesa
from controllers.veiculo_controller import VeiculoController

class DespesaController:
    @staticmethod
    def cadastrar(idplaca, descricao, valor, idprestador, data_servico):
        Despesa.cadastrar(idplaca, descricao, valor, idprestador, data_servico)
        # Atualizar o total de despesas do veículo
        VeiculoController.atualizar_total_despesa(idplaca)

    @staticmethod
    def listar():
        return Despesa.listar()

    @staticmethod
    def listar_por_veiculo(idplaca):
        return Despesa.listar_por_veiculo(idplaca)
    
    @staticmethod
    def total_despesas_mes():
        """Retorna o valor total das despesas do mês atual"""
        from models.despesa import Despesa
        return Despesa.total_despesas_mes_atual()