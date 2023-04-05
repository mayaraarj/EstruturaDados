from visual import *
from time import sleep


#FUNÇÕES PARA ARQUIVOS
def arquivoExiste(nome):
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True


def criarArquivo(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print(f'Houve um erro na criação do arquivo {nome}.')
  else:
    print(f'Arquivo {nome} criado com sucesso!')


def limparArquivo(nome):
  try:
    with open(nome, 'r+') as a:
      a.truncate(0)
      a.seek(0)
  except:
    print('Erro ao limpar arquivo.')


def escreverArquivo(arq, num_mesa, codigo, contador, arq_total='comanda_total.txt'):
  
  with open(arq, 'a') as a:
    a.write(f'{codigo};{num_mesa};{contador};\n')
  
  with open(arq_total, 'a') as a:
    a.write(f'{codigo};{num_mesa};{contador};\n')


#FUNÇÕES PARA COMANDAS
def abrirComanda(mesas, comandas, contadores):
      
  while True:
      
    num_mesa = leiaInt('Deseja abrir uma nova comanda para qual mesa? (1/2/3): ')
    index_mesa = num_mesa - 1
    
    if str(num_mesa) not in ('1', '2', '3'):
      print('\033[0;31mErro! Digite uma mesa válida.\033[m')
    
    elif mesas[index_mesa]:
      #Só podemos prosseguir caso a mesa em questão esteja desocupada (mesa == 'False').
      print('\033[0;31mErro! Essa mesa está ocupada no momento.\033[m')
      break
    
    else:     
      #Certificamos de que o arquivo para essa comanda existe.
      if not arquivoExiste(comandas[index_mesa]):
        criarArquivo(comandas[index_mesa])
        
      #Limpamos o arquivo e atribuímos o valor 'True' para a mesa em questão (que representa o estado de ocupada).
      limparArquivo(comandas[index_mesa])

      mesas[index_mesa] = True
      contadores[index_mesa] += 1
        
      print(f'Nova comanda para a mesa {num_mesa} aberta com sucesso!')
      break


def adicionarPedido(mesas, comandas, contadores, cardapio):
    
  opc = 's'
  
  while opc == 's':
      
    #Perguntar Mesa
    num_mesa = leiaInt('Deseja adicionar pedido para qual mesa? (1/2/3): ')
    index_mesa = num_mesa - 1
    
    if str(num_mesa) not in ('1', '2', '3'):
      print('\033[0;31mErro! Digite uma mesa válida.\033[m')
    
    elif not mesas[index_mesa]:
      print('\033[0;31mErro! Para adicionar pedidos à essa mesa você primeiro deve abrir uma comanda.\033[m')
      break
    
    else:
      while True:
          
        #Mostrar Cardápio
        imprimirCardapio(cardapio)
        
        #Perguntar Pedido
        pedido = input('Qual o código do item desejado?: ').strip()
        
        if pedido not in cardapio[0]:
          print('\033[0;31mErro! Digite um item válido.\033[m')
        else:
          quantidade = leiaInt(f'Qual a quantidade desejada?: ')            
          
          for x in range(quantidade):
            
            #Registrar Pedido na Comanda | arq, mesa, codigo, contador
            escreverArquivo(comandas[index_mesa], num_mesa, pedido, contadores[index_mesa])
          
          print(f'Novo pedido para a mesa {num_mesa} adicionado!')
          opc = input('\nDeseja adicionar mais algum pedido? (s/n): ').lower()
          break  
        sleep(1)


def fecharComanda(cardapio, mesas):
  
  itens = []
  preco = []
  
  while True:
    #Perguntar Mesa
    num_mesa = leiaInt('Deseja fechar a comanda de qual mesa? (1/2/3): ')
    index_mesa = num_mesa - 1
    
    if str(num_mesa) not in ('1', '2', '3'):
      print('\033[0;31mErro! Digite uma mesa válida.\033[m')
    else:
      break
  
  if mesas[index_mesa]:
    
    with open(f'comanda_mesa{num_mesa}.txt', 'r') as a:
        
      for linha in a:
        dados = linha.split(';')
        
        codigo = dados[0]
        mesa = dados[1]
        contador = dados[2]
        
        index_item = cardapio[0].index(codigo)
        itens.append(codigo)
        preco.append(cardapio[2][index_item])
    
    try:
      codigo
    except:
      print('\033[0;31mEssa comanda está vazia, ela será fechada agora.\033[m')
    else:
      num_pessoas = leiaInt('Quantas pessoas pagarão a conta?: ') 
       
      sleep(1)
      imprimirComanda(mesa, num_pessoas, itens, preco, cardapio)
    finally:
      mesas[index_mesa] = False
  
  else:
    print('\033[0;31mErro! Essa mesa não está sendo utilizada no momento.\033[m')
        
        
def fecharComandaRestaurante(cardapio, mesas, contadores, comanda_total):
  
  itens = []
  preco = []
  mesas_ocupadas = []
  
  with open(comanda_total, 'r') as a:
        
    for linha in a:
      dados = linha.split(';')

      codigo = dados[0]
      mesa = dados[1]
      contador = dados[2]
      
      index_item = cardapio[0].index(codigo)
      itens.append(codigo)
      preco.append(cardapio[2][index_item])
    
    try:
      codigo
    except:
      print('\033[0;31mA comanda do restaurante está vazia.\033[m')
    else:
      sleep(1)
      imprimirComandaRestaurante(itens, preco, contadores, cardapio)
