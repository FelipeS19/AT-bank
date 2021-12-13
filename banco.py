#Funcionalidades

def salvar_mudanças(contas):
    try:
        with open("contas.txt","w")as arq:
            for conta in contas:
                arq.write((conta[0]+";"+conta[1]+";"+ str(conta[2])+"\n"))
    except:
        print("\033[1;31mErro ao salvar\033[m")
    
def ler_arquivo():
    contas = []
    try:
        with open("contas.txt","r")as arq:
            for linha in arq:
                contas.append(linha.strip().split(";"))
        return contas
    except:
        print("\033[1;31mErro ao ler arquivo\033[m")
        return False
        
def validar_inteiro():
    while True:
        try:
            num_int = int(input("Digite a opção: "))
            return num_int
        except: ValueError
        print("Opção inválida")
                
def validar_float():
    while True:
        try:
            num_float = float(input("Digite o valor: "))
            return num_float
        except: ValueError
        print("Valor inválido")

#inclusão de contas

def existe_conta(numero):
    for linha in ler_arquivo():
        if (linha[0] == numero):
            return True
    return False
    
def entrar_numero():
    while True:
        numero = (input("Digite o número da conta com 6 digitos: ")).strip()
        if (len(numero) == 6):
            if (numero.isnumeric() == True):
                return numero
            else:
                print("\033[1;31mDigite apenas numeros\033[m")
                return False
        else:
            print("\033[1;31mDigite um número de 6 dígitos\033[m")
            return False
    
def entrar_nome():
    while True:
        nome = (input("Digite o nome e sobrenome: "))
        if (len(nome.split()) >=2):
            return nome
        else:
            print("\033[1;31mNome inválido!\nDigite nome e sobrenome\033[m")
            return False
    
def entrar_saldo():
    while True:
        valor = validar_float()
        if (valor > 0):
            return valor
        else:
            print("\033[1;31mDigite um valor maior que 0\033[m")
    
def incluir_conta(contas):
    while True:
        numero = entrar_numero()
        if (numero != False):
            if (existe_conta(numero) == False):
                nome = entrar_nome()
                if (nome != False):
                    saldo = entrar_saldo()
                    if (saldo != False):
                        print("")
                        print("\033[1;32mConta cadastrada com sucesso\033[m")
                        contas.append([numero,nome,saldo])
                        break
            else:
                print("\033[1;31mConta já existe\033[m")

#alteração de valores   
       
def alterar_saldo(contas):
    opçaosaque = menu_saldo()
    if (opçaosaque == 1):
        saque(contas)
    elif (opçaosaque == 2):
        deposito(contas)
    elif (opçaosaque == 3):
        menu_principal(contas)
                    
def saque(contas):
    conta = entrar_numero()
    if (existe_conta(conta) == True):
        for linha in contas:
            if (linha[0] == conta):
                print("Saldo atual é de R$",linha[2])
                saldo = float(linha[2])
                valor = validar_float()
                if (valor > 0):
                    saldo -= valor
                    linha[2] = saldo
                    print("\033[1;32mSaque realizado com sucesso\033[m")
                else:
                    print("Valor inválido")
    else:
        print("Conta não encontrada")
    
def deposito(contas):
    conta = entrar_numero()
    if (existe_conta(conta) == True):
        for linha in contas:
            if (linha[0] == conta):
                print("Saldo atual é de R$",linha[2])
                saldo = float(linha[2])
                valor = validar_float()
                if (valor > 0):
                    saldo += valor
                    linha[2] = saldo
                    print("\033[1;32mDeposito realizado com sucesso\033[m")
                else:
                    print("Valor inválido")
    else:
        print("Conta não encontrada")
                                
def menu_saldo():
    print("""
    1 - Saque
    2 - Deposito
    3 - Voltar ao menu principal
    """)
    opçaosaldo = validar_inteiro()
    if (opçaosaldo >= 1) and (opçaosaldo <= 3):
        return opçaosaldo
    else:
        print("Opção inválida")
        menu_saldo()
        return False

#exclusão de contas

def excluir_conta(contas):
    conta = entrar_numero()
    if (existe_conta(conta) == True):
        for linha in contas:
            if (linha[0] == conta) and (float(linha[2]) == 0):
                contas.remove(linha)
                print("\033[1;32mConta excluída com sucesso\033[m")
                menu_principal(contas)
    else:
        print("Conta não encontrada")

#relatórios de contas

def submenu_relatorio():
    print("""
    1 - Listar clientes com saldo negativo
    2 - Listar de clientes com saldo acima de um determinado valor
    3 - Listar todas as contas
    4 - Voltar ao menu principal
    """)
    opçaorel = validar_inteiro()
    if (opçaorel >= 1) and (opçaorel <= 4):
        return opçaorel
    else:
        print("Opção inválida")
        return False
    
def clientes_saldo_negativo():
    dados = ler_arquivo()
    print("\nAs contas com saldo negativo são\n")
    for linha in dados:
        if (float(linha[2]) < 0):
            print("\n",*linha)
                
def clientes_saldo_acima():
    contas = ler_arquivo()
    valor = entrar_saldo()
    print(f"\nAs contas com saldo acima de {valor} são\n")
    if valor != False:
        for linha in contas:
            if (float(linha[2]) > valor):
                print("\n",*linha)
    

def listar_contas():
    contas = ler_arquivo()
    print("\nTodas as contas cadstradas são\n")
    for conta in contas:
        print("\n",*conta)

def relatorio_gerencial(contas):
    opçao = submenu_relatorio()
    if (opçao == 1):
        clientes_saldo_negativo()
    elif (opçao == 2):
        clientes_saldo_acima()
    elif (opçao == 3):
        listar_contas()
    elif (opçao == 4):
        menu_principal(contas)
     
#programa principal

def menu():
    print("""
    1 - Incluir conta
    2 - Alterar saldo
    3 - Excluir conta
    4 - Relatório gerencial
    5 - Sair
    """) 
    opçao = validar_inteiro()
    if (opçao >= 1) and (opçao <= 5):
        return (opçao)
    else:
        print("Opção inválida")
        return False   
     
def menu_principal(contas):
    opçao = menu()
    while True:
        if (opçao == 1):
            incluir_conta(contas)
        elif (opçao == 2):
            alterar_saldo(contas)
        elif (opçao == 3):
            excluir_conta(contas)
        elif (opçao == 4):
            relatorio_gerencial(contas)
        elif (opçao == 5):
            print("\033[1;32m Obrigado por utilizar\033[m")
            salvar_mudanças(contas)
            return False

contas = ler_arquivo()
menu_principal(contas)