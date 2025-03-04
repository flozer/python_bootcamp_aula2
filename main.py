def main():
    #Menu
    while True:
        print("\nMenu:")
        print("1 - Soma ")
        print("2 - Resto da Divisão ")
        print("3 - Multiplicação ")
        print("4 - Divisão Inteira ")
        print("5 - Quadrado ")
        print("6 - Sair... \n")

        #Solicita a escolha do usuário
        try:
            opcaoEscolhida = int(input("Escolha uma opção(1-6)\n"))
            if opcaoEscolhida == 1:
                ex1()
            if opcaoEscolhida == 2:
                ex2()
            if opcaoEscolhida == 3:
                ex3()
            if opcaoEscolhida == 4:
                ex4()
            if opcaoEscolhida == 5:
                ex5()
            if opcaoEscolhida == 6:
                print("Saindo...")
                break
        except ValueError:
            print("Opção Inválida")

def ex1():
    #Escreva um programa que soma dois números inteiros inseridos pelo usuário.
    #A fazer: tratar possíveis erros (Feito 04/03/2025)
    try:
        primeiroNumero = int(input("Digite o primeiro numero (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    try:
        segundoNumero = int(input("Digite o segundo numero  (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    print(f" A soma dos dois números é {primeiroNumero + segundoNumero}")

def ex2():
    #Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
    try:
        numeroDigitado = int(input("Digite um numero para ver o resto da divisão por 5: "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
        print(f"O resto da divisão de {numeroDigitado} por 5 é: {numeroDigitado % 5}.")

def ex3():
    #Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    try:
        primeiroNumero = int(input("Digite o primeiro numero (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    try:
        segundoNumero = int(input("Digite o segundo numero  (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    print(f" O Resultado da multiplicação dos dois números é {primeiroNumero * segundoNumero}")

def ex4():
    #Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    try:
        primeiroNumero = int(input("Digite o primeiro numero (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    try:
        segundoNumero = int(input("Digite o segundo numero  (deve ser do tipo inteiro): "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    print(f" O Resultado da divisão inteira dos dois números é {primeiroNumero // segundoNumero}")

def ex5():
    #Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    try:
        numeroDigitado = int(input("Digite um numero para vê-lo ao quadrado: "))
    except ValueError:
        print("Digite um número INTEIRO válido")
        exit()
    print(f"O quadrado de {numeroDigitado} é {numeroDigitado ** 2}.")

if __name__ == "__main__":
    main()
