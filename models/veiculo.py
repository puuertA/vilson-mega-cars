from config import conectar

class Veiculo:
    @staticmethod
    def cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""INSERT INTO veiculo (idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                         (idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM veiculo")
            veiculos = cursor.fetchall()
        conexao.close()
        return veiculos

    @staticmethod
    def buscar_por_id(idplaca):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM veiculo WHERE idplaca = %s", (idplaca,))
            veiculo = cursor.fetchone()
        conexao.close()
        return veiculo

    @staticmethod
    def atualizar_total_despesa(idplaca, total_despesa):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE veiculo SET total_despesa = %s WHERE idplaca = %s", (total_despesa, idplaca))
        conexao.commit()
        conexao.close()

    @staticmethod
    def contar_total():
        """Conta o total de veículos cadastrados"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) as total FROM veiculo")
            resultado = cursor.fetchone()
        conexao.close()
        return resultado['total'] if resultado else 0