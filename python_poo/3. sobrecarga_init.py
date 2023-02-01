# Python no permite la sobrecarga de los constructores

# Si intentamos hacerla, obtenemos un warning y un error
# al ejecutar, pues unicamente se tiene en cuenta la ultima definicion

# La sobrecarga de métodos es la creación de varios métodos con el mismo
# nombre pero con diferente lista de tipos de parámetros.


class Alumno:
    def __init__(self):
        self.nombre = "Por asignar"
        self.edad = 0
        self.calificacion = 0

    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre

        if edad >= 18:
            self.edad = edad

        if calificacion >= 0:
            self.calificacion = calificacion

        else:
            print("Calificacion invalida")
            self.calificacion

    def muestraDatos(self):
        print(self.nombre, self.edad, self.calification)


a1 = Alumno()
a1.muestraDatos()  # TypeError: Alumno.__init__() missing 3 required positional arguments: 'nombre', 'edad', and 'calificacion'
