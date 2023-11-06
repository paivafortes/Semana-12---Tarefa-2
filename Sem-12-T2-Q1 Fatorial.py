#Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1

def fatorial(numero):
    resultado = numero
    fatorial = 0
    if numero == 0 : return 1

    for i in range(1, (numero - 1)):
        fatorial = resultado * (numero - 1)
        resultado = fatorial
        numero -= 1

    return fatorial


def main():
    numero = input()
    numero = int(numero)


    resultado = fatorial(numero)
    
    print(resultado)
if __name__ == '__main__':
    main()