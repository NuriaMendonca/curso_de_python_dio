#Estrutura de repetição break



while True:#condição que determina looping infinito
    numero = int(input("Informe um número: "))
    
    if numero == 10: #se o número não for igual a 10, ele será sempre exibido. Só para quando for 10.
        break

    print(numero)


# exemplo de break com range

for numero in range (100):

    if numero == 12:
        break

    print(numero, end=" ")


# CONTINUE  (é utilizado para pular/desviar de uma condição específica dentro do laço de repetição)

for numero in range (100):

    if numero == 12: # Exibe a sequência de números pulando o número 12
        continue

    print(numero, end=" ")
