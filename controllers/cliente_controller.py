from models.cliente import Cliente

class ClienteController:
    @staticmethod
    def cadastrar(nome, endereco, cidade, uf, cep):
        Cliente.cadastrar(nome, endereco, cidade, uf, cep)

    @staticmethod
    def listar():
        return Cliente.listar()
    
    @staticmethod
    def contar_clientes():
        """Conta o total de clientes cadastrados"""
        from models.cliente import Cliente
        return Cliente.contar_total()
