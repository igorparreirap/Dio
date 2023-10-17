menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saques_realizados = 0
depositos_realizados = 0

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            depositos_realizados += 1
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser positivo.")
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: R$ "))
            if valor_saque > 0 and valor_saque <= limite and saldo >= valor_saque:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                saques_realizados += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            elif valor_saque <= 0:
                print("Valor do saque deve ser positivo.")
            elif valor_saque > limite:
                print(f"Limite de saque diário é de R$ {limite:.2f}.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Limite de saques diários atingido.")
    
    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print("Sair")
        break

print(f"Total de saques realizados hoje: {saques_realizados}")
print(f"Total de depósitos realizados hoje: {depositos_realizados}")
