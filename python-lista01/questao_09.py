valorTotal = 0.00
totalMercadorias = int(input("Qual é o número total de mercadorias no estoque? "))
for totalMercadorias in range(0, totalMercadorias):
    valorMercadoria = float(input("Valor da mercadoria: "))
    valorTotal += valorMercadoria
mediaMercadorias = valorTotal / totalMercadorias
print("O valor total em estoque é R$" + str(valorTotal))
print("A média de valor das mercadorias é R$" + str(mediaMercadorias))
