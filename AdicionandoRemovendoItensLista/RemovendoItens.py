#Retire um item da lista de compras

lista = ['morango', 'detergente', 'kiwi']

print(lista)
retirar = input('Deseja retirar algum item? s/n ').lower()

while retirar == 's':
    for i in range(len(lista)):
        print(i+1, ' - ', lista[i])
    item = int(input('Qual o número do item que deseja remover? ')) -1
    lista.pop(item)
    print(f'Sua lista de compras: \n{lista}')
    retirar = input('Deseja retirar algum item? s/n ').lower()

print(f'Sua lista completa de compras:\n {lista}')
