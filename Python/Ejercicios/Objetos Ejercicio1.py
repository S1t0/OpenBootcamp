
class Vehiculo:
    color="Rojo"
    ruedas =4
    Puertas=5


class Coche(Vehiculo):
    Velocidad=150
    Cilindrada=1900


coche1=Coche()

print("El coche es de color",coche1.color, "con",coche1.Puertas,"puertas,alcanza una velocidad de",coche1.Velocidad,"y con una cilindrada de",coche1.Cilindrada,"cc")
