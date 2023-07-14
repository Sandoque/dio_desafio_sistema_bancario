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
        print("Saque")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, favor inserir novamente a operação desejada")

