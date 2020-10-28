valorMaior = 0
for i in [0,1,2]:
    valorDigitado = int(input("Digite um valor: "))
    if valorDigitado > valorMaior:
        valorMaior = valorDigitado
print("O maior valor digitado foi " + str(valorMaior))