# As LISTAS formam um tipo de dado integrado.

nomes = ['raíssa', 'pereira', 'joana', 'margarido', 'josefina'] #string
numeros = [37, 76, 23, 14, 12, 34, 57, 98, 43] # int
notas = [8.1] #float
vazio = [] 

aluno = ['joão', 0.9, 10] #string, float, int
endereco = ['rua', 'sao joao', 304, '500069-000'] #string, string, int, string

print()
print("... INDEXAÇÃO:")

# Indexação:
# O INDÍCE indica a posição do elemento na lista.
# O primeiro elemento é indexado em 0.
# O último elemento pode ser referenciado por -1, indíce reverso.
print(nomes[0])
print(nomes[1])

print()
print("... FATIAMENTO:")

# FATIAMENTO indica um intervalo a ser acessado.
# Através do operador ':'.
print(endereco[0:2])
print(endereco[:2]) #começa do primeiro elemento
print(endereco[2:]) #mostra até o último elemento
print(endereco[:]) #toda lista
print(endereco[-4:-2])

print()
print("... ALTERAÇÕES DE VALORES:")

# Alterações de valores:
penteados = ['kolese', 'koju', 'nagô', 'puff']
penteados[0] = 'twist'
print(penteados)
penteados[1:3] = ['dreads', 'crochet']
print(penteados)
penteados[-1] = 'lemonade'
print(penteados)

print()
print("... OPERAÇÕES:")

# Operações:
# O operador '+' é responsável por concatenar duas listas.
# O operador '*' repete a lista por um número inteiro de vezes. 
conca_penteados = penteados + numeros
print(conca_penteados)
multi_penteados = penteados * 3
print(multi_penteados)

print()
print("... EXCLUSÃO DE VALORES:")

# Exclusão de valores:
# A função 'pop()' para excluir determinado elemento indexado, sendo possível armazenar o valor.
a = nomes.pop(2)
print(a)
print(nomes)
# O operador 'del' para excluir determinado elemento indexado, sem armazenar o valor.
del numeros[2] #23
del numeros[3:5] #12, 34
print (numeros)
# A função 'remove()' para excluir determinado valor.
nomes.remove('raíssa')
print(nomes)

print()
print("... ADIÇÃO DE VALORES:")

# Adição de valores:
# O método 'append()' adiciona novo elemento ao fim da lista.
nomes.append('raíssa')
print(nomes)
# O método 'extend()' adiciona elementos de uma lista à outra.
aluno.extend(endereco)
print(aluno)
# O método 'insert' adiciona elementos em uma determinada posição.
numeros.insert(2, 23)
print(numeros)

print()
print("... ACESSO AOS ELEMENTOS DA LISTA:")

# Percorrendo listas:
# Para acessar os elementos da lista podemos usar a instrução 'for'.





