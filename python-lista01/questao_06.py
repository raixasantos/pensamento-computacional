duracao = 0.00
horaInicio = int(input("O jogo começou de que horas? "))
horaFim = int(input("O jogo terminou de que horas? "))
if horaFim > horaInicio:
    duracao = horaFim - horaInicio
else:
    duracao = 24 - (horaInicio + horaFim)
print("A duração foi de " + str(duracao) + "h")