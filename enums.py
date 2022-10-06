lista = ["teste", "teste2", "teste3"]

#enums
for i, nome in enumerate(lista):
  print(i, nome)


#map
def dobro(x):
  return x*2

valores = [1,2,3,4,5]

valores_dobrados = map(dobro, valores);

print(list(valores_dobrados))

from functools import reduce

#reduce
def soma(x,y):
  return x+y

lista = [1, 2, 3, 4, 5]

soma = reduce(soma, lista)

#zip - contatenar listas
lista1 = [1, 2, 3]
lista2 = ['texto', 'texto2', 'texto3']

for numero, nome in zip(lista1, lista2):
  print(numero, nome)