val = float(input("Digite a distância da viagem em km: "))
km = 0.50 if val <= 200 else 0.45
total = val * km
print(f'O valor da passagem é R${total}')
