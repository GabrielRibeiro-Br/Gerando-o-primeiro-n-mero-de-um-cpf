import os

while True:
    cpf = input("Digite os 9 primeiros números do seu cpf: ")
    cpf = cpf.replace(".", "").replace("-", "")
    lista_resultado = []
    cpf_lista = [int(digito) for digito in cpf]
    numeros = list((range(10, 1, -1)))
    os.system('cls')    
    
    for indice, digito in enumerate(cpf_lista):
        numero = numeros[indice]
        resultado = digito * numero
        print(resultado)
        lista_resultado.append(resultado)
    
    total = sum(lista_resultado)
    print(total)
    
    vezes10 = total * 10
    print(vezes10)
    
    resto = vezes10 % 11
    divisivel = 0 if resto > 9 else resto
    print(divisivel)

    
    print(f'O primeiro digito do cpf é: {cpf_lista[0]}')        