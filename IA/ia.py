#!/usr/bin/env python3
import sys
import math
import random
tabuleiro=[ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
tabuleiro_aux=[ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
deposito=[0, 0]
deposito_aux=[0, 0]


def jogar():
    global op_jogo
    global op_tab
    global bestMove
    op_jogo = 5
    op_tab = 3
    bestMove = -1
    print('Bem Vindo ao Jogo!')
    while int(op_jogo) not in [0,1,2,3,4]:    #Pergunta se queremos jogar sozinhos, contra AI ou sair. Repete pergunta até input ser válido
        print('0 - Sair')
        print('1 - Indicar melhor jogada')
        print('2 - VS_IA')
        print('3 - IA_VS_IA(Torneio)')
        print('4 - Jogo atraves de um ciclo')
        op_jogo = input()
        if int(op_jogo) not in [0,1,2,3,4]:   #Descarta as opções que não estejam no menu
            print('Selecione uma opção válida')
    if op_jogo == '0':
        return
    if op_jogo == '1':
        while int(op_tab) not in [0,1,2]:    
            print('0 - 5seg')
            print('1 - 15seg')
            print('2 - 30seg')
            op_tab = input()
            if int(op_tab) not in [0,1,2]:   #Descarta as opções que não estejam no menu
                print('Selecione uma opção válida')
        melhor_jogada(int (op_tab), bestMove)
    if op_jogo == '2':
        while int(op_tab) not in [0,1,2]:    
            print('0 - facil')
            print('1 - medio')
            print('2 - dificil')
            op_tab = input()
            if int(op_tab) not in [0,1,2]:   #Descarta as opções que não estejam no menu
                print('Selecione uma opção válida')
        while int(op_jogo) not in [0,1]:    
            print('0 - Começa o jogador')
            print('1 - Começa a IA')
            op_jogo = input()
            if int(op_tab) not in [0,1]:   #Descarta as opções que não estejam no menu
                print('Selecione uma opção válida')
        VS_IA(1,int (op_jogo), int (op_tab),bestMove)
    if op_jogo == '3':
        IA_VS_IA(0, bestMove,1)
        IA_VS_IA(0, bestMove,0)
        IA_VS_IA(1, bestMove,1)
        IA_VS_IA(1, bestMove,0)
        IA_VS_IA(2, bestMove,1)
        IA_VS_IA(2, bestMove,0)
    if op_jogo == '4':
        while int(op_jogo) not in [0,1]:    
            print('0 - Começa o jogador')
            print('1 - Começa a IA')
            op_jogo = input()
            if int(op_jogo) not in [0,1]:   #Descarta as opções que não estejam no menu
                print('Selecione uma opção válida')
        VS_IA(0,int (op_jogo), 2,bestMove)

 

def print_tabuleiro():
    print("    ")
    print("----------------------")
    print("    ", end = "")
    for a in range(11,5,-1):
        print(tabuleiro[a], end =" ")
    print("")
    print(deposito[1],"|              |",deposito[0],end = "")
    print("")
    print("    ", end = "")
    for a in range(0,6,1):
        print(tabuleiro[a], end =" ")

def checkwin():
    if(deposito[0] > 24):
        print("Jogador ganhou")
        return 1
    if(deposito[1] > 24):
        print("IA ganhou")
        return 1
    return 0

def checkwin3():
    if(deposito_aux[0] > 24):
        repor()
        return 1
    if(deposito_aux[1] > 24):
        repor()
        return 1
    return 0

def checkwin2():
    if(deposito[0] > 24):
        print("IA2 ganhou")
        repor()
        return 1
    if(deposito[1] > 24):
        print("IA1 ganhou")
        repor()
        return 1
    return 0

def repor():
    for i in range(0,11,1):
        tabuleiro[i]=4
        tabuleiro_aux[i]=4
    deposito[0]=0
    deposito[1]=0
    deposito_aux[0]=0
    deposito_aux[1]=0

def melhor_jogada(P, bestMove):
    i=0
    print("Esta opção irá indicar a melhor jogada para o jogador da parte do tabuleiro de cima(jogador2)")
    print("Insira o estado do tabuleiro(sentido contrario ao ponteiro do relogio a começar na posição mais a esquerda em baixo), um numero de cada vez")
    while i<12:
        numero = input()
        tabuleiro[i] = int(numero)
        i=i+1
    print("Insira o estado do depositósito da direita(jogador1)")
    numero = input()
    deposito[0]=int(numero)
    print("Insira o estado do depositósito da esquerda(jogador2)")
    numero = input()
    deposito[1]=int(numero)
    print_tabuleiro()
    move=IA_play(P, bestMove)
    print_tabuleiro()
    print("Melhor jogada será: ",move-5)


def player_play():
    print("")
    if tabuleiro[0] == 0 and tabuleiro[1] == 0 and tabuleiro[2] == 0 and tabuleiro[3] == 0 and tabuleiro[4] == 0 and tabuleiro[5] == 0:
        deposito[1] = tabuleiro[6]+tabuleiro[7]+tabuleiro[8]+tabuleiro[9]+tabuleiro[10]+tabuleiro[11]+deposito[1]
        tabuleiro[6] = 0
        tabuleiro[7] = 0
        tabuleiro[8] = 0
        tabuleiro[9] = 0
        tabuleiro[10] = 0
        tabuleiro[11] = 0
        print("Sem jogadas disponiveis")
        return 0
    print("Sua vez de jogar:", end = "")
    n = 0
    while int(n) not in [1,2,3,4,5,6]:   
        n = int(input())
        if int(n) not in [1,2,3,4,5,6]:   
            print('Selecione uma opção válida1')
    n = n-1
    if(tabuleiro[n]==0):
        print('Selecione uma opção válida2')
        player_play()
        return 0
    if(tabuleiro[n]==1):
        for a in range(0,6,1):
            if tabuleiro[a]> 1:
                print('Nao pode selecionar um buraco com apenas 1 semente neste momento')
                print('Selecione uma opção válida3')
                player_play()
                return 0
    m = tabuleiro[n]
    tabuleiro[n] = 0
    while m > 0:
        n = n + 1
        if n > 11:
            n = 0
        tabuleiro[n] = tabuleiro[n] + 1
        m = m - 1
    
    comer = True
    while comer:
        if(tabuleiro[n]<4 and tabuleiro[n]>1 and n > 5):
            deposito[0] = deposito[0] + int(tabuleiro[n])
            tabuleiro[n] = 0
            n = n - 1
        else:
            comer = False
    return 0


def possible_moves_ia():
    
    possiveis = [6,7,8,9,10,11]
    for a in range(6,12,1):
        if(tabuleiro[a]==0):
            possiveis.remove(a)
        elif(tabuleiro[a]==1):
            b = a
            for a in range(6,12,1):
                if tabuleiro[a]> 1:
                    possiveis.remove(b)
                    break
    return possiveis

def possible_moves_player():
    possiveis = [0,1,2,3,4,5]
    for a in range(0,6,1):
        if(tabuleiro[a]==0):
            possiveis.remove(a)
        elif(tabuleiro[a]==1):
            b = a
            for a in range(0,6,1):
                if tabuleiro[a]> 1:
                    possiveis.remove(b)
                    break
    return possiveis


def make_move_aux_ia(move):
    #fazer a jogada num tabuleiro auxiliar
    a = deposito_aux[0]
    m = tabuleiro_aux[move]
    tabuleiro_aux[move] = 0
    while m > 0:
        move = move + 1
        if move > 11:
            move = 0
        tabuleiro_aux[move] = tabuleiro_aux[move] + 1
        m = m - 1
    comer = True
    while comer:
        if(tabuleiro_aux[move]<4 and tabuleiro_aux[move]>1 and move < 6 and move > -1):
            deposito_aux[0] = deposito_aux[0] + int(tabuleiro_aux[move])
            tabuleiro_aux[move] = 0
            move = move - 1
        else:
            comer = False
    pontos = deposito_aux[0] - a
    return pontos

def make_move_aux_player(move):
    #fazer a jogada num tabuleiro auxiliar
    a =  deposito_aux[1]
    m = tabuleiro_aux[move]
    tabuleiro_aux[move] = 0
    while m > 0:
        move = move + 1
        if move > 11:
            move = 0
        tabuleiro_aux[move] = tabuleiro_aux[move] + 1
        m = m - 1
    comer = True
    while comer:
        if(tabuleiro_aux[move]<4 and tabuleiro_aux[move]>1 and move > 6 and move < 11):
            deposito_aux[1] = deposito_aux[1] + int(tabuleiro_aux[move])
            tabuleiro_aux[move] = 0
            move = move - 1
        else:
            comer = False
    pontos = deposito_aux[1] - a
    return pontos

def make_move(move):
    #fazer a jogada no tabuleiro
    m = tabuleiro[move]
    tabuleiro[move] = 0
    while m > 0:
        move = move + 1
        if move > 11:
            move = 0
        tabuleiro[move] = tabuleiro[move] + 1
        m = m - 1
    comer = True
    while comer:
        if(tabuleiro[move]<4 and tabuleiro[move]>1 and move < 6 and move > -1):
            deposito[1] = deposito[1] + int(tabuleiro[move])
            tabuleiro[move] = 0
            move = move - 1
        else:
            comer = False
    return 0



def IA_play(depth, bestMove):
        if depth == 0:
            d = 8
        if depth == 1:
            d = 9
        if depth == 2:
            d = 10

        move = minimax(d, False, bestMove)

        make_move(move)

        bestMove = -1
        return move
        
      
  
def minimax (depth, maximizingPlayer, bestMove):
    
    if depth == 0 or checkwin3() == 1:
        return deposito_aux[1]-deposito[1]

    if maximizingPlayer:
        bestScore = -math.inf
        a = possible_moves_player()
        for move in a:
            make_move_aux_player(move)
            score = minimax(depth - 1, False, bestMove)
            if(score > bestScore):
                bestScore = score
                bestMove = move
        return bestMove


    else:
        bestScore = +math.inf
        b = possible_moves_ia()
        for move in b:
            make_move_aux_ia(move)
            score = minimax(depth - 1, True, bestMove)
            if(score < bestScore):
                bestScore = score
                bestMove = move
        return bestMove


def VS_IA(L, ordem, depth, bestMove):
    print_tabuleiro()
    n=0
    p = 1
    if ordem == 0:
        while p == 1:
            player_play()
            if L == 1:
                print_tabuleiro()
            if checkwin() == 1:
                return 0
            n=IA_play(depth, bestMove)
            print("Jogado pela IA:",n-6)
            if L == 1:
                print_tabuleiro()
            if checkwin() == 1:
                return 0
    if ordem == 1:
        while p == 1:
            n=IA_play(depth, bestMove)
            print("Jogado pela IA:",n-6)
            if L == 1:
                print_tabuleiro()
            if checkwin() == 1:
                return 0
            player_play()
            if L == 1:
                print_tabuleiro()
            if checkwin() == 1:
                return 0


def IA_VS_IA(depth, bestMove,L):
    p = 1
    if L==1:
        while p == 1:
            IA_play(depth, bestMove)
            if checkwin2() == 1:
                return 0
            IA2_play()
            if checkwin2() == 1:
                return 0
    if L==0:
        while p == 1:
            IA2_play()
            if checkwin2() == 1:
                return 0
            IA_play(depth, bestMove)
            if checkwin2() == 1:
                return 0



jogar()

    
