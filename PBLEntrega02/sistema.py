#SISTEMA DE GERENCIAMENTO DE RESTAURANTE - PBL2
  #Estrutura de Dados - Prof Allisson
  
  #Equipe - Clube das Winx:
    #Alanna Costa da Silva
    #Caíque Luís Figueiredo Teles de Menezes 
    #Maria Fernanda Martins Mirabile
    #Mayara Araújo Abreu
    #Vinícius Barros Santos

  #SEÇÕES PRINCIPAIS SÃO IDENTIFICADAS POR COMENTÁRIOS EM CAIXA ALTA.
  #Seções secundárias são identificadas por comentários em caixa baixa.
  

#IMPORTAÇÕES
from visual import *
from arquivo import *
from time import sleep


#MESAS
#Mesa = False (quando estiver desocupada) | Mesa = True (quando estiver ocupada)
mesa1 = False
mesa2 = False
mesa3 = False

mesas = [mesa1, mesa2, mesa3]


#CONTADOR DE ABERTURAS
#Conta a quantidade de vezes que a mesa foi aberta
contador_mesa1 = 0
contador_mesa2 = 0
contador_mesa3 = 0

contadores = [contador_mesa1, contador_mesa2, contador_mesa3]


#ID DOS ARQUIVOS
comanda_total = 'comanda_total.txt'
comanda1 = 'comanda_mesa1.txt'
comanda2 = 'comanda_mesa2.txt'
comanda3 = 'comanda_mesa3.txt'

comandas = [comanda1, comanda2, comanda3]


#CARDÁPIO
codigo = ['001', '002']
nome = ['Pastel de Queijo', 'Caldo de Cana']
preco = [5, 4]

cardapio = [codigo, nome, preco]


#MANIPULAÇÃO DO ARQUIVO GERAL
if not arquivoExiste(comanda_total):
    criarArquivo(comanda_total)

opc = input(f'\033[0;33mDeseja apagar os arquivos usados anteriormente? (s/n): \033[m').lower()
if opc == 's':
  limparArquivo(comanda_total)
  
  for arquivo in comandas:
    limparArquivo(arquivo)
  print('Arquivos apagados com sucesso.\n')


#MENU DO SISTEMA
while True:
  
  resposta = menu(['Abrir Nova Comanda', 'Adicionar Pedido', 'Fechar Comanda de uma Mesa', 'Fechar Comanda do Restaurante', 'Sair do Sistema'])

  match resposta:
    
    #Abrir Nova Comanda
    case 1:
      abrirComanda(mesas, comandas, contadores)

    #Adicionar Pedido
    case 2:
      adicionarPedido(mesas, comandas, contadores, cardapio)

    #Fechar Comanda de uma Mesa
    case 3:
      fecharComanda(cardapio, mesas)

    #Fechar Comanda do Restaurante
    case 4:
      
      mesas_ocupadas = []
      
      for mesa in mesas:
        if mesa == True:
          mesas_ocupadas.append(mesa)
        
      if mesas_ocupadas == []:
        fecharComandaRestaurante(cardapio, mesas, contadores, comanda_total)
      else:
        print('\033[0;31mAinda existem mesas abertas. Feche-as para continuar.\033[m')      
      
    
    #Opção de Sair do Sistema
    case 5:
      cabecalho('Saindo do sistema... Até logo!')
      break

    #Opção Inválida
    case _:
        print('\033[0;31mErro! Digite uma opção válida.\033[m')

  sleep(1)