menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # INICIO operação de DEPÓSITO
    if opcao == "1":
        valor_do_deposito = float(input("Informe o valor a ser depositado: "))
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            extrato += f"Deposito de R$ {valor_do_deposito:.2f} realizado com sucesso.\n"
        else:
            print("Operação não pode ser realizada.\nValor informado é inválido.")
    # INICIO operação de SAQUE
    elif opcao == "2":
        valor_do_saque = float(input("Informe o valor a ser sacado: "))

        ultrapassou_saldo = valor_do_saque > saldo
        ultrapassou_limite = valor_do_saque > limite
        ultrapassou_quantidade_saques = numero_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("Operação não pode ser realizada.\nSeu saldo é insuficiente.")
        elif ultrapassou_limite:
            print("Operação não pode ser realizada.\nO valor solicitado para saque excede seu limite.")
        elif ultrapassou_quantidade_saques:
            print("Operação não pode ser realizada.\nQuantidade máxima de saques ultrapassada.")
        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            extrato += f"Saque de R$ {valor_do_saque:.2f} realizado com sucesso.\n"
            numero_saques += 1
        else:
            print("Operação não pode ser realizada.\nValor informado é inválido.")
    # INICIO operação de EXTRATO
    elif opcao == "3":
        print("===========Extrato===========")
        if saldo == 0:
            print("Não foram realizadas movimentações.\n")
            print(f"Saldo Atual: R$ 0,00")
        else:
            print(extrato + "\n")
            print(f"Saldo Atual: R$ {saldo:.2f}")
        print("=============================")
    # INICIO operação de SAIR
    elif opcao == "4":
        break
    else:
        print("Operação não pode ser realizada.\nEscolha uma das opções apresentadas.")