from functools import reduce

i=input("Dame una lista de numeros separada por espacios:\n")

lista=i.split(" ")
for i in range(len(lista)):
    lista[i] = int(lista[i])

print(lista)

def miFuncion(x):
    if x%2==0:
        return False

    return True

numerosImpares=list(filter(miFuncion,lista))
print("Los numeros impares de la lista son",numerosImpares)

def funcionSuma(a,b):
    return a+b

print("La suma total de los numeros impares es",reduce(funcionSuma,numerosImpares))