#encoding:utf8

import random

def converter(nome):
	for i in range(2,8):
		if nome == str(i):
			valor = i
	if nome == "valete":
		valor = 8
	elif nome == "dama":
		valor = 9
	elif nome == "rei":
		valor = 10
	elif nome == "ás":
		valor = 11
	return valor


def pontuacoes(pont_dealer,pont_jogador):
	if pont_jogador > 21:
		return 0
	if pont_dealer > 21:
		return 1

	if pont_jogador < pont_dealer:
		return 0
	elif pont_dealer < pont_jogador:
		return 1

def cartas():
	chave = ""
	for i in range(2):
		number = random.randint(2,11)
		if number == 8:
			carta = "valete"
		elif number == 9:
			carta = "dama"
		elif number == 10:
			carta = "rei"
		elif number == 11:
			carta = "ás"
		else:
			carta = str(number)
		if i == 0:
			chave = carta
		elif i == 1:
			chave = chave + "," + carta
	return chave

def avaliar(string):
	pont_total = 0
	aux = []
	item = string.split(",")
	for l in item:
		if l == "ás":
			aux.append(True)
	if len(aux) > 1:
		pont_total = 11 + (len(aux)-1)
		for i in item:
			if i != "ás":
				pontuacao = converter(i)
				pont_total += pontuacao
	else:
		for card in item:
			pontuacao = converter(card)
			pont_total += pontuacao
	return pont_total

def pedir_carta(chave_jogador):
	number = random.randint(2,11)
	if number == 8:
		carta = "valete"
	elif number == 9:
		carta = "dama"
	elif number == 10:
		carta = "rei"
	elif number == 11:
		carta = "ás"
	else:
		carta = str(number)
	chave_jogador = chave_jogador + "," + carta
	return chave_jogador

vitorias_casa = 0
vitorias_jogador = 0

boolean = True
while boolean != False:
	resposta2 = input("Quer realizar um jogo? (S/N) ")
	if resposta2 == "S":
		boolean = True
	else:
		boolean = False
	if boolean == False:
		break

	chave_jogador = cartas()
	print("Sua chave: {}".format(chave_jogador))

	resposta = ""
	while resposta != "N":
		resposta = input("Quer pedir mais uma carta? (S/N) ")
		if resposta == "N":
			break
		chave_jogador = pedir_carta(chave_jogador)
		print("A sua chave passou a ser {}".format(chave_jogador))



	chave_dealer = cartas()
	#print(chave_dealer)

	pont_jogador = avaliar(chave_jogador)
	pont_dealer = avaliar(chave_dealer)
	while pont_dealer < pont_jogador and pont_dealer <= 21:
		chave_dealer = pedir_carta(chave_dealer)
		pont_dealer = avaliar(chave_dealer)
		if pont_dealer > pont_jogador:
			break
		if pont_dealer > 21:
			break
	print(chave_dealer)




	if pont_jogador == pont_dealer:
		print("Temos um empate")
	else:
		vencedor = pontuacoes(pont_dealer,pont_jogador)
		if vencedor == 0:
			print("O vencedor é o dealer!")
			vitorias_casa += 1
		elif vencedor == 1:
			print("O vencedor é o jogador!")
			vitorias_jogador += 1
		print("Número de vitorias da casa: {} \nNúmero de vitorias do jogador: {} \n".format(vitorias_casa,vitorias_jogador))
