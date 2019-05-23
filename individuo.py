import random
import copy
import math


# Valores definidos no problema #
matriz_importancia = [[10, 8, 6, 5, 7, 8, 6, 9, 6, 10], [10, 10, 4, 9, 7, 6, 6, 8, 7, 10], [5, 6, 8, 1, 5, 2, 4, 3, 5, 7]]
custo = [60, 40, 40, 30, 20, 20, 25, 70, 50, 20]
risco = [3, 6, 2, 6, 4, 8, 9, 7, 6, 6]
posicao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Funcao Score #
def score(importancia, P, release_requisito, risco):
	S = 0
	for i in range(0, 10):
		if release_requisito[i] != 0:
			yi = 1
			S += (importancia[i] *(P - release_requisito[i] + 1) - risco[i] * release_requisito[i]) * yi 
		else:
			S += 0
	

	return S

def crossover(cromo1, cromo2, ponto_de_corte):
	filho = [0] * 10

	for m in range(0, ponto_de_corte):
		filho[m] = cromo1[m]
	for n in range(ponto_de_corte, 10):
		filho[n] = cromo2[n]



	return filho


# Variaveis a serem utilizadas #
P = int(input("Informe uma quantidade de individuos: "))
G = int(input("Informe a quantidade de geracoes: "))
importancia_total = [0] * 10
cromossomo = [0] * 10
individuo = [[0], 0]
populacao = [0] * P
custo_release1 = 0
custo_release2 = 0
custo_release3 = 0
cont_populacao = 0
cont_geracao = 0


for i in range(0, 3):
	for j in range(0, 10):
		if (i == 0):
			importancia_total[j] += matriz_importancia[i][j] * 3                ##############################
		elif (i == 1):                                                          #                            #
			importancia_total[j] += matriz_importancia[i][j] * 4                #   Matriz de Importancias   #
		elif (i == 2):                                                          #                            #
			importancia_total[j] += matriz_importancia[i][j] * 2                ##############################



# GERACAO DE P INDIVIDUOS #


while (cont_populacao < P):

	i = random.choice(posicao)

	while(custo_release1 + custo[i] <= 125):
		k = i
		cromossomo[i] = 1
		
		custo_release1 += custo[i]

		if(k in posicao):
			posicao.remove(k)
		
		i = random.choice(posicao)


	i = random.choice(posicao)

	while(custo_release2 + custo[i] <= 125):
		k = i
		cromossomo[i] = 2

		custo_release2 += custo[i]

		if(k in posicao):
			posicao.remove(k)
		
		i = random.choice(posicao)


	i = random.choice(posicao)

	while(custo_release3 + custo[i] <= 125):
		k = i
		cromossomo[i] = 3
		custo_release3 += custo[i]

		if(k in posicao):
			posicao.remove(k)
		
		i = random.choice(posicao)

	individuo[0] = copy.deepcopy(cromossomo)
	individuo[1] = score(importancia_total, P, cromossomo, risco)
	populacao[cont_populacao] = copy.deepcopy(individuo)


	cont_populacao += 1
	custo_release1 = 0
	custo_release2 = 0
	custo_release3 = 0
	posicao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	cromossomo = [0] * 10


G -= 1

# Selecao + Cruzamento #

k = 0
d_cont = 0
taxa_cruzamento = 0.75
filho1 = [[0], 0]
filho2 = [[0], 0]
descendentes = [0] * P
p1 = [0] * 10
p2 = [0] * 10
ponto_de_corte = random.randint(0, 9)


while(k < P):

	probabilidade_cruzamento = random.random()

	p1 = copy.deepcopy(random.choice(populacao))
	p2 = copy.deepcopy(random.choice(populacao))
	#p1 = copy.deepcopy(p1[0]);
	#p2 = copy.deepcopy(p2[0]);


	if(probabilidade_cruzamento <= taxa_cruzamento):
		filho1[0] = copy.deepcopy(crossover(p1[0], p2[0], ponto_de_corte))
		filho2[0] = copy.deepcopy(crossover(p2[0], p1[0], ponto_de_corte))


		#Reparo no Filho 1#
		for i in range(0, 10):
			if(filho1[0][i] == 1):
				if(custo_release1 + custo[i] <= 125):
					custo_release1 += custo[i]
				else:
					filho1[0][i] = copy.deepcopy(0)

			elif(filho1[0][i] == 2):
				if(custo_release2 + custo[i] <= 125):
					custo_release2 += custo[i]
				else:
					filho1[0][i] = copy.deepcopy(0)

			elif(filho1[0][i] == 3):
				if(custo_release3 + custo[i] <= 125):
					custo_release3 += custo[i]
				else:
					filho1[0][i] = copy.deepcopy(0)


		custo_release1 = 0
		custo_release2 = 0
		custo_release3 = 0

		#Reparo no Filho 2#
		for i in range(0, 10):
			if(filho2[0][i] == 1):
				if(custo_release1 + custo[i] <= 125):
					custo_release1 += custo[i]
				else:
					filho2[0][i] = copy.deepcopy(0)

			elif(filho2[0][i] == 2):
				if(custo_release2 + custo[i] <= 125):
					custo_release2 += custo[i]
				else:
					filho2[0][i] = copy.deepcopy(0)

			elif(filho2[0][i] == 3):
				if(custo_release3 + custo[i] <= 125):
					custo_release3 += custo[i]
				else:
					filho2[0][i] = copy.deepcopy(0)

		filho1[1] = score(importancia_total, P, filho1[0], risco)
		filho2[1] = score(importancia_total, P, filho2[0], risco)

		#print(filho1)
		#print(filho2)

		descendentes[d_cont] = copy.deepcopy(filho1)
		d_cont +=1
		descendentes[d_cont] = copy.deepcopy(filho2)
		d_cont+=1

		k+=2

	else:
		descendentes[d_cont] = copy.deepcopy(p1)
		d_cont +=1
		descendentes[d_cont] = copy.deepcopy(p2)
		d_cont += 1

		k += 2












#populacao = copy.deepcopy(sorted(populacao, key = lambda x: x[1], reverse = True)) #Ordenado pelo fitness/score de forma decrescente
#print("Populacao")
#for i in range (0, P):
#	print(populacao[i])

