#Importar módulos 
import random       
from tkinter import *
from copy import deepcopy

#Declarção de variáveis que serão usadas em mais do que uma função
tabuleiro = list()
territorio = [[0,0]]
territorio_inimigo =list()
tabuleiro_cores = list()
njogadas = 30
#A função jogar() é a que começa o jogo, abrindo o "menu" que pede ao utilizador 
def jogar():
    global op_jogo
    op_jogo = 3
    op_tab = 3
    print('Bem Vindo ao Jogo!')
    while int(op_jogo) not in [0,1,2]:    #Pergunta se queremos jogar sozinhos, contra AI ou sair. Repete pergunta até input ser válido
        print('0 - Sair')
        print('1 - Único Jogador')
        print('2 - IA')
        op_jogo = input()
        if int(op_jogo) not in [0,1,2]:   #Descarta as opções que não estejam no menu
            print('Selecione uma opção válida')
    if op_jogo == '0':
        return     
    while int(op_tab) not in [1,2]:       #Depois de selecionar o modo de jogo, seleciona-se o tipo de tabuleiro. Repete pergunta até input ser válido
        print('1 - Carregar Tabuleiro')
        print('2 - Gerar Tabuleiro')
        op_tab = input()
        if int(op_tab) not in [1,2]:      #Descarta as opções que não estejam neste segundo menu
            print('Selecione uma opção válida')
    if op_tab == '1':
        carregar_tab()
    if op_tab == '2':
        gerar_tab()
    if op_jogo == '1':
        unico_jogador()
    if op_jogo == '2':
        IA()

def carregar_tab():                       #Função que carrega o tabuleiro depois da opção ser selecionada no menu
    ftab = open('tabuleiro.txt')          #O ficheiro que será carregado terá de ter apenas este nome:"tabuleiro.txt"
    i =-1
    for line in ftab:                     #Transforma os números que estão dentro do tabuleiro.txt em listas para gerar o tabuleiro de jogo
        tabuleiro.append([])
        i += 1
        line = line.strip()
        for n in line:
            tabuleiro[i].append(int(n))

            
    global territorio_inimigo
    territorio_inimigo=[[len(tabuleiro)-1,len(tabuleiro)-1]]
    for casa in territorio:    #Aumenta o nosso território inicial, caso o nosso primeiro número tenha idênticos adjacentes.
        #territorio tem coordenadas do tabuleiro. casa[0] será o x e casa[1] será o y
        if dentro_tab(casa[0],casa[1]+1):   
            if tabuleiro[casa[1]+1][casa[0]] == tabuleiro[casa[1]][casa[0]]: #Combinações 2 por 2 de x, y, x+1, y+1, x-1, y-1 são coordenadas das casas ao lado da célula x,y
                    territorio.append([casa[0],casa[1]+1]) 
        if dentro_tab(casa[0]+1,casa[1]):
            if tabuleiro[casa[1]][casa[0]+1] == tabuleiro[casa[1]][casa[0]]:
                    territorio.append([casa[0]+1,casa[1]])
                         
    for casa in territorio_inimigo:   #Aumenta o território inicial da IA, caso o seu primeiro número tenha idênticos adjacentes
        if dentro_tab(casa[0],casa[1]-1):
            if tabuleiro[casa[1]-1][casa[0]] == tabuleiro[casa[1]][casa[0]]:
                    territorio_inimigo.append([casa[0],casa[1]-1])
        if dentro_tab(casa[0]-1,casa[1]):
            if tabuleiro[casa[1]][casa[0]-1] == tabuleiro[casa[1]][casa[0]]:
                    territorio_inimigo.append([casa[0]-1,casa[1]])

