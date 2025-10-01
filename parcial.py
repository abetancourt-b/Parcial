# Autor: Antonio Betancourt

#Ejercicio 1: Cree un algoritmo que lea 5 números enteros uno por uno e identifique cuáles son positivos y pares. Al final, debe mostrar la suma total de esos números.
def Primerejercicio():
    for x in range(0,5):
        x = int(input("Ingrese un numero entero: "))
# 1/2 = 0.5 pero 11/2 = 5.5
        if((x > 0) and ((x / 2) == (x // 2))):
            print(x, "Es par y positivo")
            participa = x
            participa += x
        else:
            print("No cumple con los requisitos de la suma")
        print("La suma de los que participan es: ", participa)

#Ejercicio 2: Diseñe un programa que lea la edad de una persona y muestre un mensaje según el siguiente criterio:
def Segundopunto:
edad = int(input("Ingrese su edad: "))
if 0 < edad < 13:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 59:
    print("Adulto")
elif edad >= 60:
    print("Adulto mayor")
else:
    print("ERROR, ese numero no puede estar en este programa")

#Ejercicio 3 Solicite al usuario que escriba una palabra (sin espacios) y cuente cuántas vocales tiene. El programa debe ser sensible a mayúsculas y minúsculas (es decir, contar tanto a como A).
def Tercerpunto():
    palabra = input("Escriba una palabra sin espacios: ")

    print("\nLa palabra tiene: ")
    letraA = palabra.count("A")
    letraa = palabra.count("a")
    print("\na | A: ", letraa, "|", letraA)
    letraE = palabra.count("E")
    letrae = palabra.count("e")
    print("\ne | E: ", letrae, "|", letraE) 
    letraI = palabra.count("I")
    letrai = palabra.count("i")
    print("\ni | I: ", letrai, "|", letraI)
    letraO = palabra.count("O")
    letrao = palabra.count("o")
    print("\no | O: ", letrao, "|", letraO)
    letraU = palabra.count("U")
    letrau = palabra.count("u")
    print("\nu | U: ", letrau, "|", letraU)






