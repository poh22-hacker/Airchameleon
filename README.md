# Airchameleon
O Airchameleon é uma ferramenta de cracking de senhas projetada para testar diferentes combinações de nomes de usuário e senhas para sistemas e serviços de autenticação. O objetivo principal da ferramenta é determinar se a senha de um serviço de rede pode ser quebrada por meio de um ataque automatizado. (uma versão melhorada do Watercat) 

                                                                                             
                                                                                                                           
                                                                                                                           
                                                                         █                                                 
                                                                       ██ ███                                              
                                                                       ██     ██                                           
                                                                        █       ███                                        
                                                                        ██         ██                                      
                                                                         █           ██                                    
                                                ███████      ██████      ██            ██                                  
                                    █       ████                   ████   █             ██                                 
                               ███       ███                          ██  ██           ████████                            
                                █      ██                              █  ██████████████  ███  ██                          
                                                                       ██  █         █       █  ██                         
                                                                        █  ██       ██   ██  █   ██                        
                                   █                                    ██ ██               ██    ██                       
                                                                         █  █         ██████       ██                      
                                 █                                       ██ ██               █████████                     
                                █                                  ████████   ███████████          ██                      
                               █                                 ███      █  ██                 ███                        
                              ██        █  █████              ███        ████              █████                           
                              █        ██      ██           ███      ████            ██████                                
                             █        ██         ██       ███      ██       ████████                                       
                                     ██   ███     ██        ███      ██████                                                
                                    ██  ██  ██     ██       ██████      ████                                               
                                   ██ ██     ██     ██████        ███        ██         ███    █                           
                                  ████        ██      ████           ████     ██                                           
                                 ███          ███        ██             ███    █                                           
                               ██████       █████████     █                ███ ██   █                                      
                             ███     ███  ███           ████                  ███                                          
                                        ███                                                                                
                            ██           █                                                                                 
                             ██          █                     █                                                           
                                        ██                 ████ ███                                                        
                              ██        ██               ██         ███                                                    
                               ██       ██               █    ███    ██                                                    
                                █        ██              █  ██   ██   █                                                    
                                ██        ██             █  ████  █   ██                                                   
                                 ██        ██             ██  ██  █   ██                                                   
                                  ██        ██               █    ██   █                                                   
                                   ██     ██████                  ██   █                                                   
                                    ██  ██      ████        ████      ██                                                   
                                      ██            ███████         ██                                                     
                                        ███                       ██                                                       
                                           ███                   ██                                                        
                                              █████         ████                                                           
                                                    ████                                                                   
                                                              


para que a ferramenta funcione corretamente, rode os seguintes comandos no terminal:

    pip install playwright
    python -m playwright install
ou 

    pip3 install playwright
    python3 -m playwright install  
Passos para instalar o Playwright no Termux:

Atualize o Termux e instale as dependências:

Execute os seguintes comandos para garantir que o Termux e todos os pacotes estejam atualizados:

    pkg update
    pkg upgrade

Agora, instale algumas dependências essenciais para o Playwright e seus navegadores:

    pkg install python
    pkg install clang
    pkg install libffi
    pkg install libssl-dev
    pkg install git
    pkg install wget
    pkg install libx11
    pkg install libxkbfile
    pkg install xz-utils
    pkg install libcurl
    pkg install libnss3
    pkg install libatk-bridge2.0-0
    pkg install libatk1.0-0
    pkg install libcups2
    pkg install libgdk-pixbuf2.0-0
    pkg install libgbm1
    pkg install libasound2

Esses pacotes são necessários para compilar e executar o Playwright e os navegadores.

Instalar o Python e o pip no Termux:

Se ainda não tiver o Python instalado, instale-o com:

    pkg install python

Depois, instale o pip (caso não tenha sido instalado automaticamente):

    python -m ensurepip --upgrade

Instalar o Playwright:

Agora, você pode instalar o Playwright usando o pip:

    pip install playwright

Após instalar o Playwright, você precisará instalar os navegadores (Chromium, Firefox ou WebKit). Para isso, execute o seguinte comando:

    python -m playwright install

Nota: A instalação do navegador pode demorar um pouco, dependendo da sua conexão e da configuração do sistema.
