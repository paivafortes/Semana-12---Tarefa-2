#A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.

def fibonacci(numero):
    começo_fibonacci = 0
    memoria = 0
    proximo_valor_fibonacci = 1
    lista_fibonacci = []
    for i in range(numero):
        lista_fibonacci.insert(i, começo_fibonacci)
        memoria = começo_fibonacci
        começo_fibonacci += proximo_valor_fibonacci
        proximo_valor_fibonacci = memoria
    return lista_fibonacci
def main():
    numero = input()
    numero = int(numero)

    resultado = fibonacci(numero)
    print(str(resultado).replace('[', '').replace(']',''))
    
    

if __name__ == '__main__':
    main()