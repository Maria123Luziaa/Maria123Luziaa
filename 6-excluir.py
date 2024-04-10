import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()

# 2-Exclusão
id = (3,4)
cursor.execute(
    """
    DELETE FROM cadastro
    WHERE id in (?,?)
    """,
    id
)
conexao.commit()