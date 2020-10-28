salario = float(input("Qual é o valor do salário? "))
perReajuste = float(input("Qual é o percentual de reajuste? "))
novoSalario = (salario*(perReajuste/100)) + salario
print("O novo salário é R$" + str(novoSalario))