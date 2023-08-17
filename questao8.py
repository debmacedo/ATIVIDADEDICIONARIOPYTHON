# 8 - Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os 
# guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda 
# a classificação final em ordem (1o o campeão). O campeão é o que tem a menor média de tempos.

def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

dicionario_corredores = {}  

for i in range(6):
    nome = input(f"Digite o nome do corredor {i+1}: ")
    tempos = []
    for volta in range(10):
        tempo = float(input(f"Digite o tempo da volta {volta+1} em segundos: "))
        tempos.append(tempo)
    dicionario_corredores[nome] = tempos

melhor_volta = float("inf")
nome_melhor_volta = ""
volta_melhor_volta = 0

for nome, tempos in dicionario_corredores.items():
    melhor_tempo_corredor = min(tempos)
    if melhor_tempo_corredor < melhor_volta:
        melhor_volta = melhor_tempo_corredor
        nome_melhor_volta = nome
        volta_melhor_volta = tempos.index(melhor_tempo_corredor) + 1

classificacao = sorted(dicionario_corredores, key=lambda nome: calcular_media_tempos(dicionario_corredores[nome]))

print(f"A melhor volta da prova foi de {nome_melhor_volta}, na volta {volta_melhor_volta}.")
print("Classificação final:")
for posicao, nome in enumerate(classificacao, start=1):
    media_tempos = calcular_media_tempos(dicionario_corredores[nome])
    print(f"{posicao}º lugar: {nome} (Média de tempos: {media_tempos:.2f} segundos)")