arq = open("texto")

# ler arquivo inteiro
print(arq.read())

# ler arquivo por linhas
for linha in arq.readlines():
  print(linha)

arq.close()

arq2 = open("texto2", "w")
arq2.write("Esse é novo arquivo")
arq2.close()