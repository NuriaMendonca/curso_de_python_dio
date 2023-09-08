
#Interpolação de variáveis

#Old Style %

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "python"

print("Olá, me chamo %s. Eu tenho %d anos de idade,  trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))
# Essa liguagem caiu em desuso, devido aos problemas de alterar os dados e ela permanecer estática


#Método format

print("Olá, me chamo {}. Eu tenho {} anos de idade,  trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
# Essa liguagem é parecida com a de cima, a diferença é que possuiu um pouco mais de mobilidade.



#F String  (é a formatação mais utilizada)

print(f"nome: {nome} Idade: {idade}")
