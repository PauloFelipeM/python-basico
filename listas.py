lista = [1, 2, 3, 4, 5]
lista2 = ["teste", "teste2", "teste3"]
lista3 = ["teste", 0, 9.99]
lista4 = []

# add na lista
lista3.append('teste4')

# deleta da lista
del lista3[2]
del lista3[:]

# ordena da lista
lista.sort()

# ordena da lista de forma reversa
lista.sort(True)

for i in lista2:
  print(i)

for i in range(10, 20, 2):
  print(i)

if 0 in lista3:
  print("Sim")

# raiz quadrada dos valores
x = [1, 2, 3, 4, 5]
y = []

for i in x:
  y.append(i**2)

print(x)
print(y)

# list comprehension
x = [1, 2, 3, 4, 5]

# raiz quadrada dos valores
y = [i ** 2 for i in x]

# Apenas números impares
z = [i for i in x if i % 2 == 1]

print('list comprehension')
print(x)
print(y)
print(z)