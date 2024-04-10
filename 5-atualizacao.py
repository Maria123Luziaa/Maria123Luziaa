import sqlite3
# 1- Conectando no BD
conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()

# 2-Atualização
id = 4
cursor.execute(
    """
    UPDATE cadastro set nome = ?
    WHERE id = ?
    """,
    ("Daniel Carvalho", id)
    
)
conexao.commit()