def gerar_tab():          #Função que gerará o tabuleiro
    for y in range(15):
        tabuleiro.append([])
        for x in range(15):
            tabuleiro[y].append(random.randint(1, 6))

    for i in range(5):   #Pseudo-randomizador, escolhe uma coordenada ao calhas e nessa posição transforma outras duas próximas em iguais a ela
        x = random.randint(1,13)
        y = random.randint(1,13)   #Escolhe coordenadas ao calhas para modificar

        formato = random.randint(1,6) #Escolhe um formato para modificar duas casas, qualquer formato que exista
        
        if formato == 1 and dentro_tab(x+1,y) and dentro_tab(x,y-1) : #Direita e cima
            tabuleiro[x+1][y] = tabuleiro[x][y]
            tabuleiro[x][y-1] = tabuleiro[x][y]
        if formato == 2 and dentro_tab(x+1,y) and dentro_tab(x,y+1): #Direita e baixo
            tabuleiro[x+1][y] = tabuleiro[x][y]
            tabuleiro[x][y+1] = tabuleiro[x][y]
        if formato == 3 and dentro_tab(x-1,y) and dentro_tab(x,y-1): #Esquerda e cima
            tabuleiro[x-1][y] = tabuleiro[x][y]
            tabuleiro[x][y-1] = tabuleiro[x][y]
        if formato == 4 and dentro_tab(x-1,y) and dentro_tab(x,y+1): #Esquerda e baixo
            tabuleiro[x-1][y] = tabuleiro[x][y]
            tabuleiro[x][y+1] = tabuleiro[x][y]
        if formato == 5 and dentro_tab(x-1,y) and dentro_tab(x+1,y): #Horizontal
            tabuleiro[x-1][y] = tabuleiro[x][y]
            tabuleiro[x+1][y] = tabuleiro[x][y]
        if formato == 6 and dentro_tab(x,y-1) and dentro_tab(x,y+1): #Vertical
            tabuleiro[x][y-1] = tabuleiro[x][y]
            tabuleiro[x][y+1] = tabuleiro[x][y]
            
        for casa in territorio:            #Aumenta o território inicial do jogador, caso o primeiro número tenha iguais pegados a ele
            if tabuleiro[casa[1]+1][casa[0]] == tabuleiro[casa[1]][casa[0]]:
                if not [casa[0],casa[1]+1] in territorio:
                    territorio.append([casa[0],casa[1]+1])
            if tabuleiro[casa[1]][casa[0]+1] == tabuleiro[casa[1]][casa[0]]:
                if not[casa[0]+1,casa[1]] in territorio:
                    territorio.append([casa[0]+1,casa[1]])

        global territorio_inimigo
        territorio_inimigo=[[len(tabuleiro)-1,len(tabuleiro)-1]]        
        for casa in territorio_inimigo:   #Aumenta o território inicial da IA, caso o seu primeiro número tenha iguais pegados a ele
            if tabuleiro[casa[1]-1][casa[0]] == tabuleiro[casa[1]][casa[0]]:
                if not [casa[0],casa[1]-1] in territorio_inimigo:
                    territorio_inimigo.append([casa[0],casa[1]-1])
            if tabuleiro[casa[1]][casa[0]-1] == tabuleiro[casa[1]][casa[0]]:
                if not [casa[0]-1,casa[1]] in territorio_inimigo:
                    territorio_inimigo.append([casa[0]-1,casa[1]])
   

def print_tab():              #Escreve o tabuleiro na shell do python, onde é então permitido jogar, num formato legível
    for y in range(len(tabuleiro)):
        print(' ')
        for x in range(len(tabuleiro)):
            print((tabuleiro[y][x]), end= ' ')

def unico_jogador():          #Função que cria o modo de Único Jogador
    print('Você está no canto superior esquerdo com o número',tabuleiro[0][0])  #Indica onde começa o nosso jogo
    
    while njogadas > 0:       #Verifica se ainda temos jogadas disponíveis
          print_tab()
          print('')
          print('Número de jogadas restantes:',njogadas)
          print('Qual o número que quer apoderar?')
          n = input()
          jogada(n)   #Função que faz a jogada
          if len(territorio) == len(tabuleiro)*len(tabuleiro):   #Verifica se completámos o jogo. Se sim, mostra mensagem de vitória e acaba sai do loop
              print_tab()
              print('')
              print('Parabéns!!!')
              print('Ganhou o jogo em',30 - njogadas,'jogadas!!')
              parar = input('Pressione qualquer tecla para sair...')
              break
    if njogadas <= 0:   #Termina o jogo quando o número de jogadas acaba
        
        print_tab()
        print('')
        print('Temos pena, mas perdeu o jogo!')
        parar = input('Pressione qualquer tecla para sair...')
        
def IA():
    print('')
    print('Você está no canto superior esquerdo com o número',tabuleiro[0][0],'e o computador está no canto inferior direito com o número',tabuleiro[len(tabuleiro)-1][len(tabuleiro)-1],'.')
    while len(territorio)+len(territorio_inimigo) < len(tabuleiro)*len(tabuleiro): #Enquanto a soma de casas de ambos jogadores for menor que a área do tabuleiro, ou seja,
        print_tab()                                                                #Enquanto ainda houver territorio sem dono
        print('')
        print('Qual o número que quer apoderar?')
        n = input()
        if jogada(n)!= False:           #If executa a função na mesma. se a função por acaso retornar False, é porque o input é errado e a jogada do inimigo não será executada
            jogada_inimigo()
    if len(territorio)>len(territorio_inimigo): #Mensagem de vitória
        print_tab()
        print('')
        print('Você ganhou contra o computador!! Parabéns!!')
        print('Você:',len(territorio))
        print('Computador:',len(territorio_inimigo))
        parar = input('Pressione qualquer tecla para sair...')
    elif len(territorio_inimigo)>len(territorio): #Mensagem de derrota
        print_tab()
        print('')
        print('Temos pena mas perdeu o jogo contra o computador... Tente novamente!')
        print('Você:',len(territorio))
        print('Computador:',len(territorio_inimigo))
        parar = input('Pressione qualquer tecla para sair...')

