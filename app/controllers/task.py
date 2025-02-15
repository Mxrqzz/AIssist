from app.database import create_connection, close_connection


class Tarefa:
    def __init__(self, nome, descricao, prazo, prioridade, criador_id):
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.criador_id = criador_id

    def salvar_dados(self):
        conexao = create_connection()

        if conexao:
            cursor = conexao.cursor()
            sql = "INSERT INTO tarefas (nome, descricao, prazo, prioridade, criador_id) VALUES (%s, %s, %s, %s, %s)"
            values = (
                self.nome,
                self.descricao,
                self.prazo,
                self.prioridade,
                self.criador_id,
            )

            try:
                cursor.execute(sql, values)
                conexao.commit()
                print(f"tarefa: {self.nome}, cadastrada com sucesso")
            except Exception as e:
                print(f"Erro ao tentar salvar tarefa: {e}.")
            finally:
                cursor.close()
                close_connection(conexao)
                print("Conexão com o banco de dados encerrada.")

    @staticmethod
    def listar_tarefas(user_id):
        try:
            conexao = create_connection()
            if not conexao:
                raise Exception("Conexao com o banco de dados encerrada")

            cursor = conexao.cursor()
            sql = """
            SELECT *
            FROM tarefas
            WHERE criador_id = %s
            ORDER BY prazo ASC
            """

            cursor.execute(sql, (user_id,))
            tarefas = cursor.fetchall()
            return tarefas

        except Exception as e:
            print(f"Erro ao tentar listar tarefas: {e}")
            return []
        finally:
            close_connection(conexao)
