import math
cat_oposto = int(input('Digita o valor do cateto oposto :'))
cat_adjac = int(input('Digite o valor do cateto adjacente :'))
a = cat_oposto ** 2
b = cat_adjac ** 2
c = a + b
hipot = math.sqrt(c)
print(f'O valor da hipotenusa é {hipot} :')