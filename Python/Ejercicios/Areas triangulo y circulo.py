from math import pi

#Area del triangulo
base=float(input("Introduce la base del triangulo"))
altura=float(input("Introduce la altura"))

def area(a,b):
    return (a*b)/2

print("El area del triangulo es",area(base,altura))


#Area del circulo

radio=float(input("Introduce el radio del circulo"))

def areaCirculo(a):
    return pi*a*a

print(areaCirculo(radio))