def jogada(n):
    if n not in ['1','2','3','4','5','6'] or int(n) == tabuleiro[0][0]: #Quando se usa tabuleiro[0][0] nestas situações, refere-se ao número atual do jogador.    
        print('JOGADA INVÁLIDA, SELECIONE UM NÚMERO VÁLIDO.')   
        return False                                #Se o input não for um número válido ou se for repetido à jogada anterior (tabuleiro[0][0]), função para e retorna False
    if op_jogo == '2':
        if int(n) == tabuleiro[len(tabuleiro)-1][len(tabuleiro)-1]:
            print('JOGADA INVÁLIDA, COR PERTENCE AO COMPUTADOR..')
            return False                #Verificação extra para, se contra computador, o input não pode ser igual ao input anterior do computador.
    global njogadas
    njogadas -= 1   #Número de jogadas restantes diminui.
    for casa in territorio:                     #A própria alteração do tabuleiro
        tabuleiro[casa[1]][casa[0]] = int(n)    #O tabuleiro mudará para as casas que fazem parte do território para o input do utilizador
        #É DE NOTAR QUE, para a jogada do computador, este n vai ser extremamente importante
    for casa in territorio:
        if dentro_tab(casa[0]-1,casa[1]) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]][casa[0]-1]: #Verifica se uma casa existe à esquerda de uma casa no territorio e se é igual à própria
            if not [casa[0]-1,casa[1]] in territorio: #Se esta casa do lado esquerdo já existir no territorio, entao não se faz nada
                territorio.append([casa[0]-1,casa[1]]) #Mas como não existe, essas coordenadas serão adicionados ao território.

        if dentro_tab(casa[0],casa[1]-1) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]-1][casa[0]]: #O mesmo para o lado de cima
            if not [casa[0],casa[1]-1] in territorio:
                territorio.append([casa[0],casa[1]-1])

        if dentro_tab(casa[0]+1,casa[1]) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]][casa[0]+1]: #O mesmo para o lado direito
            if not [casa[0]+1,casa[1]] in territorio:
                territorio.append([casa[0]+1,casa[1]])

        if dentro_tab(casa[0],casa[1]+1) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]+1][casa[0]]: #O mesmo para o lado de baixo
            if not [casa[0],casa[1]+1] in territorio:
                territorio.append([casa[0],casa[1]+1])

def jogada_inimigo():
#********************************************************************************************************
    global conta_n
    conta_n = dict()        #Este dicionário vai guardar a quantidade de casas adicionadas ao territorio para cada número...
    for i in range(1,7):    #Para depois ver qual o maior número de casas e assim o computador escolher esse número para mudar, daí este for, que percorre todos o números
        tabuleiro_teste= [] #Tabuleiro que vai ser usado como teste para cada número para o original não sofrer alterações
        territorio_teste = [] #Territorio que vai ser usado como teste para o original não sofrer alterações
        tabuleiro_teste = deepcopy(tabuleiro) #Função deepcopy, do módulo copy, copia a lista (e as listas dentro desta) para o tabuleiro teste e assim não se torna um espelho do tabuleiro
        #Se não fosse esta função, qualquer alteração que fizessemos no tabuleiro_teste, iria mostrar-se no tabuleiro original
        if i == tabuleiro_teste[0][0]: #Se o número de teste for o mesmo do jogador, salta para outro número   
            continue
        if i == tabuleiro_teste[len(tabuleiro_teste)-1][len(tabuleiro_teste)-1]: #Se o número de teste for o que o computador está a usar agora, salta para outro.
            continue
        for casa in territorio_inimigo: #Mesmo método do que o que está na função jogada()
            tabuleiro_teste[casa[1]][casa[0]] = i
        for casa in territorio_inimigo:
            if dentro_tab(casa[0]-1,casa[1]) and tabuleiro_teste[casa[1]][casa[0]] == tabuleiro_teste[casa[1]][casa[0]-1]:
                if not [casa[0]-1,casa[1]] in territorio_inimigo and not [casa[0]-1,casa[1]] in territorio_teste:
                    territorio_teste.append([casa[0]-1,casa[1]]) #Mas adiciona ao territorio_teste

            if dentro_tab(casa[0],casa[1]-1) and tabuleiro_teste[casa[1]][casa[0]] == tabuleiro_teste[casa[1]-1][casa[0]]:
                if not [casa[0],casa[1]-1] in territorio_inimigo and not [casa[0],casa[1]-1] in territorio_teste:
                    territorio_teste.append([casa[0],casa[1]-1])

            if dentro_tab(casa[0]+1,casa[1]) and tabuleiro_teste[casa[1]][casa[0]] == tabuleiro_teste[casa[1]][casa[0]+1]:
                if not [casa[0]+1,casa[1]] in territorio_inimigo and not [casa[0]+1,casa[1]] in territorio_teste:
                    territorio_teste.append([casa[0]+1,casa[1]])

            if dentro_tab(casa[0],casa[1]+1) and tabuleiro_teste[casa[1]][casa[0]] == tabuleiro_teste[casa[1]+1][casa[0]]:
                if not [casa[0],casa[1]+1] in territorio_inimigo and not [casa[0],casa[1]+1] in territorio_teste:
                    territorio_teste.append([casa[0],casa[1]+1])

        for casa in territorio_teste:           #Ao tabuleiro_teste, altera todos as casas no territorio_teste por uma string "conta"...
            tabuleiro_teste[casa[1]][casa[0]] = 'conta'
        for y in range(len(tabuleiro_teste)):
            for x in range(len(tabuleiro_teste)):
                if tabuleiro_teste[y][x] == 'conta':
                    if i not in conta_n:        #...E conta quantas vezes aparece essa string e guarda no dicionario, com a chave do número
                        conta_n[i] = 1
                    else:
                        conta_n[i] += 1

    if conta_n == {}: #Se por acaso não houver nenhum número para o qual seja possível mudar...
        while True:
            nini = random.randint(1, 6) #Então nini (a variável que será o número que o AI escolherá) vai ser um número ao calhas
            if nini != tabuleiro[0][0]: #Mas este número não pode ser o do jogador
                break
    else:
        #Aqui escolhe a chave com valor maior, que muda mais casas no tabuleiro, o que tem maior território
        v = list(conta_n.values())
        k = list(conta_n.keys())
        nini = k[v.index(max(v))] #nini é o numero que o AI vai apoderar

