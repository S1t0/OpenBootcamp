import pickle

class Vehiculo:
    ruedas=0
    aceleracion=""
    velocidadPunta=0

    def __init__(self,ruedas, aceleracion,velocidadPunta):
        self.ruedas=ruedas
        self.aceleracion=aceleracion
        self.velocidadPunta=velocidadPunta



coche1=Vehiculo(4,"100kmh en 3 segundos",275)


#f=open("Ejercicios/Ejercicio2 entrada y salida/datos.bin","wb")
#pickle.dump(coche1,f)
#f.close()

f=open("Ejercicios/Ejercicio2 entrada y salida/datos.bin","rb")
potato=pickle.load(f)
f.close()
print(potato.aceleracion)

