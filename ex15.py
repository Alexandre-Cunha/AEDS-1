'''
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura,
assim como a temperatura média.
'''

t = [ -10, -8, 0, 1, 2, 5, -2, -4]

soma_elementos_t = 0

for i in t:
    soma_elementos_t += i
    
media = soma_elementos_t / 8 

maior = t[0]
for i in t:
    if i > maior:
        maior =  i
        
menor = t[0]
for i in t:
    if i < menor:
        menor =  i

print(f'A menor temperatura registrada foi {menor}')
print(f'A maior temperatura registrada foi {maior}')
print(f'A temperatura média foi {media}')
