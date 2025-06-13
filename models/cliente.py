from config import conectar

class Cliente:
    @staticmethod
    def cadastrar(nome, endereco, cidade, uf, cep):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO cliente (nome, endereco, cidade, uf, cep) VALUES (%s, %s, %s, %s, %s)", 
                         (nome, endereco, cidade, uf, cep))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
        conexao.close()
        return clientes

    @staticmethod
    def contar_total():
        """Conta o total de clientes cadastrados"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) as total FROM cliente")
            resultado = cursor.fetchone()
        conexao.close()
        return resultado['total'] if resultado else 0
