# 1. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
#  calcule e imprima a média geral.

notas = []

for i in range(15):
    nota = float(input("Digite a nota {}: ".format(i+1)))
    notas.append(nota)

media = sum(notas) / len(notas)

# print the average
print("A nota média é: ", media)
