'''
12. Escreva um programa que calcule o resto da divisão inteira entre dois números.
Utilize apenas as operações de soma e subtração para calcular o resultado.
'''

try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    if num2 == 0:
        print('Erro Matemático, não tem como dividir por 0')
    else:
        resto = num1
        
        while resto >= num2:
            resto = resto - num2

        print(f'O resto da Divisão é: {resto}')
        
except ValueError:
    print('Valor Inválido')
