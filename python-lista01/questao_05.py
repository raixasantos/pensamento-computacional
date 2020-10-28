renda = float(input("Informe o valor da renda: "))
if (renda <= 2000):
    print('Isento')
if (renda > 2000) or (renda <= 3000):
    print("Imposto: " + str(renda - 2000 * 0.08))
if (renda > 3000) or (renda <= 4500):
    print("Imposto: " + str(renda - 2000 * 0.18))
if (renda > 4500):
    print("Imposto: " + str(renda - 2000 * 0.28))
    