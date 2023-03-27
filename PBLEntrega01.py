#APLICATIVO DE SORTEIO

  #Estrutura de Dados - Prof Allisson
  #Equipe:
    #Alanna Costa da Silva
    #Caíque Luís Figueiredo Teles de Menezes 
    #Maria Fernanda Martins Mirabile
    #Mayara Araujo Abreu
    #Vinícius Barros Santos

  #SEÇÕES PRINCIPAIS SÃO IDENTIFICADAS POR COMENTÁRIOS EM CAIXA ALTA.
  #Seções secundárias são identificadas por comentários em caixa baixa.


#IMPORTAÇÕES
from random import choice


#LISTAS
lista_premios = []
lista_pessoas = []
backup_pessoas = []
resumo_premios = []
resumo_pessoas = []


#PEDIR PRÊMIOS
qnt_premios = int(input('Quantos prêmios serão sorteados?: '))

for i in range(qnt_premios):
  lista_premios.append(input(f'Insira um Prêmio: '))

print(f'\nPronto! Sua lista de Prêmios:\n{lista_premios}\n')

#PEDIR PESSOAS
qnt_pessoas = int(input('Quantas pessoas participarão do sorteio?: '))

for i in range(qnt_pessoas):
  lista_pessoas.append(input(f'Insira o nome da {i+1}ª pessoa: '))
  
print(f'\nPronto! Sua lista de pessoas:\n{lista_pessoas}')


#SORTEAR PRÊMIOS
print('\nVAMOS COMEÇAR O SORTEIO!')
print('-' * 30)

#Lista backup de participantes caso tenhamos mais prêmios que pessoas.
backup_pessoas = [x for x in lista_pessoas]

for i in range(len(lista_premios)):
  
  #O "if" abaixo serve para o caso de termos mais prêmios que pessoas.
  #O comando reconstitui a lista de pessoas caso todas já tenham sido sorteadas.
  if lista_pessoas == []:
    lista_pessoas = [x for x in backup_pessoas]
  
  #premio_da_vez e pessoa_da_vez representam uma escolha aleatória das respectivas listas, os "sorteados da rodada".
  premio_da_vez = choice(lista_premios)
  print(f'\nO {i+1}º prêmio a ser sorteado será o(a) {premio_da_vez}!')
  
  pessoa_da_vez = choice(lista_pessoas)
  print(f'O(A) {premio_da_vez} vai para... {pessoa_da_vez}!\n')
  
  #O prêmio e seu ganhador são adicionados às listas abaixo, para fazermos o resumo ao fim do sorteio.
  resumo_premios.append(premio_da_vez)
  resumo_pessoas.append(pessoa_da_vez)
  
  #Agora retiramos os sorteados das listas completas, para que não sejam repetidos nas próximas rodadas.
  lista_premios.remove(premio_da_vez)
  lista_pessoas.remove(pessoa_da_vez)

  #Damos uma pausa e perguntamos se podemos continuar.
  cont = input('Podemos continuar? (s/n): ').lower()
  if cont == ('s' or 'sim'):
    continue
  else:
    break


#RESUMO DO SORTEIO
print('-' * 30)
print('\nSORTEIO FINALIZADO!\n')

print('Resumo do Sorteio:')
for i in range(len(resumo_premios)):
  print(f'{i+1}º - {resumo_premios[i]} para {resumo_pessoas[i]}')
  
print('\nParabéns aos ganhadores! Obrigado por participar do sorteio!')
print('-' * 30)