lados = [2,3,4,5,4,1,1,6,6,1,4,5]
qnt_lados = int(input('quantos lados? '))

def verificar(lados, qnt_lados):
    ocorrencia = []
    while qnt_lados != 0:
        soma = 0
        for i in range(len(lados)):
            if lados[i] == qnt_lados:
                soma += 1
        ocorrencia.append(soma)
        qnt_lados -= 1
    return ocorrencia

print(verificar(lados,qnt_lados))