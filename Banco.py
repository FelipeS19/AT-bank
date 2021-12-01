def salvar_contas(conta,nome,sobrenome,saldo):
    try:
        dados_conta = f"{conta};{nome} {sobrenome};{saldo}\n"
        with open("contas.txt","a")as arq:
            arq.write(dados_conta)
    except:
        print("Erro ao salvar")
        
def verificar_conta(conta):
    try:
        with open("contas.txt","r")as arq:
            for linha in arq:
                dados = linha.split(";")
                if dados[0] == str(conta):
                    return True
    except:
        print("Erro ao abrir arquivo ou ler arquivo")

def menu():
    print("""
    1 - Incluir conta
    2 - Alterar saldo
    3 - Excluir conta
    4 - Relatório gerencial
    5 - Sair
    """) 
    opçao = int(input("Digite a opção desejada: "))
    return opçao
    
def incluir_conta():
        conta = (input("Digite o número da conta: ")).strip()
        if verificar_conta(conta) == True:
            print("Conta já existente")
        elif conta.isalpha():
            print("Número da conta inválido")
        else:
            nome = input("Digite o nome do correntista: ").lower()
            sobrenome = input("Digite o sobrenome do correntista: ").lower()
            saldo = str(input("Digite o saldo: ")).replace(",",".")
            if saldo.isalpha():
                print("Saldo inválido")
            else:
                saldo = float(saldo)
                if saldo < 0 or saldo == "":
                    print("Saldo inválido")
                else:
                    print("Conta criada com sucesso")
                    salvar_contas(conta,nome,sobrenome,saldo)
                    
def alterar_saldo():
    opçaosaque = menu_saque()
    if opçaosaque == 1:
        saque()
    elif opçaosaque == 2:
        deposito()
                    
def saque():
    conta = int(input("Digite o número da conta: "))
    if verificar_conta(conta) == True:
        with open("contas.txt","r")as arq:
            contas = arq.readlines()
            for linha in contas:
                dados = linha.split(";")
                if dados[0] == str(conta):
                    saldo = float(dados[2])
                    valor = float(input("Digite o valor do saque: ").replace(",","."))
                    saldo -= valor
                    print("Saque realizado com sucesso")
                    with open("contas.txt","w")as arq:
                        for linha in contas:
                            dados = linha.split(";")
                            if dados[0] == str(conta):
                                dados[2] = str(saldo)
                                arq.write(";".join(dados))
                            else:
                                arq.write(linha)
    else:
        print("Conta não encontrada")
        
def deposito():
    conta = int(input("Digite o número da conta: "))
    if verificar_conta(conta) == True:
        with open("contas.txt","r")as arq:
            contas = arq.readlines()
            for linha in contas:
                dados = linha.split(";")
                if dados[0] == str(conta):
                    saldo = float(dados[2])
                    valor = float(input("Digite o valor do deposito: ").replace(",","."))
                    saldo += valor
                    print("Depósito realizado com sucesso")
                    with open("contas.txt","w")as arq:
                        for linha in contas:
                            dados = linha.split(";")
                            if dados[0] == str(conta):
                                dados[2] = str(saldo)
                                arq.write(";".join(dados))
                            else:
                                arq.write(linha)

def menu_saque():
    print("""
    1 - Saque
    2 - Deposito
    """)
    opçaosaque = int(input("Digite a opção desejada: "))
    return opçaosaque
    
def excluir_conta():
    conta = int(input("Digite o número da conta: "))
    if verificar_conta(conta) == True:
        with open("contas.txt","r")as arq:
            contas = arq.readlines()
            for linha in contas:
                dados = linha.split(";")
                if dados[0] == str(conta):
                    if float(dados[2]) == 0:
                        print("Conta excluida com sucesso")
                        with open("contas.txt","r")as arq:
                            contas = arq.readlines()
                            for linha in contas:
                                dados = linha.split(";")
                                if dados[0] == str(conta):
                                    contas.remove(linha)
                                with open("contas.txt","w")as arq:
                                    for linha in contas:
                                        arq.write(linha)
                    else:
                        print("Conta não pode ser excluida")
    else:
        print("Conta não encontrada")
        
def submenu_relatorio():
    print("""
          1 - Listar clientes com saldo negativo
          2 - Listar de clientes com saldo acima de um determinado valor
          3 - Listar todas as contas
          """)
    opçao = input("Digite a opção desejada: \n")
    return opçao

def clientes_saldo_negativo():
    print("Os clientes com o saldo negativo: \n")
    with open("contas.txt","r")as arq:
        contas = arq.readlines()
        for linha in contas:
            dados = linha.split(";")
            if float(dados[2]) < 0:
                print(f"{dados[1]} {dados[2]}")
                
def clientes_saldo_acima():
    valor = input("Digite o valor: ").replace(",",".")
    valor = float(valor)
    print(f"Os clientes com o saldo acima {valor} de reais são: \n")
    with open("contas.txt","r")as arq:
        contas = arq.readlines()
        for linha in contas:
            dados = linha.split(";")
            if float(dados[2]) > valor:
                print(f"{dados[1]} {dados[2]}")

def listar_contas():
    print("Todas as contas cadastradas atualmente são: \n")
    contas = []
    with open("contas.txt","r")as arq:
        for linha in arq:
            dados = linha.split(";")
            contas.append(dados)
    for conta in contas:
            if conta[2] != "0":
                print(f"Conta: {conta[0]}, Nome: {conta[1]}, Saldo: {conta[2]}")
    print("\nRelatório gerencial concluído")

def relatorio_gerencial():
    opçao = submenu_relatorio()
    if opçao == 1:
        clientes_saldo_negativo()
    elif opçao == 2:
        clientes_saldo_acima()
    elif opçao == 3:
        listar_contas()
     
def menu_principal():
    opçao = menu()
    while opçao != 5:
        if opçao == 1:
            incluir_conta()
        elif opçao == 2:
            alterar_saldo()
        elif opçao == 3:
            excluir_conta()
        elif opçao == 4:
            relatorio_gerencial()
        opçao = menu()    

menu_principal()
print("Programa finalizado")