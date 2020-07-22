import random

def read_file(file):
	lista_palavras = []
	s = open(file)
	for i,line in enumerate(s): # percorrer as linhas do ficheiro
		if i == 0:
			num_linhas,num_colunas = line.split(" ")
		else:
			lista_palavras.append(line.strip())
	return lista_palavras,num_linhas,num_colunas

def sopa_letras1(num_linhas,num_colunas):     #origina uma sopa de letras comletamente ao acaso
	lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
	lista_letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	sopa_letras = []
	indice = ""
	num_linhas,num_colunas = int(num_linhas),int(num_colunas)
	while num_linhas != 0:
		new_line1 = []
		new_line = ""
		for i in range(num_colunas):
			number = random.randint(1,26)
			for l,numero in enumerate(lista_numeros):
				if numero == number:
					indice = l
			letter = lista_letras[indice]
			new_line += letter
		new_line1.append(new_line)
		sopa_letras.append(new_line1)
		num_linhas-=1
	return sopa_letras

def lista_palavras1(lista_palavras):        #ordena a lista de palavras pelas palvras maiores para as mais pequenas
	maior_palavras = []
	i = len(lista_palavras)
	print(i)
	while i != 0:
		maior_palavra = 0
		better_word = ""
		for word in lista_palavras:
			if len(word) > maior_palavra and not word in maior_palavras:
				maior_palavra = len(word)
				better_word = word
		maior_palavras.append(better_word)
		print(maior_palavras)
		i-=1
	return maior_palavras

def transformar_letra(sopa_letras,coordenada,letra):
	for i,linha in enumerate(sopa_letras):
		if i+1 == coordenada[0]:
			for l,coluna in enumerate(linha[0]):
				if l+1 == coordenada[1]:
					#letter3 = linha[0].replace(linha[0][l],letra,1)
					letter3 = linha[0][:l] + letra + linha[0][l+1:]
					sopa_letras[i] = [letter3]
	return sopa_letras
#                                                                    
def verificacao_esq_dir(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1,coordenada2 + i) in aux:
			return True
	return False

def verificacao_dir_esq(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1,coordenada2-i) in aux:
			return True
	return False

def verificacao_cima_baixo(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1+i,coordenada2) in aux:
			return True
	return False

def verificacao_baixo_cima(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1-i,coordenada2) in aux:
			return True
	return False

def verificacao_dg_dir_cima(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1-i,coordenada2+i) in aux:
			return True
	return False

def verificacao_dg_dir_baixo(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1+i,coordenada2+i) in aux:
			return True
	return False

def verificacao_dg_esq_cima(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1-i,coordenada2-i) in aux:
			return True
	return False

def verificacao_dg_esq_baixo(coordenada1,coordenada2,word,aux):
	for i in range(len(word)):
		if (coordenada1+i,coordenada2-i) in aux:
			return True
	return False

