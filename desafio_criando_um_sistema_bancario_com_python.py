menu = """
--------------
[0] Depositar 
[1] Sacar 
[2] Extrato
[3] Sair  
--------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == "0":
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Não foi possível realizar a operação para o valor informado.") 

    elif opcao == "1":
        valor_saque = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo Insuficiente! Não foi possível realizar a operação.")

        elif excedeu_limite:
            print("O valor do saque excede o limite disponível! Não foi possível realizar a operação.")

        elif excedeu_saques:
            print("Número máximo de saques diários realizado! Não foi possível realizar a operação.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("Não foi possível realizar a operação para o valor informado.")          

    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
        


    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.") 
