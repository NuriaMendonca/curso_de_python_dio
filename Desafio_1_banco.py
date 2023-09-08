
# Desafio 1
#Criando um sistema bancário

''' Sistema bancário com operações: depósito, saque e extrato
DEPÓSITO - apenas valores positivos
- armazenamento em uma variável
- exibir todos os lançamentos no extrato

SAQUES
- apenas 3 saques diários
- limite de R$ 500,00 por saque
- caso sem saldo, emitir mensagem
- armazenamento em variável
- exibir todos os lançamentos no extrato

 EXTRATO
- listar todas as movimentações
- ao final exibir o saldo atual da conta
- se estiver em branco, exibir que não houveram movimentações
'''

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3





while True:
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:  # validação de valor
            saldo += valor    # atribuição de valor no saldo em conta
            extrato += f"Depósito: R$ {valor:.2f}\n" # concatena o  valor do depósito e registra no extrato
            # o .2f, serve para delimitar as casas decimais do valor

        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verificações de possibilidades para o saque
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:  # Validação de saldo, para verificar se não está tentando sacar valor negativo
            saldo -= valor  #debita o valor sacado do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Concatena o valor ao saque e registra no extrato a movimentação
            numero_saques += 1  #registra a movimentação, para o limite de saques

        else:
            print("Operação falho! O valor informado é inválido.")

    elif opcao == "e":
        print("\n =============== EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato) #If ternário | que verifica se o extrato está vazio
        print(f"\nSaldo: R$ {saldo:.2f}") # exibe o saldo
        print("==========================================")

    elif opcao =="q":  # para sair
        break

    else:
        print("Operção inválida, por favor selecione novamente a operação desejada.")




    