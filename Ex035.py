import random
num = int(input("Escreva um número de 1 a 5:"))
numero= [1, 2, 3, 4, 5]
escolhido = random.choice(numero)
print(f'O numero escolhido foi {escolhido}')

if num == escolhido:
    print("Você ganhou!")
else:
    print("Você perdeu!")
