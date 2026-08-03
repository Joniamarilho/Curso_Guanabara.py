vel = int(input("Digite a velocidade do carro em km/h: "))
if vel > 80:
    print("Você foi multado! A velocidade máxima permitida é de 80 km/h.")
    multa = (vel - 80) * 7
    print(f"O valor da multa é de R${multa:.2f}.")