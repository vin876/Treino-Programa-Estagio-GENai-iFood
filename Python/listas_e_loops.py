# LISTAS
numeros = [10, 20, 30, 40]

print("Primeiro:", numeros[0])
print("Tamanho:", len(numeros))

# ADICIONAR
numeros.append(50)

# REMOVER
numeros.remove(20)

# LOOP EM LISTA
for n in numeros:
    print("Número:", n)

# COMPREENDENDO A LISTA
dobrados = [n * 2 for n in numeros]
print("Dobrado:", dobrados)

