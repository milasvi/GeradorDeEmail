import emoji
import random

print(emoji.emojize(':e-mail: Gerador De Emails da Universidade :e-mail:'))

while True:
    nome = str(input('Qual é seu nome completo?')).strip()
    lista = nome.split()

    email1 = f'{lista[0].lower()}_{lista[-1].lower()}{random.randint(0,22)}@universidade.edu.br'
    email2 = f'{random.choice(lista).lower()}_{random.choice(lista).lower()}{random.randint(23,55)}@universidade.edu.br'
    email3 = f'{random.choice(lista).lower()}_{random.choice(lista).lower()}{random.randint(56,99)}@universidade.edu.br'

    email = input(f'\nEscolha uma das opções abaixo \n[1]{email1} \n[2]{email2} \n[3]{email3}:')
    while email != '1' and email !='2' and email != '3':
        email = input('\nOpção inválida! Digite apenas 1, 2 ou 3.')
    if email == '1':
        print(f'\nSeu novo email estudantil é {email1}.')
    elif email == '2':
        print(f'\nSeu novo email estudantil é {email2}')
    elif email == '3':
        print(f'\nSeu novo email estudantil é {email3}')
    

    repeticao = str(input('\nDeseja gerar outro email?'))
    while repeticao.upper()[0] != 'N' and repeticao.upper()[0] !='S':
        repeticao = input(emoji.emojize('\nNão entendi :thinking_face:...'))
    if repeticao.upper()[0] == 'N':
        print('\nSaindo...\nAté mais.')
        break
