# import os

from datetime import datetime
import sys, os


def menu_principal(clientes, contas):
    os.system("cls")

    print(
        """ 
--------------------------------------------
                PESTANA BANK
--------------------------------------------

[1] - Já sou cliente
[2] - Desejo ser cliente
[3] - Atendimento sem cadastro
[9] - Finalizar atendimento

--------------------------------------------
    """
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print("\n>>> Já sou cliente!\n")
        atendimento_cliente(clientes, contas)
    elif opcaoSelecionada == "2":
        print("\n>>> Desejo ser cliente!!\n")
        # cadastrar_cliente(clientes, contas)
    elif opcaoSelecionada == "3":
        atendimento_sem_cadastro(clientes, contas)
    elif opcaoSelecionada == "9":
        sair_do_programa()
    else:
        input("\n!!! Opção Inválida.\nPressione qualquer tecla para continuar...\n")
        menu_principal(clientes, contas)

    return clientes, contas


def menu_rodape(clientes, contas, menu_de_chamada, outra_operacao=False):
    str_operacao = ""
    if outra_operacao:
        str_operacao = "\n[#] - Fazer outra operação"

    print(
        f"""
\n------------------------------------------{str_operacao}
[0] - Voltar ao Início
[9] - Sair\n
------------------------------------------\n"""
    )

    opcao_selecionada = input("Selecione a opção desejada: ")

    if opcao_selecionada == "9":
        sair_do_programa()

    elif opcao_selecionada == "0":
        menu_principal(clientes, contas)

    elif opcao_selecionada == "#":
        menu_de_chamada(clientes, contas)

    # elif opcao_selecionada == "*":
    #     menu_anterior(clientes, contas)

    else:
        print("\n!!! Opção inválida!")
        menu_rodape(clientes, contas, menu_de_chamada, outra_operacao)

    return clientes, contas


def atendimento_cliente(clientes, contas, cpf_cliente=""):
    os.system("cls")

    print(
        """
--------------------------------------------
           PESTANA BANK - CLIENTE           
--------------------------------------------"""
    )

    # if cpf_cliente == "":
    cpf = input("Digite o CPF: ")

    for digito in cpf:
        if digito >= "0" and digito <= "9":
            cpf_cliente += digito

    if len(cpf_cliente) != 11:
        print("\n!!! Erro!\n!!! CPF inválido!\n")
        menu_rodape(clientes, contas, atendimento_cliente, True)

    index_cliente = buscar_cliente(clientes, "cpf", cpf_cliente)

    if index_cliente == -1:
        print("\n!!! Erro!\n!!! Não existe cliente cadastrado com esse CPF!\n")
        menu_rodape(clientes, contas, atendimento_cliente, True)

    cliente = clientes[index_cliente]
    nome_cliente = cliente["nome"]

    print(f"\n\n>>> Bem vindo {nome_cliente}!")

    print(
        """

[1] - Criar Conta
[2] - Listar Contas
[3] - Depósito
[4] - Saque
[5] - Extrato
[0] - Voltar ao Menu Anterior
[9] - Finalizar atendimento

--------------------------------------------
"""
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print("\n>>> Criar conta corrente!\n")

        # criar_conta_corrente(clientes, contas, cpf_cliente)
    elif opcaoSelecionada == "2":
        print("\n>>> Listar contas!\n")

        # listar_contas(contas, cpf_cliente)
    elif opcaoSelecionada == "3":
        print("\n>>> Depositar!\n")
        depositar(clientes, contas, cpf_cliente=cpf_cliente)
    elif opcaoSelecionada == "4":
        print("\n>>> Saque\n")
    elif opcaoSelecionada == "5":
        print("\n>>> Imprimir extrato\n")
        # imprimir_extrato(clientes, contas)
    elif opcaoSelecionada == "0":
        menu_principal(clientes, contas)
    elif opcaoSelecionada == "9":
        sair_do_programa()
    else:
        input("\n!!! Opção Inválida.\nPressione qualquer tecla para continuar...\n")
        atendimento_cliente(clientes, contas)

    menu_rodape(clientes, contas, atendimento_cliente, True)

    return clientes, contas


def atendimento_sem_cadastro(clientes, contas):
    os.system("cls")

    print(
        """
--------------------------------------------
  PESTANA BANK - ATENDIMENTO SEM CADASTRO           
--------------------------------------------

[1] - Listar Clientes
[2] - Listar Contas
[3] - Depósito
[4] - Extrato
[0] - Voltar ao Menu Principal
[9] - Finalizar o Atendimento

--------------------------------------------
"""
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print("\n>>> Listar clientes!")
        # listar_clientes(clientes)
        menu_rodape(clientes, contas, atendimento_sem_cadastro, True)
    elif opcaoSelecionada == "2":
        print("\n>>> Listar Contas")
        # listar_contas(contas)
        menu_rodape(clientes, contas, atendimento_sem_cadastro, True)
    elif opcaoSelecionada == "3":
        print("\n>>> Depositar!\n")

        # depositar(clientes, contas, "")
    elif opcaoSelecionada == "4":
        print("\n>>> Imprimir extrato\n")
        # imprimir_extrato(clientes, contas)
    elif opcaoSelecionada == "0":
        menu_principal(clientes, contas)
    elif opcaoSelecionada == "9":
        sair_do_programa()
    else:
        input("\n!!! Opção Inválida.\nPressione qualquer tecla para continuar...\n")
        atendimento_sem_cadastro(clientes, contas)

    menu_rodape(clientes, contas, atendimento_sem_cadastro, True)


def repetir_operacao(operation):
    while True:
        selected_option = input(f"    Deseja fazer outro {operation}? [S/N] ")

        if selected_option.upper() == "N":
            return False

        elif selected_option.upper() == "S":
            print(" ")
            return True
        else:
            print("\n    Opção inválida!!!!\n")
            continue


def testar_entrada(str_input):
    if len(str_input) >= 4:
        # print("tamanho maior ou igual a 4")
        if str_input[-3] == "." or str_input[-3] == ",":
            # print("tem ponto ou virgula de centavos")
            str_aux = str_input.replace(".", "").replace(",", "")

            if str_aux.isnumeric() and float(str_aux) > 0:
                # print("é número maior que 0")
                return float(str_aux) / 100

    return 0


def depositar():
    global saldo, extrato

    print(
        """
------------------------------------------
                DEPÓSITO                  
------------------------------------------"""
    )

    while True:
        print("\n    - formato R$ 00.00")

        str_valor = input("\n    Valor do depósito: R$ ")

        valor = testar_entrada(str_valor)

        if valor == 0:
            print("\n    O valor é inválido!")
            continue

        else:
            NOW = datetime.now()
            strNOW = NOW.strftime("%d/%m/%y %H:%M")

            saldo += valor

            extrato += f"{strNOW}    Depósito     R$ {valor:,.2f}\n"

            print("    Depósito realizado com sucesso!\n")

            if not repetir_operacao("depósito"):
                menu_rodape()
                break


def sacar():
    global saldo, extrato, QTD_SAQUES, cont_saques, LIMITE_SAQUE

    print(
        """
------------------------------------------
                SAQUE                  
------------------------------------------\n"""
    )

    while True:
        if cont_saques >= QTD_SAQUES:
            print("\n    Saque não permitido!\n")
            print(
                """    Você já atingiu sua quantidade
    de saques disponíveis!"""
            )
            menu_rodape()
            break

        str_valor = input("    Valor do saque: R$ ")

        valor = testar_entrada(str_valor)

        if valor == 0:
            print("\n    O valor é inválido!")
            continue

        else:
            #         if cont_saques >= QTD_SAQUES:
            #             print("\n    Saque não permitido!\n")
            #             print(
            #                 """    Você já atingiu sua quantidade
            # de saques disponíveis!"""
            #             )

            #             menu_rodape()
            #             break

            if saldo < valor:
                print("\n    Saldo insuficiente!\n\n")
                menu_rodape()
                break

            elif valor > LIMITE_SAQUE:
                print("\n    Saque não permitido!\n")
                print(f"    Seu limite de saque é R${LIMITE_SAQUE},00!\n\n")

            else:
                NOW = datetime.today()
                strNOW = NOW.strftime("%d/%m/%y %H:%M")

                saldo -= valor
                cont_saques += 1
                extrato += f"{strNOW}    Saque      - R$ {valor:,.2f}\n"

                print("\n    Saque realizado com sucesso!\n\n")

                if not repetir_operacao("saque"):
                    menu_rodape()
                    break


def inprimir_extrato():
    global extrato, saldo

    print(
        """
------------------------------------------
                  EXTRATO                  
------------------------------------------\n"""
    )

    if extrato == "":
        print("\n\n    Não foram realizadas movimentações\n\n")
    else:
        print(extrato)

    print(
        f"""
------------------------------------------
Saldo = R$ {saldo:,.2f}
------------------------------------------"""
    )

    menu_rodape()


def sair_do_programa():
    print(
        """
--------------------------------------------
          Obrigado! Volte sempre!                  
--------------------------------------------\n\n\n\n"""
    )
    sys.exit()


def main():
    clientes = list()
    contas = list()

    nome = "Fernanda Pestana"
    data_de_nascimento = "15/10/1988"
    cpf = "01174820306"
    logradouro = "Rua 5 (Und 205)"
    numero_casa = "50"
    bairro = "Cidade Operária"
    cidade = "São Luís"
    estado = "MA"

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"

    novo_cliente = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "contas": [],
    }

    nova_conta = {
        "agencia": "0001",
        "numero_conta": 1,
        "cpf_dono": "01174820306",
        "LIMITE_SAQUE": 500.00,
        "SAQUES_DISPONIVEIS": 3,
        "cont_saques": 0,
        "saldo": 0.0,
        "extrato": "",
    }

    nova_conta["saldo"] = 100

    clientes.append(novo_cliente)
    clientes[0]["contas"].append(nova_conta)
    contas.append(nova_conta)

    menu_principal(clientes, contas)


main()
