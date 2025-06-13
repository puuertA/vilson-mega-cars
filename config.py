import pymysql

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'ifsp'
MYSQL_DB = 'db_concessionaria'

def conectar():
    conexao = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

    with conexao.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")
        cursor.execute(f"USE {MYSQL_DB}")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                idcliente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                endereco VARCHAR(200),
                cidade VARCHAR(100),
                uf VARCHAR(2),
                cep VARCHAR(10)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestador (
                idprestador INT AUTO_INCREMENT PRIMARY KEY,
                nome_empresa VARCHAR(100),
                cidade VARCHAR(100),
                uf VARCHAR(2),
                cep VARCHAR(10),
                forma_pagamento VARCHAR(50)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS veiculo (
                idplaca VARCHAR(9) PRIMARY KEY,
                ano INT,
                modelo INT,
                preco_fipe DECIMAL(10,2),
                fabricante VARCHAR(50),
                modelo_veiculo VARCHAR(100),
                cor VARCHAR(20),
                preco_venda DECIMAL(10,2),
                total_despesa DECIMAL(10,2) DEFAULT 0
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS despesa (
                iddespesa INT AUTO_INCREMENT PRIMARY KEY,
                idplaca VARCHAR(9),
                descricao VARCHAR(200),
                valor DECIMAL(10,2),
                idprestador INT,
                data_servico DATE,
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idprestador) REFERENCES prestador(idprestador)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS compra (
                idcompra INT AUTO_INCREMENT PRIMARY KEY,
                idplaca VARCHAR(9),
                idcliente INT,
                data DATE,
                valor_pago DECIMAL(10,2),
                forma_pagamento VARCHAR(50),
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS venda (
                idvenda INT AUTO_INCREMENT PRIMARY KEY,
                data DATE,
                valor_vendido DECIMAL(10,2),
                idcliente INT,
                idplaca VARCHAR(9),
                forma_pagamento VARCHAR(50),
                FOREIGN KEY (idcliente) REFERENCES cliente(idcliente)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (idplaca) REFERENCES veiculo(idplaca)
                    ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)

    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )
