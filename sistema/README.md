# Sistema de Gestão SAEP (Prova Prática)

Este projeto é uma aplicação de Interface de Linha de Comando (CLI) desenvolvida em Python e SQLite3 para atender aos requisitos da Avaliação Prática de Desempenho do SAEP. 

O sistema contempla o fluxo de autenticação de usuários, cadastro de produtos (com validações de dados) e registro de movimentações de estoque (com regras de negócio de alerta de estoque mínimo).

## ⚙️ Pré-requisitos

Para executar este sistema, o ambiente de avaliação precisa ter instalado:
* **Python 3.x** (Recomendado 3.8 ou superior)
* A biblioteca nativa do Python `sqlite3` já está inclusa na instalação padrão, não sendo necessária instalação adicional de Banco de Dados.

## 📦 Dependências

O sistema foi arquitetado para **não depender de bibliotecas externas**. Todas as bibliotecas utilizadas (`sqlite3`, `datetime`, `os`, `sys`) fazem parte da biblioteca padrão do Python. O arquivo `requirements.txt` encontra-se vazio por este motivo, garantindo que o sistema rode imediatamente em qualquer máquina com Python instalado, sem necessidade de conexão com a internet para baixar pacotes via `pip`.

## 🚀 Como Executar a Aplicação

1. Abra o terminal (ou prompt de comando) da máquina.
2. Navegue até o diretório `sistema/` (onde o arquivo `main.py` está localizado).
3. Execute o comando principal do sistema:
   ```bash
   python main.py