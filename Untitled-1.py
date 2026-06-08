#Importações, Funções, Variáveis, Dados, etc.

from datetime import datetime

import time
import os

def sep(nome):
            return '-' * (len(nome) + 2)

proximo_id = 1
chamados = {}

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

time.sleep(0.3)

print("""
Bem-vindo ao Sistema de Chamados! Este sistema foi desenvolvido para facilitar
a gestão e resolução de chamados em sua organização. Com ele, você pode criar,
acompanhar e resolver chamados de forma eficiente, garantindo que as solicitações
sejam atendidas de maneira rápida e organizada.
""")

time.sleep(0.3)

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
    
    time.sleep(0.3)

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
            
            time.sleep(0.3)

            #Questionário para criação de chamados
            print("<---------===========<( Dados do Usuário )>==========--------->\n")

            nome = input(" Digite o nome do solicitante: ")

            print("\n<---------===========<( Dados do Chamado )>==========--------->\n")

            titulo = input(" Digite o título do chamado (Poucas palavras): ")

            descricao = input(" Digite a descrição do chamado: ")

            while True:
                try:
                    niveis = {1: "Baixa", 2: "Média", 3: "Elevado"}
                    prioridade = int(input(" Digite a prioridade do chamado (Baixo = 1, Média = 2, Alta = 3): "))
                    
                    if prioridade not in niveis:
                        print("""  ________________________________
 |                                |
 | Digite apenas os números:      |
 | Baixo = 1, Média = 2, Alta = 3 |
 |________________________________|
""")
                    else:
                        break
                except ValueError:
                                
                    print("""  ________________________ 
 |                        |
 | Digite apenas numeros! |
 |________________________|
""")
            #Dados do chamado registrado.

            chamados[proximo_id] = {
                "id": proximo_id,
                "nome": nome,
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": niveis[prioridade],
                "status": "Aberto",
                "data_abertura": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            proximo_id += 1

            #Pergunta para adicionar outro chamado ou retornar ao menu principal.
            print("\n<-----------==============<( Opções )>=============----------->\n")

            time.sleep(0.4)
            print(" Chamado criado com sucesso!")
            time.sleep(0.3)
            add_outro = input(" Deseja Adicionar algum outro chamado? (s/n): ").lower()

            if add_outro == "s":
                limpar()
                print("\nRecomeçando...")
                time.sleep(0.5)
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

            time.sleep(0.3)

            #Listagem de todos os chamados registrados.
            print("-"*86)
            print(24*" "+"LISTA DE TODOS OS CHAMADOS REGISTRADOS"+24*" ")
            print("-"*86+"\n")

            print(f"{'ID':^11}{'TÍTULO':^15}{'PRIORIDADE':^19}{'STATUS':^15}{'DATA DE ABERTURA':^26}")
            print(f"{sep('ID'):^11}{sep('TÍTULO'):^15}{sep('PRIORIDADE'):^19}{sep('STATUS'):^15}{sep('DATA DE ABERTURA'):^26}")

            for chamado in chamados.values():
                id_formatacao = f"{chamado['id']:02}"
                print(
                    f"{id_formatacao:^11}{chamado['titulo'][:17]:^15}{chamado['prioridade']:^19}{chamado['status']:^15}{chamado['data_abertura']:^26}"
                )

            print("\n"+"-"*86+"\n")

            #Total de chamados registrados.
            if len(chamados) == 1:
                singular = "chamado"
            elif len(chamados) == 0:
                singular = "chamado"
            else:
                singular = "chamados"

            print(" Esse são TODOS os chamados registrados até o momento, há no total",len(chamados),singular+".")
            input(" Pressione Enter para retornar ao menu principal...")
            retornar()
            break

    
    elif menu_opcoes == "3":
        carregando()
        while True:
            print("""
 ██████╗ ███████╗███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
 ██████╔╝█████╗  ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
 ██╔══██╗██╔══╝  ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ██║  ██║███████╗███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
 ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                 
 ██████╗██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗ ███████╗
██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ███████║███████║██╔████╔██║███████║██║  ██║██║   ██║███████╗
██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║██║   ██║╚════██║
╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝╚██████╔╝███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                    
                    <  Resolução de Chamados  >
""")
            
            time.sleep(0.3)
            print(" Essa funcionalidade ainda está em desenvolvimento, aguarde por futuras atualizações...")
            input("\n Pressione Enter para retornar ao menu principal...")
            retornar()
            break


    elif menu_opcoes == "4":
        limpar()
        print("\nSaindo do sistema...")
        time.sleep(3)
        break

    else:
        caractere_errado()