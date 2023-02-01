# Se usa para reusar codigo de la clase base


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def muestraDatos(self):

        print("el nombre es", self.nombre)
        print("la edad es", self.edad)


# Hacemos una herencia


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, puesto):

        # Por medio de super() invocamos metodos que existan en la clase base
        # Y podemos reusar este codigo

        # Aprovechamos que el init ya inicializa algunos atributos
        super().__init__(nombre, edad)

        # Ahora inicializamos los propios
        self.sueldo = sueldo
        self.puesto = puesto

    def muestraDatos(self):

        # Aprovechamos el muestraDatos de Persona
        super().muestraDatos()

        # Adicionamos los propios
        print("el puesto es", self.puesto)
        print("el sueldo es", self.sueldo)


# Creamos una instancia
p1 = Persona("Ana", 25)

print(p1.mayorEdad())
p1.muestraDatos()

print("--------")

e1 = Empleado("Juan", 30, 15000, "Analista")
print(e1.mayorEdad())
e1.muestraDatos()
