numeros01 = [1,23,4]
numeros02 = [0,1,24,4]

def contar(lista01, lista02):
    total = 0
    for i in range(len(lista01)):
        for j in range(len(lista02)):
            if lista01[i] == lista02[j]:
                total += 1
    return total

print(contar(numeros01,numeros02))