# import os

from datetime import date
import sys


# transacoes = dict()

selected_option = -1
account_balance = 0
statement = ""


saldo = 0
limite = 500
LIMITE_SAQUES = 3
qtd_saques = 0
extrato = ""


#######################################################
#    MENU PRINCIPAL
#######################################################


def print_main_menu():
    print(
        """
------------------------------------------
                  MENU                  
------------------------------------------

    [0] - Depósito
    [1] - Saque
    [2] - Extrato
    [9] - Sair

------------------------------------------
------------------------------------------
        """
    )


#########################################################
#   MENU AUXILIAR
#########################################################


def aux_menu():
    while True:
        print(
            """\n------------------------------------------\n
    [0] - Voltar ao Menu Principal\n    [9] - Sair\n"""
        )

        selected_option = input("   Selecione a opção desejada: ")

        if selected_option == "9":
            exit_program()

        elif selected_option == "0":
            break

        else:
            print("\n   Opção inválida!")
            continue


#########################################################


#########################################################
#   REPETIR OPERACAO
#########################################################


def repeat_operation():
    while True:
        selected_option = input("    Deseja fazer outro depósito? [S/N] ")

        if selected_option.upper() == "N":
            return False

        elif selected_option.upper() == "S":
            print(" ")
            return True
        else:
            print("\n    Opção inválida!!!!\n")
            continue


#########################################################


#########################################################
#   0 - DEPÓSITO
#########################################################
def deposit_value():
    global account_balance, statement

    print(
        """
------------------------------------------
                DEPÓSITO                  
------------------------------------------"""
    )

    while True:
        value = input("    Valor do depósito: R$ ")

        NOW = date.today()
        account_balance += int(value)

        statement += f"  {NOW}     Depósito        R$ {value},00\n"

        print("    Depósito realizado com sucesso!\n")

        if not repeat_operation():
            aux_menu()
            break

        # selected_option = input("    Deseja fazer outro depósito? [S/N] ")

        # if selected_option.upper() == "N":
        #     aux_menu()
        #     break

        # elif selected_option.upper() == "S":
        #     print(" ")
        #     continue
        # else:
        #     print("\n   Opção inválida!")
        #     continue


#########################################################


#########################################################
#   1 - SAQUE
#########################################################


def take_value():
    global account_balance, statement

    print(
        """
------------------------------------------
                SAQUE                  
------------------------------------------\n"""
    )

    while True:
        value = int(input("    Valor do saque: R$ "))

        NOW = date.today()

        if account_balance >= value:
            account_balance -= value

            statement += f"  {NOW}     Saque         - R$ {value},00\n"

            print("\n    Saque realizado com sucesso!\n\n")

            if not repeat_operation():
                aux_menu()
                break


#########################################################


#########################################################
#   2 - EXTRATO
#########################################################
def print_statement():
    global statement, account_balance

    print(
        """
------------------------------------------
                  EXTRATO                  
------------------------------------------\n"""
    )

    print(statement)

    print(
        f"""
------------------------------------------
Saldo = R$ {account_balance},00
------------------------------------------"""
    )

    aux_menu()


#########################################################


#########################################################
#   9 - SAIR DO PROGRAMA
#########################################################
def exit_program():
    print(
        """
------------------------------------------
------------------------------------------
        Obrigado! Volte sempre!                  
------------------------------------------
------------------------------------------"""
    )
    sys.exit()


#########################################################


#########################################################
#   INÍCIO DA EXECUÇÃO
#########################################################

selected_option = -1
account_balance = 0
statement = ""

while True:
    print_main_menu()

    # print(opcao_selecionada)
    selected_option = input("   Selecione a opção desejada: ")

    if selected_option == "0":
        deposit_value()

    elif selected_option == "1":
        take_value()

    elif selected_option == "2":
        print_statement()

    elif selected_option == "9":
        exit_program()

    else:
        print("\n   Opção inválida!")
        selected_option = input("   Selecione a opção desejada: ")


#########################################################
#   FIM DA EXECUÇÃO
#########################################################