#********************************************************************************************************
        
    #Agora o territorio inimigo fica com o nini e é o mesmo método do que na função jogada() mas com o territorio_inimigo.
    for casa in territorio_inimigo:
        tabuleiro[casa[1]][casa[0]] = nini
    for casa in territorio_inimigo:
        if dentro_tab(casa[0]-1,casa[1]) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]][casa[0]-1]:
            if not [casa[0]-1,casa[1]] in territorio_inimigo:
                territorio_inimigo.append([casa[0]-1,casa[1]])

        if dentro_tab(casa[0],casa[1]-1) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]-1][casa[0]]:
            if not [casa[0],casa[1]-1] in territorio_inimigo:
                territorio_inimigo.append([casa[0],casa[1]-1])

        if dentro_tab(casa[0]+1,casa[1]) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]][casa[0]+1]:
            if not [casa[0]+1,casa[1]] in territorio_inimigo:
                territorio_inimigo.append([casa[0]+1,casa[1]])

        if dentro_tab(casa[0],casa[1]+1) and tabuleiro[casa[1]][casa[0]] == tabuleiro[casa[1]+1][casa[0]]:
            if not [casa[0],casa[1]+1] in territorio_inimigo:
                territorio_inimigo.append([casa[0],casa[1]+1])
    
def dentro_tab(casaX, casaY):           #Esta função verifica se as coordenadas no argumento pertencem ou não ao tabuleiro
    #Esta função existe para que não ocorra o erro "index out of range" quando usamos listas na função jogada() e adiante.
    if casaX > len(tabuleiro)-1 or casaX < 0:
        return False
    if casaY > len(tabuleiro)-1 or casaY < 0:
        return False
    return True

#NOTA: AS PRÓXIMAS FUNÇÕES NÃO SÃO USADAS NA FUNÇÃO jogar()
#Servem apenas para fins de teste e está incompleto, por falta de conhecimento sobre a área gráfica.
def gui():              #Esta função permite ver o tabuleiro com cores, tal como no jogo zyan drench, flood it ,etc.
    labels = list()     #Para testar esta função, quando executar o jogo, basta fazer Ctrl+D , introduzir gerar_tab() e de seguida gui(). Isto mostrará o tabuleiro em cores
    root = Tk()         #Mas não irá executar o jogo
    tab_cores()
    for y in range(len(tabuleiro)):
        for x in range(len(tabuleiro)):
           Label(bg=tabuleiro_cores[x][y], width=1, height=1).grid(row=y, column=x)
    root.mainloop()    
    
def tab_cores():            #Esta função cria um tabuleiro novo onde os números são substituídos por cores correspondentes.
    cores = {1:'light blue', 2:'green', 3:'pink', 4:'purple', 5:'red', 6:'gold'}
    for y in range(len(tabuleiro)):
        tabuleiro_cores.append([])
        for x in range(len(tabuleiro)):
            tabuleiro_cores[y].append(cores[tabuleiro[x][y]])
    
jogar()            
