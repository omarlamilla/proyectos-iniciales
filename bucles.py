# from turtle import st


# def run():
#     LIMITE = 100000
#     contador = 0
#     elevado_2 = 2**contador
#     while elevado_2 < LIMITE:
#         print("2 elevado a " + str(contador) + " es igual a " + str(elevado_2))
#         contador = contador + 1
#         elevado_2 = 2**contador


# if __name__ == "__main__":
#     run()

# def run():
#     for i in range (6):
#         if i == 5:
#             print("figaroooo")
#             break
#         print("galileo")
        

# if __name__ == "__main__":
#     run()
from re import T


def es_primo(numero):
    contador = 0

    if numero <= 1:
        return False

    for i in range(1, numero + 1):
        if i == 1 or 1 == numero:
            continue
        if numero % i == 0:
            contador = contador + 1
            break
    if contador == 0:
        return True
    else:
        return False
            

def run():
    numero = int(input("Escribe un número bastardo: "))
    if es_primo == 0:
        print("no es un numero primo")
    else:
        print("es un numero primo")
    

if __name__ == "__main__":
    run()