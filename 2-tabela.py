import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('cadastro.db')

cursor = conexao.cursor()

# 2-Criação da Tabela
cursor.execute(
    """
        CREATE TABLE cadastro(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
          nome TEXT NOT NULL,
          idade INTEGER NOT NULL,
          cpf INTEGER NOT NULL,
          matricula INTEGER NOT NULL
        );
    """
)
# 3- Fecha conexão
conexao.close()
print("Tabela foi criada")