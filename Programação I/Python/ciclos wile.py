import math
def compara(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    elif x<y:
        return -1
##Exercicio2##
def hipotenusa(x,y):
    b=math.sqrt(x**2+y**2)
    return b
##exercicio3##
def countdown(a):
    x=0
    while x<a:
        x=x+1
        print(x)
    while x>0:
        x=x-1
        print(x)
##exercicio4##exercicio5##
a=int(input('Qual o valor?'))

c=0
n=0
n=n+a
while a!=0:
    a=int(input('Qual o valor?'))
    n=n+a
    c=c+1
if c==0:
    m=0
else:
    m=n/c
print('foram introdusidos',c,'valores e a media e',m)
