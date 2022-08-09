class Alumno:
    nombre=None
    nota=None

    def DarNombre(self,nombre):
        print("El alumno se llama",nombre)
    
    def Nota(self, nota):
        if nota>5:
            print("El alumno a sacado un",nota,"por lo que a aprobado")
        else:
            print("El alumno a scado un",nota,"por lo que a suspendido")


alumno1=Alumno()

alumno1.DarNombre("Andres")
alumno1.Nota(6)
