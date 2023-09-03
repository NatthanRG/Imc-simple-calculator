
# Calculadora IMC

print('\033[4;33;40mᑕᗩᒪᑕᑌᒪᗩᗪOᖇᗩ ᗪE Iᗰᑕ  ')
peso = int(input('\033[0;35;40mQual seu peso atual?: '))
altura = float(input('\033[0;34;40mQual sua altura?: '))
nome = input('\033[0;33;40mQual seu nome?: ')
idade = int(input('Qual a sua idade?: '))
imc = peso / (altura ** 2)
validacao = input('\033[0;31;40mAs informações estão corretas? Responda S para Sim ou N para Não: ')
print(f'\033[1;36;40mOlá {nome}, seu peso atual é de {peso} kg e sua altura atual é de {altura} metros, nascido(a) em {2023 - int(idade)}.')

if validacao.lower() == 's':
    print(f'Seu IMC é: {imc:.2f}')

    if 0.00 <= imc < 18.5:
        print('\033[0;31;40mAbaixo do peso')
    else:
        print('.')

    if 18.60 <= imc < 24.90:
        print('\033[;32;40mPeso ideal')
    else:
        print('.')

    if 25.00 <= imc < 29.90:
        print('\033[1;33;40mUm pouco acima do peso')
    else:
        print('.')

    if 30.00 <= imc < 34.90:
        print('\033[1;31;40mObesidade grau 1')
    else:
        print('.')

    if 35.00 <= imc < 39.90:
        print('\033[1;31;40mObesidade grau 2')
    else:
        print('.')

    if imc > 40:
        print('\033[1;31;40mObesidade grau 3 (c vai morrer mlk)')

        input('aperte enter')


        




