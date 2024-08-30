menu = '''
###########
Digite:
d para Depositar
s para Sacar
e para Extrato
q para Sair

==>
'''


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Insira a quantidade a ser depositada: "))
        if deposito <= -1:
            while deposito <= -1:
                deposito = float(input("Por favor, insira um número positivo: "))
                if deposito > -1:
                    saldo += deposito
                    print(f"Você depositou R${deposito:.2f}. Agora seu saldo é de R${saldo:.2f}")
                    extrato += f"Deposito: R${deposito:.2f}\n"
        else:
            saldo += deposito
            print(f"Você depositou R${deposito:.2f}. Agora seu saldo é de R${saldo:.2f}")
            extrato += f"Deposito: R${deposito:.2f}\n"
    elif opcao == "s":
        print("Sacar")
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite máximo de saques diário")
        else:
            saque = float(input("Insira a quantidade a ser sacada: "))
            if saque > 500:
                print("Seu limite máximo é de R$500.00 por saque")
            elif saldo <= 0 or saldo < saque:
                print("Não será possível sacar por falta de dinheiro")
            else:
                saldo -= saque
                numero_saques += 1
                print(f"Você sacou R${saque:.2f}. Agora seu saldo é de R${saldo:.2f}")
                extrato += f"Saque: R${saque:.2f}\n"
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada.")
