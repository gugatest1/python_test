# adding new users into the platform
#using def to prompt the command
from encodings import normalize_encoding


def cadastro_usuario():
    nome = input('Nome Principal: ')
    idade = input('Idade: ')
    sexo = input('Sexo: ')
    endereço = input('Insira seu endereço: ')
    email = input('Seu melhor email: ')
    documento = input('Insira seu documento: ')
    celular = input('Insira seu celular: ')

    print(cadastro_usuario())

