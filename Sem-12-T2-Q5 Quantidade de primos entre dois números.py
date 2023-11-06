#Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

def e_primo(numero):
    for i in range(2, numero):
        if numero % i == 0: return False
    return True

def mostra_numeros_primos(numero_um, numero_dois):
    for i in range(numero_um, (numero_dois + 1)):
        if e_primo(i): 
            print(i)



def main():
    
    numero_um = input().strip()
    numero_dois = input().strip()
    numero_um = int(numero_um)
    numero_dois = int(numero_dois)

    mostra_numeros_primos(numero_um, numero_dois)

    

if __name__ == '__main__':
    main()