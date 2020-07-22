def triangulo(a,b,c):    
        if a==b==c and a!=0:
            print('é um triangulo equilatero')
        elif a==b!=c or a==c!=b or b==c!=a:
            print('o triangulo é isosceles')
        elif a!=b!=c and a+b>c and a+c>b and b+c>a:
            print('triangulo escaleno')
        else:
            print('Nao e triangulo')
