# VERSAO 2.0 DO DESAFIO DE FAZER UM SISTEMA BANCARIO
# COM UPDATES AGORA
import textwrap


def menu():
    menu =  """\n
    =============== MENU ===============
    [0]\tDepositar
    [1]\tSacar
    [2]\tExtrato
    [3]\tNova Conta
    [4]\tListar Contas
    [5]\tNovo Usuário
    [6]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com Sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo sulficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O Valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd--mm--aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairo - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta Criada com Sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
       linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
       print("=" * 100)
       print(textwrap.dedent(linha)) 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
                 
            


        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "3":
            criar_usuario(usuarios)

        elif opcao =="4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta: 
                contas.append(conta)

        elif opcao =="5":
            listar_contas(contas)

        elif opcao =="6":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()