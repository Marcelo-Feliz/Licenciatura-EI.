num1 = float(input('Indique o 1ºnumero '))
num2 = float(input('Indique o 2ºnumero '))
num3 = float(input('Indique o 3ºnumero '))
if num2<num1<num3 or num3<num1<num2:
    print('o numero do meio inserido foi',num1)
if num1<num2<num3 or num3<num2<num1:
    print('o numero do meio inserido foi',num2)
if num1<num3<num2 or num2<num3<num1:
    print('o numero do meio inserido foi',num3)
