def main():
    #Menu
    while True:
        print("\nMenu:")
        print("1 - Soma (inteiros)")
        print("2 - Resto da Divisão")
        print("3 - Multiplicação")
        print("4 - Divisão Inteira")
        print("5 - Quadrado")
        print("6 - Soma (flutuantes)")
        print("7 - Média de números flutuantes")
        print("8 - Cálculo de Potência")
        print("9 - Conversor Celsius para Fahrenheit")
        print("10 - Cálculo da área do círculo")
        print("11 - Converter texto para maiúsculas")
        print("12 - Exibir primeiro nome em maiúsculas")
        print("13 - Sair...\n")

        #Solicita a escolha do usuário
        try:
            opcaoEscolhida = int(input("Escolha uma opção(1-12)\n"))
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
                ex6()
            if opcaoEscolhida == 7:
                ex7()
            if opcaoEscolhida == 8:
                ex8()
            if opcaoEscolhida == 9:
                ex9()
            if opcaoEscolhida == 10:
                ex10()
            if opcaoEscolhida == 11:
                ex11()
            if opcaoEscolhida == 12:
                ex12()
            if opcaoEscolhida == 13:
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

def ex6():
    #Escreva um programa que receba dois números flutuantes e realize a sua adição.
    try:
        primeiroNumero = float(input("Digite o primeiro numero (deve ser do tipo FLOAT): "))
    except ValueError:
        print("Digite um número FLOAT válido")
        exit()
    try:
        segundoNumero = float(input("Digite o segundo numero  (deve ser do tipo FLOAT): "))
    except ValueError:
        print("Digite um número FLOAT válido")
        exit()
    print(f" A soma dos dois números é {primeiroNumero + segundoNumero}")   

def ex7():
    #Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    try:
        primeiroNumero = float(input("Digite o primeiro numero (deve ser do tipo FLOAT): "))
    except ValueError:
        print("Digite um número FLOAT válido")
        exit()
    try:
        segundoNumero = float(input("Digite o segundo numero  (deve ser do tipo FLOAT): "))
    except ValueError:
        print("Digite um número FLOAT válido")
        exit()
    print(f" A média dos dois números é {(primeiroNumero + segundoNumero) / 2}")   

def ex8():
    #Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    try:
        numeroBase = float(input("Digite a Base: "))
    except ValueError:
        print("Digite um número válido")
        exit()
    try:
        numeroExpoente = float(input("Digite o expoente: "))
    except ValueError:
        print("Digite um número válido")
        exit()
    print(f" A potência da base informada é {numeroBase ** numeroExpoente}") 

def ex9():
    #Faça um programa que converta a temperatura de Celsius para Fahrenheit.
    try:
        numeroTemperatura = float(input("Digite os graus °C: "))
    except ValueError:
        print("Digite um valor válido")
        exit()
    numeroFahrenheit = (numeroTemperatura * 9/5) + 32
    print(f" A temperatura em Fahrenheit é {numeroFahrenheit}")

def ex10():
    #Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada
    try:
        valorRaio = float(input("Digite o valor do raio: "))
    except ValueError:
        print("Digite um valor válido")
        exit()
    areaCirculo = 3.14 * (valorRaio ** 2)
    print(f" A área do círculo é {areaCirculo}")

def ex11():
    #Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    try:
        inputString = str(input("Digite uma string para ser colocada em maiúscula: "))
    except ValueError:
        print("Digite uma string válida")
    inputString = inputString.upper()
    print(f"A string em maiúscula é: {inputString}")

def ex12():
    try:
        inputString = str(input("Digite seu nome completo para ser colocada em maiúscula: "))
    except ValueError:
        print("Digite uma string válida")
    nome = inputString.split()[0].upper()
    print(f"O primeiro nome é: {nome}")

if __name__ == "__main__":
    main()
