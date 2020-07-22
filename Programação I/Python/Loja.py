loja = [['Headphones',5.00],
        ['Carregador',5.00],
        ['Filme',10.00],
        ['Bateria',20.00],
        ['Radio',15.00],
        ['Rato',7.50],
        ['Teclado',17.00],
        ['Pen',12.00]]
carrinho = []
for i in range(len(loja)):
    print(loja[i][0],'-' , loja[i][1], 'euros')
print('\n')
while True:
    print('O que quer fazer?')
    print('\n')
    print('1 - Adicionar produtos')
    print('2 - Retirar produtos')
    print('3 - Ver despesa')
    print('"exit" para sair')
    print('\n')
    command = input('>>>')
    if command =='1':
        existe = False
        b = str(input('produto?'))
        for a in range(len(carrinho)):
            if b in carrinho[a]:
                c = int(input('Quantidade?'))
                carrinho[a][1] += c
                existe = True
        if not existe:
            c = int(input('Quantidade'))
            carrinho.append([b,c])

    if command == '2':
        b = str(input('Produto?'))
        for w in range(len(carrinho)):
            if carrinho[w][0] == b:
                carrinho.remove(carrinho[w])
            else:
                print('Nao esta na lista...\n')
    if command == '3':
        preço = 0
        for w in range(len(loja)):
            for i in range(len(carrinho)):
                if loja[w][0] == carrinho[i][0]:
                    print(carrinho[i][1], carrinho[i][0], loja[w][1] * carrinho[i][1], 'euros.')
                    preço =preço + loja[w][1] * carrinho[i][1]
        print('Total = ' ,preço,'\n')
    if command =='exit':
        break
    
