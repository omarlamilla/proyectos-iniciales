import random

def run():
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Introduce un numero: "))
    vidas = 7
    while numerorandom != numeroelegido :
        if numeroelegido < numerorandom : 
            vidas -= 1
            if vidas == 0:
                print("paila te jodiste v: ")
                break
            print("Elige un numero mas grande parcero.")
        elif numeroelegido > numerorandom: 
            vidas -= 1
            if vidas == 0:
                print("paila, te jodiste v: ")
                break
            print("Elige un numero mas pequeño parcero.")
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce numero: "))
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()