from config import conectar

class Despesa:
    @staticmethod
    def cadastrar(idplaca, descricao, valor, idprestador, data_servico):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""INSERT INTO despesa (idplaca, descricao, valor, idprestador, data_servico) 
                           VALUES (%s, %s, %s, %s, %s)""", 
                         (idplaca, descricao, valor, idprestador, data_servico))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT d.*, v.modelo_veiculo, p.nome_empresa 
                           FROM despesa d
                           JOIN veiculo v ON d.idplaca = v.idplaca
                           JOIN prestador p ON d.idprestador = p.idprestador""")
            despesas = cursor.fetchall()
        conexao.close()
        return despesas

    @staticmethod
    def listar_por_veiculo(idplaca):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT d.*, p.nome_empresa 
                           FROM despesa d
                           JOIN prestador p ON d.idprestador = p.idprestador
                           WHERE d.idplaca = %s""", (idplaca,))
            despesas = cursor.fetchall()
        conexao.close()
        return despesas

    @staticmethod
    def calcular_total_por_veiculo(idplaca):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT SUM(valor) as total FROM despesa WHERE idplaca = %s", (idplaca,))
            resultado = cursor.fetchone()
        conexao.close()
        return resultado['total'] if resultado['total'] else 0

    @staticmethod
    def total_despesas_mes_atual():
        """Retorna o valor total das despesas do mês atual"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT COALESCE(SUM(valor), 0) as total 
                FROM despesa 
                WHERE MONTH(data_servico) = MONTH(CURDATE()) 
                AND YEAR(data_servico) = YEAR(CURDATE())
            """)
            resultado = cursor.fetchone()
        conexao.close()
        return float(resultado['total']) if resultado else 0.0