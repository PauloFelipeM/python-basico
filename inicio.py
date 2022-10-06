print(2 + 2);
print(2 - 2);
print(2 * 3);
print(10 / 3);
# Exponente
print(2 ** 3);
# dividir retornando o resto
print(10 % 3);

mensagem = "Alo";
print(mensagem);

x = 3;
y = 1;

print(x > y);

print(x == y and x < y);

print(x == y or x < y);

print(not(x < y));

if not(x == y):
  print('Sim');
elif(x == y):
  print('Não');
else:
  print('Não');

x = 1;

while x <= 10:
  print(x);
  x += 1;

tamanho = ' aacawasDDdanhowua\n'

print(len(tamanho));

print(tamanho[1]);
print(tamanho[1:5]);
print(tamanho.lower());
print(tamanho.upper());

# remove espaços e caracteres especiais
print(tamanho.strip());

# convert string to array
print(tamanho.split('a'));

# busca string
print(tamanho.find('DD'));

# replace string
print(tamanho.replace('DD', 'dd'));