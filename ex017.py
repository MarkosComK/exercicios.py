#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Usanto SQRT
from math import sqrt
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h =  sqrt(c1 ** 2 + c2 ** 2) 
print(f'A hipotenusa tem valor {h:.2F}')

  #  sem usar SQRT
  #  c1 = float(input('Comprimento do cateto oposto: '))
  #  c2 = float(input('Comprimento do cateto adjacente: '))
  #  h = (c1 ** 2 + c2 ** 2) ** (1/2) 
  #  print(f'A hipotenusa tem valor {h:.2F}')


#Usando Hypot
#from math import hypot
#c1 = float(input('Comprimento do cateto oposto: '))
#c2 = float(input('Comprimento do cateto adjacente: '))
#h =  hypot(c1, c2)
#print(f'A hipotenusa tem valor {h:.2F}')