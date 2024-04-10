import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('cadastro.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO cadastro(nome, idade, cpf, matricula)
        VALUES ('Janna Hevillyn', 18, 46859685311, 202316),
        ('Maria Luzia', 19, 79465952395, 202400);
    """
)
conexao.commit()
conexao.close()