# EXERCICIO 1

# Lista com a quantidade de dias em cada mes, sendo 0 = janeiro e 11 = dezembro
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
mes_escolhido = int(input("Digite um número de 1 a 12 para indicar um mês do ano, sendo 1 = janeiro, 2 = fevereiro, etc:  "))

# algoritmo para identificar se o mes escolhido existe(menor que 12)
if mes_escolhido <= 12:
    i = mes_escolhido-1 # maneira de contar ao computador que o item 0 da lista dias é igual ao numero 1 digitado pelo usuario
    valor = (dias[i]) # assumir o valor ao numero de dias de um certo mes escolhido
    print("O mês "+str(mes_escolhido)+" tem "+str(valor)+" dias!") # um print bonitinho :)
else:
    print("Seu mes nao existe >:(")

# EXERCICIO 2

for i in range(100):
    print(i+1) # O "+1" é necessário pois o computador inicia em index 0, por isso é importante somar um para que sempre esteja entre 1 e 100 (e nao em 0)

# EXERCICIO 3

n = int(input("Digite um valor para n: "))
if n > 0: #algoritmo pra detectar se algo é maior q 0
    for i in range(n):
        print(i+1) # o +1 novamente faz o papel de "regulador" pro index 0 da maquina
else: print("Digite um número maior do que 0")
    
# EXERCICIO 4

n = int(input("Digite o valor de n: "))
m = int(input("Digite o valor de m: "))

if n > m:
    print("O valor 'm' deve ser maior do que o valor 'n'")
else:
    for i in range(n,m):
        print(i)
        
# EXERCICIO 5

for i in reversed(range(100)):
    print(i+1)

# EXERCICIO 6

valor = input("Digite um caractere: ")
print("O correspondente ASCII de '" + str(valor) + "' é", ord(valor))

# EXERCICIO 7

letras = list(map(chr, range(65, 91)))
print(letras)

# EXERCICIO 8

letras = list(map(chr, range(97, 123)))
print(letras)

# EXERCICIO 9

inp = input("Digite um caractere: ")
inp = ord(inp)
if ((inp > 64) and (inp < 91)):
    print("Maiusculo")
else:
    if((inp >96) and (inp <123)):
        print("Minusculo")
    else: print("Caractere especial")
