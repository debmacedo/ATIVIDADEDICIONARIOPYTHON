# 5 - Considere um sistema onde os dados são armazenados em dicionários. Nesse sistema existe um dicionario principal e o dicionário 
# de backup. Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo. Crie um 
# programa que insira dados em um dicionário, realizando o backup a cada dado e excluindo os dados do dicionário principal quando 
# ele atingir tamanho 5.

def backup(dicionario_principal, dicionario_backup):
    dicionario_backup.update(dicionario_principal)
    dicionario_principal.clear()

dicionario_principal = {}
dicionario_backup = {}

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")

    dicionario_principal[cpf] = {
        "nome": nome,
        "idade": idade
    }

    if len(dicionario_principal) == 5:
        backup(dicionario_principal, dicionario_backup)
        print("Backup realizado!")

if dicionario_principal:
    print("\nDados restantes no dicionário principal:")
    for cpf, dados in dicionario_principal.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Idade: {dados['idade']}")

print("\nDados no dicionário de backup:")
for cpf, dados in dicionario_backup.items():
    print(f"CPF: {cpf}, Nome: {dados['nome']}, Idade: {dados['idade']}")