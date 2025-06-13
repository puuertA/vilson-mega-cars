from config import conectar

class Venda:
    @staticmethod
    def cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO venda (data, valor_vendido, idcliente, idplaca, forma_pagamento) VALUES (%s, %s, %s, %s, %s)",
                (data, valor_vendido, idcliente, idplaca, forma_pagamento)
            )
            idvenda = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return idvenda

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT v.idvenda, v.data, v.valor_vendido, v.forma_pagamento, 
                       c.nome AS cliente, ve.modelo_veiculo, ve.idplaca
                FROM venda v
                JOIN cliente c ON v.idcliente = c.idcliente
                LEFT JOIN veiculo ve ON v.idplaca = ve.idplaca
            """)
            vendas = cursor.fetchall()
        conexao.close()
        return vendas

    @staticmethod
    def buscar_por_id(idvenda):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT v.*, c.nome AS cliente, ve.modelo_veiculo, ve.fabricante, ve.cor
                FROM venda v
                JOIN cliente c ON v.idcliente = c.idcliente
                LEFT JOIN veiculo ve ON v.idplaca = ve.idplaca
                WHERE v.idvenda = %s
            """, (idvenda,))
            venda = cursor.fetchone()
        conexao.close()
        return venda

    @staticmethod
    def listar_itens(idvenda):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT iv.*, p.nome, v.data, v.forma_pagamento, c.nome AS cliente
                FROM itemvenda iv
                JOIN produto p ON iv.codproduto = p.codproduto
                JOIN venda v ON iv.codvenda = v.idvenda
                JOIN cliente c ON v.idcliente = c.idcliente
                WHERE iv.codvenda = %s
            """, (idvenda,))
            itens = cursor.fetchall()
        conexao.close()
        return itens

    @staticmethod
    def total_vendas_mes_atual():
        """Retorna o valor total das vendas do mês atual"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT COALESCE(SUM(valor_vendido), 0) as total 
                FROM venda 
                WHERE MONTH(data) = MONTH(CURDATE()) 
                AND YEAR(data) = YEAR(CURDATE())
            """)
            resultado = cursor.fetchone()
        conexao.close()
        return float(resultado['total']) if resultado else 0.0
