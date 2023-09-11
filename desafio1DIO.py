
menu = """
1 -Depositar
2- Sacar
3- Extrato
4- Sair
"""
          
saldo = 0
limite = 500
n_saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:
    opcao = int(input(menu))
    
    if opcao==1:
        valor = float(input("Insira o valor do deposito:"))
        if valor<0:
            print("valor invalido")
        else:
            print("deposito executado.")
            saldo+=valor
            extrato.append(("deposito",f"R${valor:.2f}"))
            
            
            
    elif opcao==2:
        valor = float(input("Insira o valor desejado:"))
        
        if(valor>saldo):
            print("nao ha saldo suficiente na conta")
        
        elif n_saques==LIMITE_SAQUES:
            print("Limite de saques diarios atingido")
        
        elif valor>500:
            print("o valor maximo permitido para saque eh R$500")
            
        else:
            saldo-=valor
            n_saques+=1
            print(f"saque efetuado, saldo atual = R${saldo:.2f}")
            extrato.append(("saque",f"R${valor:.2f}"))
            
            
    elif opcao==3:
        
        if len(extrato)==0:
            print("Nao foram realizadas movimentacoes")
        
        else:
        
            print("\nExtrato:")
            for item in extrato:
                print(f"{item[0]} ----- {item[1]}")
            
            print("\n---------------------------")
            print(f"saldo total = R${saldo:.2f}")
            print("---------------------------")
            
    elif opcao==4:
        break
    
    else:
        print("opcao invalida, por favor selecione novamente a opcao desejada")
    
