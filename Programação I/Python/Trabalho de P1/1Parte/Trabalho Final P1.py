def coordenadas(x,y):
    return (sopaletras[x][y])

def encontrar(x,y,z):
    if encontrar_baixo(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Baixo')
    if encontrar_diagonaldireitabaixo(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Sudeste')
    if encontrar_direita(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Direita')
    if encontrar_diagonaldireitacima(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Nordeste')
    if encontrar_cima(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Cima')
    if encontrar_diagonalesquerdacima(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Noroeste')
    if encontrar_esquerda(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Esquerda')
    if encontrar_diagonalesquerdabaixo(x,y,z) == True:
        print(z,': Linha',x+1,'Coluna',y+1,', Sudoeste')
    
def encontrar_baixo(x,y,z):
    if z == '':
        return True
    if x > num_palavras-1 or y > num_palavras:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_baixo(x+1,y,z[1:])
    else:
        return False

def encontrar_diagonaldireitabaixo(x,y,z):
    if z == '':
        return True
    if x > num_palavras-1 or y > num_palavras-1:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_diagonaldireitabaixo(x+1,y+1,z[1:])
    else:
        return False

def encontrar_direita(x,y,z):
    if z == '':
        return True
    if x > num_palavras-1 or y > num_palavras-1:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_direita(x,y+1,z[1:])
    else:
        return False

def encontrar_diagonaldireitacima(x,y,z):
    if z == '':
        return True
    if x  < 0 or y > num_palavras-1:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_diagonaldireitacima(x-1,y+1,z[1:])
    else:
        return False

def encontrar_cima(x,y,z):
    if z == '':
        return True
    if x < 0 or y > num_palavras-1:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_cima(x-1,y,z[1:])
    else:
        return False

def encontrar_diagonalesquerdacima(x,y,z):
    if z == '':
        return True
    if x < 0 or y < 0:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_diagonalesquerdacima(x-1,y-1,z[1:])
    else:
        return False

def encontrar_esquerda(x,y,z):
    if z == '':
        return True
    if x > num_palavras or y < 0:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_esquerda(x,y-1,z[1:])
    else:
        return False

def encontrar_diagonalesquerdabaixo(x,y,z):
    if z == '':
        return True
    if x > num_palavras-1 or y < 0:
        return False
    if coordenadas(x,y) == z[0]:
        return encontrar_diagonalesquerdabaixo(x+1,y-1,z[1:])
    else:
        return False
            
def main():
    global num_palavras, sopaletras, palavras
    fic=str(input('nome: '))+'.txt' #nome do ficheiro
    f=open(fic) #Abrir o ficheiro
    sopaletras=[]#tabela de sopa de letras
    a=[]#lista com as primeiras letras de cada palavra(inutil)
    palavras=[]#lista com as palavras
    num_palavras=int(f.readline())
    for i in range(num_palavras):
        a.append(f.readline().upper())
        palavras.append(a[i][0:-1])
    a=[]
    for c in range(num_palavras):
        a.append(f.readline())
        sopaletras.append(a[c][0:-1])
    sopaletras.pop()
    sopaletras.append(a[c])
    a=[]
    f.close()
    for i in range(num_palavras):
        a.append((palavras[i][0]))
    for i in range(num_palavras):
        for w in range(num_palavras):
            for q in range(num_palavras):
                encontrar(i,w,palavras[q])
