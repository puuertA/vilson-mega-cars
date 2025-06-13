from config import conectar

class Prestador:
    @staticmethod
    def cadastrar(nome_empresa, cidade, uf, cep):
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("""INSERT INTO prestador (nome_empresa, cidade, uf, cep) 
                           VALUES (%s, %s, %s, %s)""", 
                         (nome_empresa, cidade, uf, cep))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM prestador")
            prestadores = cursor.fetchall()
        conexao.close()
        return prestadores