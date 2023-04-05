#Adicione itens a uma lista de supermercado

lista = []
opcao = 's'

while opcao == 's':
    lista.append(input('Insira um item para a sua lista de compras: '))
    print(f'Lista de compras: {lista} \n')
    opcao = input('Deseja continuar? s/n ').lower()

print(f'Sua lista completa de compras: \n {lista}')