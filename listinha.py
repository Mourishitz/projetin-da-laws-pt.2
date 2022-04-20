
# EXERCICIO 1

# funcao pra acronimo
def fxn(stng):
    # adicionar primeira letra
    oupt = stng[0]

    # iterar no input.str
    for i in range(1, len(stng)):
        if stng[i - 1] == ' ':
            # adicionar letra depois do espaço
            oupt += stng[i]

    # deixar o output maiusculo
    oupt = oupt.upper()
    return oupt


# inputs
inpt1 = str(inpu("Digite uma frase para transformar em Acronimo: "))

# output do acronimo
print(fxn(inpt1))

# EXERCICIO 2

#limpar caractere especial do cpf (pontos e traços)
inpt = input("Digite o seu CPF: ")
cpf = ''.join(e for e in inpt if e.isalnum())

#lista de estados por cpf

lista = ["Rio Grande do Sul",
         "Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins",
         "Pará, Amazonas, Acre, Amapá, Rondônia e Roraima",
         "Ceará, Maranhão e Piauí",
         "Pernambuco, Rio Grande do Norte, Paraíba e Alagoas",
         "Bahia e Sergipe",
         "Minas Gerais",
         "Rio de Janeiro e Espírito Santo",
         "São Paulo",
         "Paraná e Santa Catarina"]


#identificar o ultimo digito do cpf
digito = int(cpf[8])
print("Seu CPF tem o digito antes dos digitos de controle igual a "+str(digito))
print("Seu estado é: "+str(lista[digito]))

# EXERCICIO 3

# EXPLICAÇÃO MATEMATICA
# achar um numero de digito n em Armstrong
# Primeiro extrair cada digito do numero e multiplicar n vezes e adicionar todos esses valores
# a soma vai ser comparada com um numero que foi dado, se é o mesmo entao é um Armstrong, else = nao é

# Passo 1: ler o numero
# Passo 2: Calcular o numero de digitos e armazenar na variavel n
# Passo 2²: Declarar a variavel soma e iniciar em 0
# Passo 2³: Para cada digito no numero, multiplicar o mesmo digito por m vezes e adicionar isso na soma
# Passo 3: Checar se é igual ao numero do int(input)
# Passo 4: if statement para indicar se é ou nao um Armstrong

number = int(input("Digite um número: "))
m = len(str(number))
temp = number
add_sum = 0
while temp!=0:
    #pegar o ultimo digito
    k = temp%10
    #achar k^m
    add_sum +=k**m
    #divisoes que se atualizam conforme o ultimo e penultimo digito
    temp = temp//10
if add_sum==number:
    print('Seu numero é um numero de Armstrong')
else:
    print('Seu numero não é um numero de Armstrong')
