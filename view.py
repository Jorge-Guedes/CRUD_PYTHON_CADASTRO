# importando SQLite
import sqlite3 as lite


# CRUD

# Creaty = Inserir / criar
# Ready = Acessar / mostrar
# Update = Atualizar
# Delete = Deletar

# criando conexao
connection = lite.connect('dados.db')

# Inserir informacoes
def inserir_info(i):
    with connection:
        cur = connection.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em_, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query)

# Acessar informacoes
def mostrar_info():
    lista = []

    with connection:
        cur = connection.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista



lista = ['joao', 1]
# Atualizar informacoes
def atualizar_info(i):
    with connection:
        cur = connection.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?,  dia_em_=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, lista)

'''
lista = [1]
# Deletar informacoes
with connection:
    cur = connection.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)
'''
