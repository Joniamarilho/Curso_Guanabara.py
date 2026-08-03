sal = float(input("Digite o salário do funcionário: R$"))
if sal <= 1250:
    novo = sal * 0.10
else:
    novo = sal * 0.15
print(f'O salário do funcionário era R${sal:.2f} e aumentou R${novo:.2f}')