import sqlite3
# 1- Conectando no BANCO DE DADOS
conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()

# 2 - Leitura de Dados
dados = cursor.execute(
    "SELECT * FROM cadastro"
)
print(dados.fetchall())