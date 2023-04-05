def leiaInt(msg):

  while True:
    try:
      valor = int(input(msg).strip())
      
    except KeyboardInterrupt:
      print("\033[0;31mUsuário preferiu não digitar esse número.\033[m")
      valor = 0
      break
    
    except:
      print("\033[0;31mErro! Digite um número inteiro válido.\033[m")
      
    else:
      break
  return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


def imprimirCardapio(cardapio):
  cabecalho('CARDÁPIO')
  
  print('Código'.center(10), 'Descrição'.center(22), 'Preço'.center(10))
    
  for i in range(2):
    print(f'\033[34m{cardapio[0][i]:^10} {cardapio[1][i]:^22} R${cardapio[2][i]:^7.2f}\033[m')
    
  print(linha())


def listarComanda(itens, cardapio):
  
  print(linha())
  print('Qtd'.center(5), 'Descrição'.center(20), 'Unidade'.center(8), 'Total'.center(8))
  
  for item in cardapio[0]:
    
    if item in itens:
      item_idx = cardapio[0].index(item)
      
      qtd = itens.count(item)
      descricao = cardapio[1][item_idx]
      preco_unidade = cardapio[2][item_idx]
      preco_total = preco_unidade * qtd
      
      print(f'{qtd:^5} {descricao:^20} {preco_unidade:^8.2f} {preco_total:^8.2f}')
  print(linha())


def imprimirComanda(num_mesa, num_pessoas, itens, preco, cardapio):
  
  sub_total = sum(preco)
  gorjeta = sub_total*0.1
  total = sub_total + gorjeta
  total_por_pessoa = total/num_pessoas
  
  print('\033[0;33m')
  print(linha())
  print('RESTAURANTE CLUBE DAS WINX'.center(42))
  print(f'--- MESA {num_mesa} ---'.center(42))

  listarComanda(itens, cardapio)
  
  print(f'Sub Total:{sub_total:>32.2f}')
  print(f'Gorjeta Sugerida:{gorjeta:>25.2f}')
  print(linha())
  
  print(f'Total:{total:>36.2f}')
  print(linha())
  
  print(f'Número de Pessoas:{num_pessoas:>23}')
  print(f'Por Pessoa:{total_por_pessoa:>31.2f}') 
  print(linha())
  
  print('\033[m')
  
  
def imprimirComandaRestaurante(itens, preco, contadores, cardapio):
  
  total = sum(preco)
  media_por_mesa = total/sum(contadores)
  
  print('\033[0;33m')
  print(linha())
  print('RESTAURANTE CLUBE DAS WINX'.center(42))
  print(f'--- COMANDA GERAL ---'.center(42))
  
  listarComanda(itens, cardapio)
  
  print(f'Total:{total:>36.2f}')
  print(linha())
  
  print('\033[m')
