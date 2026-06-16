import sys

# Importação dos módulos do sistema que criaremos na sequência.
# O Python buscará esses arquivos no mesmo diretório.
import database
import modulo_auth
import modulo_produto
import modulo_estoque

def exibir_menu_principal(usuario_logado):
    """
    Exibe o menu principal do sistema e gerencia a navegação.
    Representa a Entrega 3.5 da avaliação.
    """
    # O laço 'while True' mantém o menu ativo até o usuário escolher sair ou fazer logout
    while True:
        print("\n" + "="*45)
        print("          SISTEMA DE GESTÃO - SAEP")
        print("="*45)
        
        # Exigência da prova: apresentar o nome do usuário logado na interface principal
        print(f"👤 Usuário logado: {usuario_logado['nome']}\n")
        
        print("1. Cadastro e Gestão de Produtos")
        print("2. Gestão de Estoque")
        print("3. Fazer Logout")
        print("4. Encerrar Sistema")
        print("-" * 45)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            # Delega o controle para o módulo de produtos (Entrega 3.6)
            modulo_produto.menu()
            
        elif opcao == '2':
            # Delega o controle para o módulo de estoque (Entrega 3.7)
            modulo_estoque.menu()
            
        elif opcao == '3':
            # A instrução 'break' quebra o laço atual e retorna para o laço de login
            print("\nRealizando logout...")
            break
            
        elif opcao == '4':
            # Encerra a execução do programa de forma limpa
            print("\nEncerrando o sistema. Até logo!")
            sys.exit(0)
            
        else:
            print("\n[Erro] Opção inválida. Digite um número de 1 a 4.")

def iniciar_sistema():
    """
    Ponto de entrada do sistema.
    Inicializa dependências e controla o loop de sessão do usuário.
    """
    print("Inicializando componentes do sistema...")
    
    # Chama a função que criamos anteriormente para garantir que o banco existe (Entrega 3.3)
    database.inicializar_banco()
    
    # Este laço mais externo garante que, após um logout, o sistema volte para a tela de login
    while True:
        print("\n--- TELA DE ACESSO ---")
        
        # Chama a função de login do módulo de autenticação (Entrega 3.4)
        # Espera-se que essa função retorne um dicionário com os dados do usuário, ou None
        usuario_logado = modulo_auth.login()
        
        if usuario_logado:
            # Se a autenticação for bem-sucedida, transfere para o menu principal
            exibir_menu_principal(usuario_logado)
        else:
            # Se a função retornar None (ex: usuário escolheu sair na tela de login), o sistema encerra
            print("\nSistema encerrado.")
            break

# Bloco condicional padrão do Python para garantir que o script só rode se executado diretamente
if __name__ == "__main__":
    iniciar_sistema()