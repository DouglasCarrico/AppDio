menu ="""
    ===== MENU PRINCIPAL =====

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Novo Usuário
    [5] - Criar Nova Conta
    [6] - Listar Contas
    [7] - Sair
    
    ==>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:

    opcao = input(menu)

    if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor inválido")

    elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_limite = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
               print("Saldo insuficiente")

            elif excedeu_limite:
                print("Operação Falhou! O valor do saque excede o limite diário")

            elif excedeu_limite:
                print("Operação Falhou! O número de saques excede o limite diário")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação Falhou! Valor inválido")

    elif opcao == "3":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "4":

        print("Criar Novo Usuário")
        nome = input("Informe o nome do usuário: ")
        cpf = input("Informe o CPF do usuário: ")
        print(f"Usuário {nome} cadastrado com sucesso!")    

    elif opcao == "5":

        print("Criar Nova Conta")
        numero_conta = input("Informe o número da conta: ")
        print(f"Conta {numero_conta} criada com sucesso!")
        

    elif opcao == "6":
        print("Listar Contas")
        if numero_conta:
            print(f"Conta: {numero_conta}")
        else:
            print("Nenhuma conta cadastrada")

    elif opcao == "7":
        print("Saindo...")    
        
                 
                    


