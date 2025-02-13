from app.database import create_connection, close_connection


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def salvar_dados(self):
        conexao = create_connection()

        if conexao:
            cursor = conexao.cursor()
            sql = "INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES (%s, %s, %s, %s)"
            values = (self.nome, self.sobrenome, self.email, self.senha)

            try:
                cursor.execute(sql, values)
                conexao.commit()
                print(f"Usuario: {self.nome}, cadastrado com sucesso.")
            except Exception as e:
                print(f"Erro ao tentar cadastrar usuario: {e}.")
            finally:
                cursor.close()
                close_connection(conexao)
                print("A Conexão com o banco de dados foi encerrada.")
