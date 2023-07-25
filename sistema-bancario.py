# import os

from datetime import datetime
import sys, os


def menu_principal(clientes, contas, fluxo, index_cliente):
    fluxo.clear()
    fluxo.append(menu_principal)
    # print(fluxo)
    # input("enter")
    os.system("cls")

    print(
        """ 
--------------------------------------------
                PESTANA BANK
--------------------------------------------

[1]  Já sou cliente
[2]  Desejo ser cliente
[3]  Atendimento sem cadastro
[9]  Finalizar atendimento

--------------------------------------------
    """
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print(
            """
--------------------------------------------
>>> Já sou Cliente
--------------------------------------------"""
        )

        cpf = input("Digite o CPF: ")
        cpf_cliente = ""

        for digito in cpf:
            if digito >= "0" and digito <= "9":
                cpf_cliente += digito

        if len(cpf_cliente) != 11:
            print("\n!!! Erro!\n!!! CPF inválido!\n")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        index_cliente = buscar_cliente(clientes, "cpf", cpf_cliente)

        if index_cliente == -1:
            print("\n!!! Erro!\n!!! Não existe cliente cadastrado com esse CPF!\n")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        atendimento_cliente(clientes, contas, fluxo, index_cliente)

    elif opcaoSelecionada == "2":
        print("\n>>> Desejo ser cliente!!\n")

        cadastrar_cliente(clientes, contas, fluxo, -1)

    elif opcaoSelecionada == "3":
        atendimento_sem_cadastro(clientes, contas, fluxo, -1)

    elif opcaoSelecionada == "9":
        sair_do_programa()

    else:
        input("\n!!! Opção Inválida.\nPressione enter para continuar...\n")
        menu_principal(clientes, contas, fluxo, -1)

    return clientes, contas, fluxo


def menu_rodape(clientes, contas, fluxo, index_cliente=-1):
    str_menu_anterior = ""
    if len(fluxo) > 1:
        str_menu_anterior = "\n[-]  Menu anterior\n"

    print(
        f"""
\n------------------------------------------
[+]  Fazer outra operação{str_menu_anterior}
[0]  Voltar ao Início
[9]  Sair\n
------------------------------------------\n"""
    )

    opcao_selecionada = input("Selecione a opção desejada: ")

    if opcao_selecionada == "9":
        sair_do_programa()

    elif opcao_selecionada == "0":
        menu_principal(clientes, contas, fluxo, -1)

    elif opcao_selecionada == "+":
        menu_de_chamada = fluxo.pop()
        if menu_de_chamada == sacar_cliente:
            menu_de_chamada(
                clientes=clientes,
                contas=contas,
                fluxo=fluxo,
                index_cliente=index_cliente,
            )
        else:
            menu_de_chamada(clientes, contas, fluxo, index_cliente=index_cliente)

    elif len(fluxo) > 1 and opcao_selecionada == "-":
        fluxo.pop()
        menu_de_chamada = fluxo.pop()
        if menu_de_chamada == sacar_cliente:
            menu_de_chamada(
                clientes=clientes,
                contas=contas,
                fluxo=fluxo,
                index_cliente=index_cliente,
            )
        else:
            menu_de_chamada(clientes, contas, fluxo, index_cliente=index_cliente)

    else:
        print("\n!!! Opção inválida!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    return clientes, contas, fluxo


def atendimento_cliente(clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(atendimento_cliente)
    # print(fluxo)
    # input("enter")
    os.system("cls")

    print(
        """
--------------------------------------------
           PESTANA BANK - CLIENTE           
--------------------------------------------"""
    )

    cliente = clientes[index_cliente]

    print(f"\n\n>>> Bem vindo {cliente['nome']}!")

    print(
        """

[1]  Criar Conta
[2]  Listar Contas
[3]  Depósito
[4]  Saque
[5]  Extrato
[0]  Voltar ao Menu Principal
[9]  Finalizar atendimento

--------------------------------------------
"""
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print("\n>>> Criar conta corrente!\n")
        criar_conta_corrente(clientes, contas, fluxo, index_cliente)

    elif opcaoSelecionada == "2":
        print("\n>>> Listar contas!\n")
        listar_contas(clientes, contas, fluxo, index_cliente)

    elif opcaoSelecionada == "3":
        # print("\n>>> Depositar!\n")
        depositar_cliente(clientes, contas, fluxo, index_cliente=index_cliente)

    elif opcaoSelecionada == "4":
        # print("\n>>> Saque\n")
        sacar_cliente(
            clientes=clientes, contas=contas, fluxo=fluxo, index_cliente=index_cliente
        )

    elif opcaoSelecionada == "5":
        # print("\n>>> Imprimir extrato\n")
        imprimir_extrato_cliente(clientes, contas, fluxo, index_cliente)

    elif opcaoSelecionada == "0":
        menu_principal(clientes, contas, fluxo, -1)

    elif opcaoSelecionada == "9":
        sair_do_programa()

    else:
        input("\n!!! Opção Inválida.\nPressione enter para continuar...\n")
        atendimento_cliente(clientes, contas, fluxo, index_cliente=index_cliente)

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def atendimento_sem_cadastro(clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(atendimento_sem_cadastro)
    os.system("cls")

    print(
        """
--------------------------------------------
  PESTANA BANK - ATENDIMENTO SEM CADASTRO           
--------------------------------------------

[1]  Listar Clientes
[2]  Listar Contas
[3]  Depósito
[5]  Extrato
[0]  Voltar ao Menu Principal
[9]  Finalizar o Atendimento

--------------------------------------------
"""
    )

    opcaoSelecionada = input("Selecione a opção desejada: ")

    if opcaoSelecionada == "1":
        print("\n>>> Listar clientes!")
        listar_clientes(clientes, contas, fluxo, -1)
        menu_rodape(clientes, contas, fluxo, -1)
    elif opcaoSelecionada == "2":
        print("\n>>> Listar Contas")
        listar_contas(clientes, contas, fluxo, -1)
        menu_rodape(clientes, contas, fluxo, -1)
    elif opcaoSelecionada == "3":
        print("\n>>> Depositar!\n")
        depositar(clientes, contas, fluxo, index_cliente=-1)
    elif opcaoSelecionada == "5":
        print("\n>>> Imprimir extrato\n")
        imprimir_extrato(clientes, contas, fluxo, -1)
    elif opcaoSelecionada == "0":
        menu_principal(clientes, contas, fluxo, -1)
    elif opcaoSelecionada == "9":
        sair_do_programa()
    else:
        input("\n!!! Opção Inválida.\nPressione enter para continuar...\n")
        atendimento_sem_cadastro(clientes, contas, fluxo, -1)

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def cadastrar_cliente(clientes, contas, fluxo, index_cliente):
    fluxo.append(cadastrar_cliente)
    print(
        """
--------------------------------------------
>>> Cadastrar Cliente
--------------------------------------------"""
    )

    nome = teste_cadastro("Nome completo")

    data_de_nascimento = teste_cadastro("Data de Nascimento(dd/mm/aaaa)")

    cpf = teste_cadastro("CPF")

    if buscar_cliente(clientes, "cpf", cpf) != -1:
        print("\n!!! Erro!\n!!! Já existe um cadastro para esse CPF!\n")
        menu_rodape(clientes, contas, fluxo, -1)

    print("\nEndereço:")

    logradouro = teste_cadastro("Logradouro/rua")

    numero_casa = teste_cadastro("Nº")

    bairro = teste_cadastro("Bairro")

    cidade = teste_cadastro("Cidade")

    estado = teste_cadastro("Estado(XX)")

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado.upper()}"

    novo_cliente = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }

    clientes.append(novo_cliente)
    print("\n\n>>> Cliente cadastrado!")

    fluxo.pop()
    return menu_rodape(clientes, contas, fluxo, -1)


def teste_cadastro(campo):
    entrada_campo = input(f"{campo}: ")

    if (entrada_campo == "") or (campo == "Estado(XX)" and len(entrada_campo) != 2):
        print(f"\n!!! Erro!\n!!! {campo} possui valor inválido!\n")
        return teste_cadastro(campo)
    elif campo == "CPF":
        cpf_tratado = ""
        for digito in entrada_campo:
            if digito >= "0" and digito <= "9":
                cpf_tratado += digito

        if len(cpf_tratado) != 11:
            print("\n!!! Erro!\n!!! CPF inválido!\n")
            return teste_cadastro(campo)

        return cpf_tratado

    return entrada_campo


def buscar_cliente(clientes, chave, valor):
    for cliente in clientes:
        if cliente[chave] == valor:
            return clientes.index(cliente)
    return -1


def buscar_conta(contas, chave, valor):
    for conta in contas:
        if conta[chave] == valor:
            return contas.index(conta)
    return -1


def buscar_lista_contas_por_cpf(contas, cpf_cliente):
    contas_cliente = []

    for conta in contas:
        if conta["cpf_dono"] == cpf_cliente:
            contas_cliente.append(contas.index(conta))

    return contas_cliente


def buscar_lista_contas_por_index_cliente(clientes, contas, index_cliente):
    contas_cliente = []

    for conta in contas:
        if conta["cpf_dono"] == clientes[index_cliente]["cpf"]:
            contas_cliente.append(contas.index(conta))

    return contas_cliente


def retorna_index_conta(contas, numero_conta):
    for conta in contas:
        if numero_conta == conta["numero_conta"]:
            return contas.index(conta)
    return -1


def criar_conta_corrente(clientes, contas, fluxo, index_cliente):
    fluxo.append(criar_conta_corrente)
    print(
        """
--------------------------------------------
>>> Criar Conta Corrente
--------------------------------------------"""
    )

    resposta = input("Tem certeza que deseja\nabrir uma conta corrente? (S/N)")

    if resposta.upper() == "N":
        menu_rodape(clientes, contas, fluxo, index_cliente)

    elif resposta.upper() == "S":
        nova_conta = {
            "agencia": "0001",
            "numero_conta": len(contas) + 1,
            "cpf_dono": clientes[index_cliente]["cpf"],
            "LIMITE_SAQUE": 500.00,
            "SAQUES_DISPONIVEIS": 3,
            "cont_saques": 0,
            "saldo": 0,
            "extrato": "",
        }

        contas.append(nova_conta)

        print("\n>>> Conta criada com sucesso!\n\n")
        imprimir_conta(nova_conta)

    else:
        input("\n!!! Opção Inválida.\nPressione enter para continuar...\n")
        fluxo.pop()
        criar_conta_corrente(clientes, contas, fluxo, index_cliente)

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def listar_clientes(clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(listar_clientes)

    for cliente in clientes:
        if index_cliente == -1:
            # print(conta)
            imprimir_cliente(cliente)

        elif cliente["cpf_dono"] == clientes[index_cliente]["cpf"]:
            # print(conta)
            imprimir_cliente(cliente)

    return menu_rodape(clientes, contas, fluxo, -1)


def imprimir_cliente(cliente):
    print(f"\n\nNome: {cliente['nome']}")
    print(f"Data de Nascimento: {cliente['data_de_nascimento']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Endereço: {cliente['endereco']}")


def listar_contas(clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(listar_contas)

    for conta in contas:
        if index_cliente == -1:
            # print(conta)
            imprimir_conta(conta)

        elif conta["cpf_dono"] == clientes[index_cliente]["cpf"]:
            # print(conta)
            imprimir_conta(conta)

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def imprimir_conta(conta):
    print("\nAgência: " + conta["agencia"])
    print(f"Conta Corrente: {'%04d'%conta['numero_conta']}")
    print("Proprietário (CPF): " + conta["cpf_dono"])
    print(f"Limite por Saque (R$): {conta['LIMITE_SAQUE']:.2f}")
    print(f"Saques disponíveis: {conta['SAQUES_DISPONIVEIS']}")
    print(f"Saques realizados: {conta['cont_saques']}")
    print(f"Saldo: {conta['saldo']:.2f}")


def testar_entrada(str_input):
    valor_entrada = input(str_input)

    if len(valor_entrada) >= 4:
        if valor_entrada[-3] == "." or valor_entrada[-3] == ",":
            str_aux = valor_entrada.replace(".", "").replace(",", "")
            if str_aux.isnumeric() and float(str_aux) > 0:
                return float(str_aux) / 100

    print("\n!!! O valor é inválido!\n")
    return testar_entrada(str_input)


def depositar(clientes, contas, /, fluxo, index_cliente):
    fluxo.append(depositar)
    print(
        """
--------------------------------------------
>>> Depósito
--------------------------------------------"""
    )

    print("\n    Agência: 0001")
    conta_corrente = input("    Conta corrente: ")

    if not conta_corrente.isdigit():
        print("\n!!! Conta corrente inválida!")
        menu_rodape(clientes, contas, fluxo, -1)

    index_conta = retorna_index_conta(contas, int(conta_corrente))

    if index_conta == -1:
        print("\n!!! Conta corrente não encontrada!")
        menu_rodape(clientes, contas, fluxo, -1)

    # print("\n    - formato R$ 00.00")

    valor = testar_entrada("\n    Valor do depósito: R$ ")

    NOW = datetime.now()
    strNOW = NOW.strftime("%d/%m/%y %H:%M")

    contas[index_conta]["saldo"] += valor
    contas[index_conta]["extrato"] += f"{strNOW}    Depósito     R$ {valor:,.2f}\n"

    print("\n>>> Depósito realizado com sucesso!\n")

    return menu_rodape(clientes, contas, fluxo, -1)


def depositar_cliente(clientes, contas, /, fluxo, *, index_cliente=-1):
    fluxo.append(depositar_cliente)

    print(
        """
--------------------------------------------
>>> Depósito
--------------------------------------------"""
    )

    contas_cliente = buscar_lista_contas_por_cpf(contas, clientes[index_cliente]["cpf"])

    if len(contas_cliente) <= 0:
        print("\n!!! Nenhuma conta corrente encontrada!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    else:
        for index in contas_cliente:
            print(
                f"""
\n[{index}] - Agência: {contas[index]['agencia']}
      Conta: {'%04d'%contas[index]['numero_conta']}"""
            )

        opcao = input("\nSelecione a conta em que \ndeseja realizar o depósito: ")

        if not opcao.isdigit():
            print("\n!!! Opção Inválida!")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        id_conta = int(opcao)

        if not id_conta in contas_cliente:
            print("\n!!! Opção Inválida!")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        valor = testar_entrada("\n    Valor do depósito: R$ ")

        NOW = datetime.now()
        strNOW = NOW.strftime("%d/%m/%y %H:%M")

        contas[id_conta]["saldo"] += valor
        contas[id_conta]["extrato"] += f"{strNOW}    Depósito     R$ {valor:,.2f}\n"

        print("\n>>> Depósito realizado com sucesso!\n")

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def sacar(*clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(sacar)
    print(
        """
--------------------------------------------
>>> Saque
--------------------------------------------"""
    )

    print("\n    Agência: 0001")
    conta_corrente = input("    Conta corrente: ")

    if not conta_corrente.isdigit():
        print("\n!!! Conta corrente inválida!")
        menu_rodape(clientes, contas, fluxo, -1)

    index_conta = retorna_index_conta(contas, int(conta_corrente))

    if index_conta == -1:
        print("\n!!! Conta corrente não encontrada!")
        menu_rodape(clientes, contas, fluxo, -1)

    if contas[index_conta]["cont_saques"] >= contas[index_conta]["SAQUES_DISPONIVEIS"]:
        print("\n!!! Saque não permitido!\n")
        print(
            """!!! Você já atingiu sua quantidade
    de saques disponíveis!"""
        )
        menu_rodape(clientes, contas, fluxo, -1)

    # print("\n    - formato R$ 00.00")

    valor = testar_entrada("\n    Valor do saque: R$ ")

    if contas[index_conta]["saldo"] < valor:
        print("\n    Saldo insuficiente!\n\n")
        menu_rodape(clientes, contas, fluxo, -1)

    elif valor > contas[index_conta]["LIMITE_SAQUE"]:
        print("\n!!! Saque não permitido!\n")
        print(
            f"!!! Seu limite de saque é R${contas[index_conta]['LIMITE_SAQUE']:.2f}!\n\n"
        )
        menu_rodape(clientes, contas, fluxo, -1)

    NOW = datetime.today()
    strNOW = NOW.strftime("%d/%m/%y %H:%M")

    saldo -= valor
    cont_saques += 1
    extrato += f"{strNOW}    Saque      - R$ {valor:,.2f}\n"

    print("\n>>> Saque realizado com sucesso!\n\n")

    return menu_rodape(clientes, contas, fluxo, -1)


def sacar_cliente(*, clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(sacar_cliente)
    print(
        """
--------------------------------------------
>>> Saque Cliente
--------------------------------------------"""
    )
    contas_cliente = buscar_lista_contas_por_cpf(contas, clientes[index_cliente]["cpf"])

    if len(contas_cliente) <= 0:
        print("\n!!! Nenhuma conta corrente encontrada!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    for index in contas_cliente:
        print(
            f"""
\n[{index}] - Agência: {contas[index]['agencia']}
      Conta: {'%04d'%contas[index]['numero_conta']}"""
        )

    opcao = input("\nSelecione a conta em que \ndeseja realizar o saque: ")

    if not opcao.isdigit():
        print("\n!!! Opção Inválida!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    id_conta = int(opcao)

    if not id_conta in contas_cliente:
        print("\n!!! Opção Inválida!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    if contas[id_conta]["cont_saques"] >= contas[id_conta]["SAQUES_DISPONIVEIS"]:
        print("\n!!! Saque não permitido!\n")
        print(
            """!!! Você já atingiu sua quantidade
    de saques disponíveis!"""
        )
        menu_rodape(clientes, contas, fluxo, index_cliente)

    # print("\n    - formato R$ 00.00")

    valor = testar_entrada("\n    Valor do depósito: R$ ")

    if contas[id_conta]["saldo"] < valor:
        print("\n    Saldo insuficiente!\n\n")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    elif valor > contas[id_conta]["LIMITE_SAQUE"]:
        print("\n!!! Saque não permitido!\n")
        print(f"!!! Seu limite de saque é R${contas[id_conta]['LIMITE_SAQUE']},00!\n\n")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    NOW = datetime.today()
    strNOW = NOW.strftime("%d/%m/%y %H:%M")

    contas[id_conta]["saldo"] -= valor
    contas[id_conta]["cont_saques"] += 1
    contas[id_conta]["extrato"] += f"{strNOW}    Saque      - R$ {valor:,.2f}\n"

    print("\n>>> Saque realizado com sucesso!\n\n")

    return menu_rodape(clientes, contas, fluxo, index_cliente)


def imprimir_extrato(clientes, contas, fluxo, index_cliente):
    fluxo.append(imprimir_extrato)

    print(
        """
--------------------------------------------
>>> Extrato
--------------------------------------------"""
    )

    print("\n    Agência: 0001")
    conta_corrente = input("    Conta corrente: ")

    if not conta_corrente.isdigit():
        print("\n!!! Conta Inválida!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    index_conta = buscar_conta(contas, "numero_conta", int(conta_corrente))

    if index_conta == -1:
        print("\n!!! Conta corrente não encontrada!")
        menu_rodape(clientes, contas, fluxo, -1)

    if contas[index_conta]["extrato"] == "":
        print("\n\n!!! Não foram realizadas movimentações\n\n")
    else:
        print("\n--------------------------------------------\n")
        print(contas[index_conta]["extrato"])

    print(
        f"""
--------------------------------------------
Saldo = R$ {contas[index_conta]['saldo']:,.2f}
--------------------------------------------"""
    )

    menu_rodape(clientes, contas, fluxo, -1)


def imprimir_extrato_cliente(clientes, contas, fluxo, index_cliente=-1):
    fluxo.append(imprimir_extrato_cliente)
    print(
        """
--------------------------------------------
>>> Extrato
--------------------------------------------"""
    )

    contas_cliente = buscar_lista_contas_por_cpf(contas, clientes[index_cliente]["cpf"])

    if len(contas_cliente) <= 0:
        print("\n!!! Nenhuma conta corrente encontrada!")
        menu_rodape(clientes, contas, fluxo, index_cliente)

    else:
        for index in contas_cliente:
            print(
                f"""
\n[{index}] - Agência: {contas[index]['agencia']}
      Conta: {'%04d'%contas[index]['numero_conta']}"""
            )

        opcao = input("\nSelecione a conta: ")

        if not opcao.isdigit():
            print("\n!!! Opção Inválida!")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        id_conta = int(opcao)

        if not id_conta in contas_cliente:
            print("\n!!! Opção Inválida!")
            menu_rodape(clientes, contas, fluxo, index_cliente)

        print(
            f"""
--------------------------------------------
>>> Agência: {contas[id_conta]['agencia']} Conta: {'%04d'%contas[id_conta]['numero_conta']}
--------------------------------------------"""
        )
        if contas[id_conta]["extrato"] == "":
            print("\n\n!!! Não foram realizadas movimentações\n\n")
        else:
            print("--------------------------------------------\n")
            print(contas[id_conta]["extrato"])

        print(
            f"""
--------------------------------------------
Saldo = R$ {contas[id_conta]['saldo']:,.2f}
--------------------------------------------"""
        )

    menu_rodape(clientes, contas, fluxo, index_cliente)


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
    fluxo = list()

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
    # clientes[0]["contas"].append(nova_conta)
    contas.append(nova_conta)

    menu_principal(clientes, contas, fluxo, -1)


main()
