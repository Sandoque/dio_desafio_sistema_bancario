menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limites_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! valor inválidoo.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limites_saques

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! valor inválidoo.")

    elif opcao == "e":
        print("\n######################### EXTRATO #########################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: {saldo:.2f} ")
        print("===============================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, favor inserir novamente a operação desejada")
