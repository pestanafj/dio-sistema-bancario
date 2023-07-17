# import os

from datetime import datetime
import sys, os


# transacoes = dict()

selected_option = -1
account_balance = 0
statement = ""
count_loot = 0

LOOT_LIMIT = 500
NUMBER_LOOT = 3


#######################################################
#    MENU PRINCIPAL
#######################################################


def print_main_menu():
    os.system("cls")

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


#########################################################
#   MENU AUXILIAR
#########################################################


def aux_menu():
    while True:
        print(
            """\n------------------------------------------\n
    [0] - Voltar ao Menu Principal\n    [9] - Sair\n
------------------------------------------\n"""
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


def repeat_operation(operation):
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


#########################################################


#########################################################
#   TESTE DE ENTRADA
#########################################################


def input_test(str_input):
    if len(str_input) >= 4:
        # print("tamanho maior ou igual a 4")
        if str_input[-3] == "." or str_input[-3] == ",":
            # print("tem ponto ou virgula de centavos")
            str_aux = str_input.replace(".", "").replace(",", "")

            if str_aux.isnumeric() and float(str_aux) > 0:
                # print("é número maior que 0")
                return float(str_aux) / 100

    return 0


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
        print("\n    - formato R$ 00.00")

        str_value = input("\n    Valor do depósito: R$ ")

        value = input_test(str_value)

        if value == 0:
            print("\n    O valor é inválido!")
            continue

        else:
            NOW = datetime.now()
            strNOW = NOW.strftime("%d/%m/%y %H:%M")

            account_balance += value

            statement += f"{strNOW}    Depósito     R$ {value:,.2f}\n"

            print("    Depósito realizado com sucesso!\n")

            if not repeat_operation("depósito"):
                aux_menu()
                break


#########################################################


#########################################################
#   1 - SAQUE
#########################################################


def take_value():
    global account_balance, statement, NUMBER_LOOT, count_loot, LOOT_LIMIT

    print(
        """
------------------------------------------
                SAQUE                  
------------------------------------------\n"""
    )

    while True:
        if count_loot >= NUMBER_LOOT:
            print("\n    Saque não permitido!\n")
            print(
                """    Você já atingiu sua quantidade
    de saques disponíveis!"""
            )
            aux_menu()
            break

        str_value = input("    Valor do saque: R$ ")

        value = input_test(str_value)

        if value == 0:
            print("\n    O valor é inválido!")
            continue

        else:
            #         if count_loot >= NUMBER_LOOT:
            #             print("\n    Saque não permitido!\n")
            #             print(
            #                 """    Você já atingiu sua quantidade
            # de saques disponíveis!"""
            #             )

            #             aux_menu()
            #             break

            if account_balance < value:
                print("\n    Saldo insuficiente!\n\n")
                aux_menu()
                break

            elif value > LOOT_LIMIT:
                print("\n    Saque não permitido!\n")
                print(f"    Seu limite de saque é R${LOOT_LIMIT},00!\n\n")

            else:
                NOW = datetime.today()
                strNOW = NOW.strftime("%d/%m/%y %H:%M")

                account_balance -= value
                count_loot += 1
                statement += f"{strNOW}    Saque      - R$ {value:,.2f}\n"

                print("\n    Saque realizado com sucesso!\n\n")

                if not repeat_operation("saque"):
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

    if statement == "":
        print("\n\n    Não foram realizadas movimentações\n\n")
    else:
        print(statement)

    print(
        f"""
------------------------------------------
Saldo = R$ {account_balance:,.2f}
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
------------------------------------------\n\n\n\n"""
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


#########################################################
#   FIM DA EXECUÇÃO
#########################################################
