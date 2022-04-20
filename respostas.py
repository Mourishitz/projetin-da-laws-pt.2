# Lista com a quantidade de dias em cada mes, sendo 0 = janeiro e 11 = dezembro
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
mes_escolhido = int(input("Digite um número de 1 a 12 para indicar um mês do ano, sendo 1 = janeiro, 2 = fevereiro, etc:  "))

# algoritmo para identificar se o mes escolhido existe(menor que 12)
if mes_escolhido <= 12:
    i = mes_escolhido-1 # maneira de contar ao computador que o item 0 da lista dias é igual ao numero 1 digitado pelo usuario
    valor = (dias[i]) # assumir o valor ao numero de dias de um certo mes escolhido
    print("O mês "+str(mes_escolhido)+" tem "+str(valor)+" dias!") # um print bonitinho :)
