#Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa que leia um número e determine se ele é ou não primo.

def e_primo(numero):
    for i in range(2, numero):
        if numero % i == 0: return False
    return True


def main():
    numero = input().strip()
    numero = int(numero)

    resultado = e_primo(numero)
    print(resultado)
    
if __name__ == '__main__':
    main()