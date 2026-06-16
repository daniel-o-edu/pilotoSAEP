import sqlite3
import os

DB_NAME = 'saep.db'
SQL_SCRIPT = '../saep_db.sql' # Caminho relativo apontando para a raiz do projeto

def conectar():
    """Estabelece e retorna a conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    # Permite acessar os resultados das consultas como dicionários
    conn.row_factory = sqlite3.Row 
    # Habilita o suporte a chaves estrangeiras no SQLite
    conn.execute("PRAGMA foreign_keys = 1") 
    return conn

def inicializar_banco():
    """Lê o script saep_db.sql e inicializa o banco de dados se não existir."""
    if not os.path.exists(DB_NAME):
        print("[Sistema] Criando e populando o banco de dados inicial...")
        try:
            with open(SQL_SCRIPT, 'r', encoding='utf-8') as arquivo_sql:
                script = arquivo_sql.read()
            
            conn = conectar()
            cursor = conn.cursor()
            cursor.executescript(script)
            conn.commit()
            conn.close()
            print("[Sistema] Banco de dados criado com sucesso!")
        except Exception as e:
            print(f"[Erro] Falha ao inicializar o banco de dados: {e}")
    else:
        print("[Sistema] Banco de dados já existe. Carregamento concluído.")

# Testa a inicialização ao executar este arquivo diretamente
if __name__ == '__main__':
    inicializar_banco()