def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es un palindromo bro")
    elif es_palindromo == False:
        print("No es un palindromo bro")

    


if __name__ == "__main__":
    run()

#Esto es la prueba para hacer un push con llave ssh a github