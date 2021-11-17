from os import system, name

def clear():
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def cor(cor, texto):
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'

def numero_Primo():
    numero = int(input("Digite um número inteiro: "))
    contador = 2
    resto = 0

    naoprimo = False

    while contador < numero:
        resto = numero % contador
        contador = contador + 1
        if resto == 0:
            naoprimo=True
    if naoprimo:
        texto = "R: Não é um número primo"
        print(cor('yellow', texto))
    else:
        texto = "R: Esse é um número primo"
        print(cor('blue', texto))

def fatorial():
    numero = int(input('Digite um número inteiro: '))
    resultado = 1
    contagem = 1

    while contagem <= numero: ## N! = Nx * Nx-1 * Nx -2...
        resultado = resultado * contagem
        contagem = contagem + 1

    texto = f'O valor de {numero}! é: {resultado}'
    print(cor('blue', texto))

def bhaskara():
    
    a = float(input('Digite o valor de "a": ')) #Tipo de valor como float (prevendo decimais)
    b = float(input('Digite o valor de "b": '))
    c = float(input('Digite o valor de "c": '))

    print('=' * 75)
    print(f'Os coeficientes da equação informados foram: ',a,'x² +',b,'x +',c,'= 0')
    print('=' * 75)

    delta = ((b**2) - 4 * a * c)

    if delta == 0: # Nesse caso somente uma raiz é possível.
        x1 = (- b + (delta**0.5)) / (2 * a) # Elevar um número a 0.5 é o mesmo que sua raiz quadrada
        print('A única raiz é:', x1)
        print('=' * 75)
    else:
        if delta < 0: # Não se aplica aos números Reais.
            print('O Delta é negativo, portanto, essa equação não possui raízes Reais')
            print('=' * 75)
        else:
            x1 = (- b + (delta**0.5)) / (2 * a) # Complementando a fórmula de Bhaskara.
            x2 = (- b - (delta**0.5)) / (2 * a)
            print('A primeira raiz (x1) é: ', x1)
            print('A segunda raiz (x2) é: ', x2)
            print('=' * 75)