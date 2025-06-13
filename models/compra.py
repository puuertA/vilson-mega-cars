from config import conectar

class Compra:
    @staticmethod
    def cadastrar(idplaca, idcliente, data, valor_pago, forma_pagamento):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""INSERT INTO compra (idplaca, idcliente, data, valor_pago, forma_pagamento) 
                           VALUES (%s, %s, %s, %s, %s)""", 
                         (idplaca, idcliente, data, valor_pago, forma_pagamento))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""SELECT c.*, v.modelo_veiculo, cl.nome 
                           FROM compra c
                           JOIN veiculo v ON c.idplaca = v.idplaca
                           JOIN cliente cl ON c.idcliente = cl.idcliente""")
            compras = cursor.fetchall()
        conexao.close()
        return compras