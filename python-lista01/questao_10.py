valorTotal = 0
qntPositivos = 0
valor = int(input("Digite um valor: "))
valorTotal += valor
menorValor = valor
maiorValor = valor
if valor > 0:
    qntPositivos += 1
for i in range(0,9):
    valor = int(input("Digite um valor: "))
    valorTotal += valor
    if valor > 0:
        qntPositivos += 1
    if valor > maiorValor:
        maiorValor = valor
    if valor < menorValor:
        menorValor = valor
mediaValores = valorTotal / 10
print("Quantidade de positivos: " + str(qntPositivos))
print("A média dos valores é " + str(mediaValores))
print("O menor valor é " + str(menorValor))
print("O maior valor é " + str(maiorValor))