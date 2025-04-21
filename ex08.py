'''
Escreva um programa que exiba uma lista de opções (menu): adição, subtração,
divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até
que a opção “saída” seja escolhida.
'''

while True: 
    print('1: Adição, 2: Subtração, 3: Multiplicação, 4: Divisão,  0: Sair')
    opcao = int(input('Digite a sua Opção: '))

    if opcao == 1:
        num = int(input('Você deseja a tabuada de qual número? '))
        print('ADIÇÂO')
        print('-' * 12)
        print(f'{num} + {1} = {num + 1}')
        print(f'{num} + {2} = {num + 2}')
        print(f'{num} + {3} = {num + 3}')
        print(f'{num} + {4} = {num + 4}')
        print(f'{num} + {5} = {num + 5}')
        print(f'{num} + {6} = {num + 6}')
        print(f'{num} + {7} = {num + 7}')
        print(f'{num} + {8} = {num + 8}')
        print(f'{num} + {9} = {num + 9}')
        print(f'{num} + {10} = {num +10}')
        print('-' * 12)

    elif opcao == 2:
        num = int(input('Você deseja a tabuada de qual número? '))
        print('SUBTRAÇÃO')
        print('-' * 12)
        print(f'{num + 1} - {num} = {(num + 1) - num}')
        print(f'{num + 2} - {num} = {(num + 2) - num}')
        print(f'{num + 3} - {num} = {(num + 3) - num}')
        print(f'{num + 4} - {num} = {(num + 4) - num}')
        print(f'{num + 5} - {num} = {(num + 5) - num}')
        print(f'{num + 6} - {num} = {(num + 6) - num}')
        print(f'{num + 7} - {num} = {(num + 7) - num}')
        print(f'{num + 8} - {num} = {(num + 8) - num}')
        print(f'{num + 9} - {num} = {(num + 9) - num}')
        print(f'{num + 10} - {num} = {(num + 10) - num}')
        print('-' * 12)

    elif opcao == 3:
        num = int(input('Você deseja a tabuada de qual número? '))
        print('MULTIPLICAÇÃO')
        print('-' * 12)
        print(f'{num} X {1} = {num * 1}')
        print(f'{num} X {2} = {num * 2}')
        print(f'{num} X {3} = {num * 3}')
        print(f'{num} X {4} = {num * 4}')
        print(f'{num} X {5} = {num * 5}')
        print(f'{num} X {6} = {num * 6}')
        print(f'{num} X {7} = {num * 7}')
        print(f'{num} X {8} = {num * 8}')
        print(f'{num} X {9} = {num * 9}')
        print(f'{num} X {10} = {num * 10}')
        print('-' * 12)

    elif opcao == 4:
        num = int(input('Você deseja a tabuada de qual número? '))
        print('DIVISÃO')
        print('-' * 12)
        print(f'{num * 1} / {num} = {num*1 / num} ')
        print(f'{num * 2} / {num} = {num*2 / num} ')
        print(f'{num * 3} / {num} = {num*3 / num} ')
        print(f'{num * 4} / {num} = {num*4 / num} ')
        print(f'{num * 5} / {num} = {num*5 / num} ')
        print(f'{num * 6} / {num} = {num*6 / num} ')
        print(f'{num * 7} / {num} = {num*7 / num} ')
        print(f'{num * 8} / {num} = {num*8 / num} ')
        print(f'{num * 9} / {num} = {num*9 / num} ')
        print(f'{num * 10} / {num} = {num*10 / num} ')
        print('-' * 12)

    elif opcao == 0:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
