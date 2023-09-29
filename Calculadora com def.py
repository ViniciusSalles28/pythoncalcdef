# Calculadora Utilizando Funções

def soma(numero):
   return int(numero[0]) + int(numero[1])


def subtracao(numero):
     return int(numero[0]) - int(numero[1])


def multiplicacao(numero):
     return int(numero[0]) * int(numero[1])


def divisao(numero):
     return int(numero[0]) / int(numero[1])



entrada_numeros = input('Digite dois numeros com espaços: ').split(' ')
entrada_operadores = input('Digite algum desses operadores "+-*/": ')
resultado = 0

if len(entrada_numeros) != 2:
    print('Você não digitou a quantidade correta de números')
else:
    if entrada_operadores in '+/-*':
        if entrada_operadores == '+':
            resultado = soma(entrada_numeros)
       
        elif entrada_operadores == '-':
            resultado = subtracao(entrada_numeros)
       
        elif entrada_operadores == '*':
            resultado = multiplicacao(entrada_numeros)
        
        elif entrada_operadores == '/':
            resultado = divisao(entrada_numeros)
        
        print(f'O resultado foi : {resultado}')
    else:
        print(f'O operador digitado não foi correspondente aos {entrada_operadores}')












