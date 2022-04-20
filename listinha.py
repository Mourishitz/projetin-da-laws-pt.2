
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
