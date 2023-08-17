# 6 - Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada.

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador_vogais = {} 

    for char in texto:
        if char in vogais:
            if char in contador_vogais:
                contador_vogais[char] += 1
            else:
                contador_vogais[char] = 1

    return contador_vogais

texto = input("Digite um texto: ")
resultado = contar_vogais(texto)

for vogal, quantidade in resultado.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes.")