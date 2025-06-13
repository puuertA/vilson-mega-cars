from config import conectar

class Prestador:
    def __init__(self, idprestador=None, nome_empresa=None, cidade=None, uf=None, cep=None, forma_pagamento=None):
        self.idprestador = idprestador
        self.nome_empresa = nome_empresa
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.forma_pagamento = forma_pagamento

    @staticmethod
    def listar_todos():
        """Lista todos os prestadores cadastrados"""
        conexao = conectar()
        prestadores = []
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM prestador ORDER BY nome_empresa")
            resultados = cursor.fetchall()
            for resultado in resultados:
                prestador = Prestador(
                    idprestador=resultado['idprestador'],
                    nome_empresa=resultado['nome_empresa'],
                    cidade=resultado['cidade'],
                    uf=resultado['uf'],
                    cep=resultado['cep'],
                    forma_pagamento=resultado['forma_pagamento']
                )
                prestadores.append(prestador)
        conexao.close()
        return prestadores

    @staticmethod
    def listar():
        """Alias para listar_todos() para compatibilidade"""
        return Prestador.listar_todos()

    @staticmethod
    def cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento):
        """Cadastra um novo prestador"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            sql = """INSERT INTO prestador (nome_empresa, cidade, uf, cep, forma_pagamento) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nome_empresa, cidade, uf, cep, forma_pagamento))
            conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def buscar_por_id(idprestador):
        """Busca um prestador pelo ID"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM prestador WHERE idprestador = %s", (idprestador,))
            resultado = cursor.fetchone()
        conexao.close()
        
        if resultado:
            return Prestador(
                idprestador=resultado['idprestador'],
                nome_empresa=resultado['nome_empresa'],
                cidade=resultado['cidade'],
                uf=resultado['uf'],
                cep=resultado['cep'],
                forma_pagamento=resultado['forma_pagamento']
            )
        return None

    @staticmethod
    def atualizar(idprestador, nome_empresa, cidade, uf, cep, forma_pagamento):
        """Atualiza os dados de um prestador"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            sql = """UPDATE prestador 
                     SET nome_empresa = %s, cidade = %s, uf = %s, cep = %s, forma_pagamento = %s
                     WHERE idprestador = %s"""
            cursor.execute(sql, (nome_empresa, cidade, uf, cep, forma_pagamento, idprestador))
            conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def excluir(idprestador):
        """Exclui um prestador"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("DELETE FROM prestador WHERE idprestador = %s", (idprestador,))
            conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def contar_total():
        """Conta o total de prestadores cadastrados"""
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) as total FROM prestador")
            resultado = cursor.fetchone()
        conexao.close()
        return resultado['total'] if resultado else 0