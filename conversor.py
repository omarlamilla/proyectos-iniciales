menu = """elige el tipo de peso que quieres convertir a dolares

1 - Peso colombiano
2 - Peso argentino
3 - Peso mexicano

Elige una opción: """


opcion = input(menu)


def tipo_peso(tipopeso, valordolar):
    peso = input("¿Cuantos pesos " + tipopeso + " tienes?: ")
    peso = float(peso)
    valor_dolar = valordolar
    dolar = peso / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tienes $" + dolar + " dolares")


if opcion == "1":
    tipo_peso("colombiano", 4200)
elif opcion == "2":
    tipo_peso("argentino", 127)
elif opcion == "3":
    tipo_peso("mexicano", 20)
else:
    print("elige una opción care mondá")


   


