# 4 - Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. 
# Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

pessoas = {}  
menores = {}  

while True:
    print("Menu:")
    print("1 - Cadastrar nova pessoa")
    print("2 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o CPF: ")

        pessoas[cpf] = {
            "nome": nome,
            "idade": idade
        }

    elif escolha == "2":
        break

    else:
        print("Opção inválida. Escolha 1 para cadastrar ou 2 para sair.")


for cpf, dados in pessoas.items():
    if dados["idade"] < 18:
        menores[cpf] = dados

for cpf in menores:
    del pessoas[cpf]

print("\nPessoas maiores de 18 anos:")
for cpf, dados in pessoas.items():
    print(f"CPF: {cpf}, Nome: {dados['nome']}, Idade: {dados['idade']}")

print("\nMenores de 18 anos:")
for cpf, dados in menores.items():
    print(f"CPF: {cpf}, Nome: {dados['nome']}, Idade: {dados['idade']}")