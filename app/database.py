import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", database="AIssit_db", user="root", password=""
        )
        if connection.is_connected():
            print(f"Conexão com o banco de dados estabelecida com sucesso.")
            return connection
    except Error as e:
        print(f"Error ao tentar criar conexão com o banco de dados: {e};")


def close_connection(connection):
    if connection.is_connected():
        connection.close()
