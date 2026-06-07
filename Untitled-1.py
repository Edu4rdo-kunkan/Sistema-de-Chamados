#Importações, Funções, Variáveis, Dados, etc.

import time
import os
import sqlite3

def limpar():
    os.system('cls')
    os.system('clear')

def carregando():
    limpar()
    print("\nCarregando...")
    time.sleep(1)
    limpar()

def retornar():
    limpar()
    print("\nRetornando ao menu principal...")
    time.sleep(1)
    limpar()

def caractere_errado():
    limpar()
    print("\nO Caractere digitado não é uma opção válida...")
    time.sleep(1)
    limpar()

#Introdução
print("""
     
    ███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗ 
    ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗
    ███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║
    ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║
    ███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║
    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝
      
                        ██████╗ ███████╗    
                        ██╔══██╗██╔════╝     
                        ██║  ██║█████╗       
                        ██║  ██║██╔══╝      
                        ██████╔╝███████╗    
                        ╚═════╝ ╚══════╝     
      
 ██████╗██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗  
██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ███████║███████║██╔████╔██║███████║██║  ██║██║   ██║███████╗
██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║╚════██║ 
╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝███████║ 
╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
       
                        < Sistema de Chamados >
""")

time.sleep(0.5)

print("""
Bem-vindo ao Sistema de Chamados! Este sistema foi desenvolvido para facilitar
a gestão e resolução de chamados em sua organização. Com ele, você pode criar,
acompanhar e resolver chamados de forma eficiente, garantindo que as solicitações
sejam atendidas de maneira rápida e organizada.
""")

time.sleep(0.5)

input("\n  Pressione Enter para continuar...")

#Menu Principal

carregando()
while True:
    print("""
         ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
         ████╗ ████║██╔════╝████╗  ██║██║   ██║
         ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
         ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
         ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
         ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                      
██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗██████╗  █████╗ ██╗     
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║██╔══██╗██╔══██╗██║     
██████╔╝██████╔╝██║██╔██╗ ██║██║     ██║██████╔╝███████║██║     
██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██║██╔═══╝ ██╔══██║██║     
██║     ██║  ██║██║██║ ╚████║╚██████╗██║██║     ██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝
                                                                
                    < Menu Principal >
""")
    
    time.sleep(0.5)

    print("""
[1] - Criar Chamado
[2] - Acompanhar Chamado
[3] - Resolver Chamado
[4] - Sair
""")
    
    menu_opcoes = input(" Selecione uma opção desejada: ")

    #Opção 1 - Criar Chamado
    if menu_opcoes == "1":
        carregando()
        while True:
            print("""
         ██████╗██████╗ ██╗ █████╗  ██████╗ █████╗  ██████╗ 
        ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗
        ██║     ██████╔╝██║███████║██║     ███████║██║   ██║
        ██║     ██╔══██╗██║██╔══██║██║     ██╔══██║██║   ██║
        ╚██████╗██║  ██║██║██║  ██║╚██████╗██║  ██║╚██████╔╝
         ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ 
                                                    
                        ██████╗ ███████╗
                        ██╔══██╗██╔════╝
                        ██║  ██║█████╗  
                        ██║  ██║██╔══╝  
                        ██████╔╝███████╗
                        ╚═════╝ ╚══════╝
                
 ██████╗██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗
██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ███████║███████║██╔████╔██║███████║██║  ██║██║   ██║███████╗
██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║╚════██║
╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝███████║
╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                    
                    <  Criação de Chamados  >

    """)
            
            time.sleep(0.5)

            #Questionário para criação de chamados
            print("<---------===========<( Dados do Usuário )>==========--------->\n")

            nome = input(" Digite o nome do solicitante: ")

            print("\n<---------===========<( Dados do Chamado )>==========--------->\n")

            titulo = input(" Digite o título do chamado: ")

            descricao = input(" Digite a descrição do chamado: ")

            while True:
                try:
                    prioridade = int(input(" Digite a prioridade do chamado (Baixo = 1, Média = 2, Alta = 3): "))
                    break
                except ValueError:
                                
                    print("""  ________________________ 
 |                        |
 | Digite apenas numeros! |
 |________________________|
""")
            #Dados do chamado registrado.
            registro_chamados = {
                "nome": nome,
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": prioridade
            }

            #Pergunta para adicionar outro chamado ou retornar ao menu principal.
            print("\n<-----------==============<( Opções )>=============----------->\n")

            time.sleep(1)
            print(" Chamado criado com sucesso!")
            time.sleep(0.7)
            add_outro = input(" Deseja Adicionar algum outro chamado? (s/n): ").lower()

            if add_outro == "s":
                limpar()
                print("\nRecomeçando...")
                time.sleep(0.8)
                limpar()
        
            elif add_outro == "n":
                retornar()
                break
            
            else:
                caractere_errado()


    #Opção 2 - Acompanhar Chamado
    elif menu_opcoes == "2":
        while True:
            carregando()
            print("""
 █████╗  ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ███╗   ██╗██╗  ██╗ █████╗ ██████╗ 
██╔══██╗██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗████╗  ██║██║  ██║██╔══██╗██╔══██╗
███████║██║     ██║   ██║██╔████╔██║██████╔╝███████║██╔██╗ ██║███████║███████║██████╔╝
██╔══██║██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██║╚██╗██║██╔══██║██╔══██║██╔══██╗
██║  ██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║ ╚████║██║  ██║██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
            
         ██████╗██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗
        ██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝
        ██║     ███████║███████║██╔████╔██║███████║██║  ██║██║   ██║███████╗
        ██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║╚════██║
        ╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝███████║
        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝

                            <  Acompanhamento de Chamados  >
    """)

            time.sleep(0.5)

            print("-"*86)
            print(24*" "+"LISTA DE TODOS OS CHAMADOS REGISTRADOS"+24*" ")
            print("-"*86+"\n")
            
            print(6*" "+"ID"+8*" "+"TÍTULO"+8*" "+"PRIORIDADE"+8*" "+"STATUS"+10*" "+"DATA DE ABERTURA")
            print(5*" "+4*"-"+6*" "+8*"-"+6*" "+12*"-"+6*" "+8*"-"+8*" "+18*"-"+"\n")      

            input("\n Pressione Enter para retornar ao menu principal...i")


    
    elif menu_opcoes == "3":
        print("")





    elif menu_opcoes == "4":
        limpar()
        print("\nSaindo do sistema...")
        time.sleep(3)
        break

    else:
        caractere_errado()