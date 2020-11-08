numeros = [0,1,2,3,4,5,6,7,8,9]
a = 10

def produto(x, L):
    for i in range(len(L)):
        L[i] = x * L[i]
    return L

print(produto(a,numeros))