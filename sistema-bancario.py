# import os

from datetime import datetime
import sys, os


def menu_principal(usuarios):
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


def menu_rodape():
    while True:
        print(
            """\n------------------------------------------\n
    [0] - Voltar ao Menu Principal\n    [9] - Sair\n
------------------------------------------\n"""
        )

        selected_option = input("   Selecione a opção desejada: ")

        if selected_option == "9":
            sair_do_programa()

        elif selected_option == "0":
            break

        else:
            print("\n   Opção inválida!")
            continue


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
    usuarios = list()

    nome = "Fernanda Pestana"
    data_de_nascimento = "15/10/1988"
    cpf = "01174820306"
    logradouro = "Rua 5 (Und 205)"
    numero_casa = "50"
    bairro = "Cidade Operária"
    cidade = "São Luís"
    estado = "MA"

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"

    novo_usuario = {
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

    usuarios.append(novo_usuario)
    usuarios[0]["contas"].append(nova_conta)

    menu_principal(usuarios)


main()
