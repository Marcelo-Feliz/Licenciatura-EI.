import math
num = float(input('Escolha um numero '))
if num < 0:
    print('O numero inserido e negativo')
else:
    raiz = math.sqrt(num)
    print('a raiz quadrada de',num, 'e', raiz)
