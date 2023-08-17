# 3- Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone. O programa deve 
# ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-fone.

agenda = {} 

while True:
    print("Menu:")
    print("1 - Cadastrar novo contato")
    print("2 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        telefone = input("Digite o telefone: ")

       
        agenda[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }

    elif escolha == "2":
        break

    else:
        print("Opção inválida. Escolha 1 para cadastrar ou 2 para sair.")


for cpf, dados in agenda.items():
    print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")

    