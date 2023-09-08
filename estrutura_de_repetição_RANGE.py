# Estrutura de repetição com RANGE

''' Range é uma função built-in do Python, ela é usada para reproduzir uma sequência de números
inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range (i,j) será 
produzido:

i, i+1, i+2, i+3, ..., j+1.

ela recebe 3 argumentos: stop(obrigatório), start (opicional) e step (opicional)

'''

range(4)
list(range(4)) #função para chamar lista

#exemplo de For com Range (função buil-in range)
for numero in range(0,51,5):
    print(numero,end=" ")

