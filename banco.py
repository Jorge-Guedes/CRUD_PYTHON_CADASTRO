# importando SQLite
import sqlite3 as lite

# criando conexao
connection = lite.connect('dados.db')

# criando tabela
with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em_ DATE, estado TEXT, assunto TEXT)")
