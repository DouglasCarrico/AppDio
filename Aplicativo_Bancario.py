import textwrap

def menu():
    menu = """\n
    ====== MENU ======
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [7]\tSair
    ==>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n XXXX - Operação falhou! O valor informado é inválido. - XXXX")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n XXXX - Operação falhou! Você não tem saldo suficiente. - XXXX")

    elif excedeu_limite:
        print("\n XXXX - Operação falhou! O valor do saque excede o limite. - XXXX")

    elif excedeu_saques:
        print("\n XXXX - Operação falhou! Número máximo de saques excedido. - XXXX")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n XXXX - Operação falhou! O valor informado é inválido. - XXXX")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
   
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n XXXX - Já existe usuário com esse CPF! - XXXX")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===") 

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n=== Conta criada com sucesso! ===\nAgência:\t{agencia}\nConta:\t\t{numero_conta}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n XXXX - Usuário não encontrado. - XXXX") 
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 20)
        print(textwrap.dedent(linha))
        
def main():
    LIMITE = 2000
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 1

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            print("\n=== Sistema encerrado. ===")
            break

        else:
            print("\n XXXX - Operação inválida. Tente novamente. - XXXX")
    
    
main()