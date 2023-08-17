# 7 - Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. 
# A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.

def calcular_media(notas):
    return sum(notas) / len(notas)

alunos = {}  # Dicionário para armazenar as notas

while True:
    nome = input("Digite o nome do aluno (ou enter para sair): ")

    if nome == "":
        break

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    alunos[nome] = [nota1, nota2]

nome_busca = input("Digite o nome do aluno para calcular a média: ")

if nome_busca in alunos:
    media = calcular_media(alunos[nome_busca])
    print(f"A média do(a) aluno(a) {nome_busca} é {media:.2f}.")
else:
    print(f"Aluno(a) {nome_busca} não encontrado(a).")