import funcoes

funcoes.clear()
texto = ('='*30 + 'CALCULADORA EXPERIMENTAL'+'='*30)
print(funcoes.cor('red', texto))

texto = '  Selecione uma das opções abaixo: '
print(funcoes.cor('green', texto))
print('=' * 85)
print('[A] Verifica se o número é primo ou não ')
print('[B] Calcula o fatorial de um número inteiro ')
print('[C] Cálculo das raízes Reais (Bhaskara) ')
print('[D] Cálculo do resto da divisão')
print('=' * 85)


atende = False
while atende == False:
    seleciona_calculadora = input(
        'Digite a letra correspondente a calculadora desejada: ').lower()

    if seleciona_calculadora == 'A' or seleciona_calculadora == 'a':
        funcoes.numero_Primo()
        atende = True

    elif seleciona_calculadora == 'B' or seleciona_calculadora == 'b':
        funcoes.fatorial()
        atende = True

    elif seleciona_calculadora == 'C' or seleciona_calculadora == 'c':
        funcoes.bhaskara()
        atende = True

    elif seleciona_calculadora == 'd':
        funcoes.resto()
        atende = True

    else:
        texto = ('Digite somente as letras do menu!!!')
        print(funcoes.cor('yellow', texto))
        atende = False