file = input("Ficheiro: ")
lista_palavras,num_linhas,num_colunas = read_file(file)
lista_palavras2 = lista_palavras1(lista_palavras)
print(lista_palavras2)
num_linhas,num_colunas = int(num_linhas),int(num_colunas)
sopa_letras = sopa_letras1(num_linhas,num_colunas)
while True: 
	boolean = True                                   # caso ocorra alguma situação em que não dê para introduzir a palvra  na sopa, a variavel passa a false... caso no fim ela esteja em false, repete se tudo de novo até dar
	aux = []       
	coordenada1,coordenada2 = 0,0            
	for word in lista_palavras2:                               
		letras = len(word)
		number_metodo = random.randint(1,8)          # há 8 metodos (direita-esquerda, esquerda-direita, baixo-cima, cima-baixo etc...). Para cada palavra, o metodo é aleatorio
		print(number_metodo)
		if number_metodo == 1:                                                                                  # se o metodo for esquerda - direita
			coordenada1,coordenada2 = random.randint(1,num_linhas),random.randint(1,(num_colunas-letras))  # coordenadas da primeira letra da palavra   (num_colunas-letras) pois como o sentido é este, se a palavra tiver 3 letras e se calhar sendo na ultima coluna, não haveria espaço para as restantes letras
			t = 0
			while verificacao_esq_dir(coordenada1,coordenada2,word,aux) == True:                           # enquanto as coordenadas das letras da palavra estiverem na lista aux, essas coordenadas já foram usadas por isso ´necessario definir novas coordenadas
				coordenada1,coordenada2 = random.randint(1,num_linhas),random.randint(1,(num_colunas-letras))
				if t==40:                                                                                   # o problema está aqui
					print("lala")                                                                            # o problema está aqui
					#print(number_metodo)                                                                    # o problema está aqui
					#number_metodo = random.randint(1,8)
					if boolean == True:
						boolean == False                                                      # o problema está aqui
					break                                                                                 # o problema está aqui
				if  verificacao_esq_dir(coordenada1,coordenada2,word,aux) == False: # saida do ciclo
					break
				t+=1
			for i,letter in enumerate(word):  # vai se transformar uma letra de cada vez
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1,coordenada2+i),letter.upper()) #coordenada2 + i pois á medida que vamos transformando a palvra, tem de se ir avançando na coluna caso contrario estar se ia a transformar sempre a mesma letra e se a palavra ou se azul, apenas iria ficar a ultima letra ou seja l
				aux.append((coordenada1,coordenada2+i))                                                # tem de se ir adicionando á lista auxiliar para que na palavra a seguir não se repitam as posições
			print(sopa_letras)
		
	# o resto é igual só que para as outras direções
		elif number_metodo == 2:                                                                                            #se o metodo for direita - esquerda
			coordenada1,coordenada2 = random.randint(1,num_linhas),random.randint(letras,num_colunas)
			t = 0
			while verificacao_dir_esq(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(1,num_linhas),random.randint(letras,num_colunas)
				if t==40:
					if boolean == True: 
						boolean = False
					break
				if verificacao_dir_esq(coordenada1,coordenada2,word,aux) == False:
					break
				t+=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1,coordenada2-i),letter.upper())
				aux.append((coordenada1,coordenada2-i))
			print(sopa_letras)

		elif number_metodo == 3:
			coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(1,num_colunas)
			t = 0
			while verificacao_cima_baixo(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(1,num_colunas)
				if t==40:
					if boolean == True:
						boolean = False 
					break
				if verificacao_cima_baixo(coordenada1,coordenada2,word,aux) == False:
					break
				t+=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1+i,coordenada2),letter.upper())
				aux.append((coordenada1+i,coordenada2))
			print(sopa_letras)

		elif number_metodo == 4:
			coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(1,num_colunas)
			t = 0
			while verificacao_baixo_cima(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(1,num_colunas)
				if t==40:
					if boolean == True:
						boolean = False
					break
				if verificacao_baixo_cima(coordenada1,coordenada2,word,aux) == False:
					break
				t+=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1-i,coordenada2),letter.upper())
				aux.append((coordenada1-i,coordenada2))
			print(sopa_letras)

		elif number_metodo == 5:
			coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(1,(num_linhas-letras))
			t = 0
			while verificacao_dg_dir_cima(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(1,(num_linhas-letras))
				if t==40:
					if boolean == True:
						boolean = False 
					break
				if verificacao_dg_dir_cima(coordenada1,coordenada2,word,aux) == False:
					break
				t+=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1-i,coordenada2+i),letter.upper())
				aux.append((coordenada1-i,coordenada2+i))
			print(sopa_letras)

		elif number_metodo == 6:
			coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(1,(num_linhas-letras))
			t=0
			while verificacao_dg_dir_baixo(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(1,(num_linhas-letras))
				if t==40:
					if boolean == True:
						boolean = False 
					break
				if verificacao_dg_dir_baixo(coordenada1,coordenada2,word,aux) == False:
					break
				t+=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1+i,coordenada2+i),letter.upper())
				aux.append((coordenada1+i,coordenada2+i))
			print(sopa_letras)

		elif number_metodo == 7:
			coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(letras,num_colunas)
			t=0
			while verificacao_dg_esq_cima(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(letras,num_linhas),random.randint(letras,num_colunas)
				if t==40:
					if boolean == True:
						boolean = False
					break
				if verificacao_dg_esq_cima(coordenada1,coordenada2,word,aux) == False:
					break
				t += 1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1-i,coordenada2-i),letter.upper())
				aux.append((coordenada1-i,coordenada2-i))
			print(sopa_letras)

		elif number_metodo == 8:
			coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(letras,num_colunas)
			t=0
			while verificacao_dg_esq_baixo(coordenada1,coordenada2,word,aux) == True:
				coordenada1,coordenada2 = random.randint(1,(num_linhas-letras)),random.randint(letras,num_colunas)
				if t==40:
					if boolean == True:
						boolean = False
					break
				if verificacao_dg_esq_baixo(coordenada1,coordenada2,word,aux) == False:
					break
				t +=1
			for i,letter in enumerate(word):
				print(letter)
				sopa_letras = transformar_letra(sopa_letras,(coordenada1+i,coordenada2-i),letter.upper())
				aux.append((coordenada1+i,coordenada2-i))
			
			#print(sopa_letras)
	#print(boolean)
	if boolean == True:
		#print("lele")
		break
	else:
		sopa_letras = sopa_letras1(num_linhas,num_colunas)

print(sopa_letras)
#print(aux)
number_of_words = len(lista_palavras)
#print(lista_palavras2)

fout = open("sopa_letras.txt","w")
fout.write("{}\n".format(number_of_words))
fout.close()
fout = open("sopa_letras.txt","a")
for word in lista_palavras:
	fout.write("{}\n".format(word))
for i in sopa_letras:
	for l in i:
		fout.write("{}\n".format(l))
fout.close()
