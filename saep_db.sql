-- Criação da tabela de Usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    login TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);

-- Criação da tabela de Produtos (Contexto: Ferramentas Manuais)
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    estoque_minimo INTEGER NOT NULL
);

-- Criação da tabela de Estoque
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo_movimentacao TEXT CHECK(tipo_movimentacao IN ('E', 'S')) NOT NULL,
    quantidade INTEGER NOT NULL,
    data_movimentacao DATE NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

-- População da tabela de Usuários (Mínimo de 3 registros)
INSERT INTO usuarios (nome, login, senha) VALUES 
('Administrador', 'admin', '123456'),
('João Silva', 'joao.silva', 'senha123'),
('Maria Souza', 'maria.souza', 'senha123');

-- População da tabela de Produtos (Mínimo de 3 registros)
INSERT INTO produtos (nome, descricao, preco, estoque_minimo) VALUES 
('Martelo Unha', 'Martelo unha com cabo de madeira 25mm', 35.50, 10),
('Chave de Fenda', 'Chave de fenda simples 1/4 x 6', 12.90, 20),
('Alicate Universal', 'Alicate universal 8 polegadas isolado', 45.00, 15);

-- População da tabela de Estoque (Mínimo de 3 registros)
-- 'E' para Entrada, 'S' para Saída
INSERT INTO estoque (produto_id, tipo_movimentacao, quantidade, data_movimentacao) VALUES 
(1, 'E', 50, '2023-10-01'),
(2, 'E', 100, '2023-10-02'),
(3, 'E', 60, '2023-10-03');