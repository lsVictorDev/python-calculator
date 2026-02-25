print('Bem-Vindo a calculadora do Dev Victor! :)')

conta = input('Qual operação deseja fazer? (+, -, x, /): ')

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número: '))

if conta == 'x':
    print(f'O resultado da multiplicação é: {num1*num2}')

elif conta == '+':
    print(f'O resultado da adição é: {num1+num2}')

elif conta == '-':
    print(f'O resultado da subtração é: {num1-num2}')

# Verificando se o segundo número é zero para evitar erro
elif conta == '/':
    if num2 == 0:
        print('Erro! Divisão por 0')
    else:
        print(f'O resultado da divisão é: {num1/num2}')

else: print('Algo deu errado! Tente novamente')

print('-----Fim do programa-----')
