# 2 - Crie um dicionário d e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone,endereço. Também usando d, 
# imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave.

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
telefone = input("Informe seu telefone: ")
endereco = input("Informe seu endereço: ")

d = {
    "Nome": nome,
    "Idade": idade,
    "Telefone": telefone,
    "Endereço": endereco
}

print (d)

