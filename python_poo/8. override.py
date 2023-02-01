# Hacemos override a la clase base cuando
# La clase hija ve que necesita una version diferente al metodo
# que usa la clase base, es decir no le sirve, pero si necesita ese metodo
# Oveeride sobreecibe este metodo de acuerdo a sus necesidades, unicamente en su clase


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

        super().__init__(nombre, edad)
        self.sueldo = sueldo
        self.puesto = puesto

    # Hacemos el override simplemente al definir de nuevo el metodo

    def mayorEdad(self):
        if self.edad >= 25:
            print("Bienvenido a la empresa")
            return True
        else:
            print("La empresa no contrata a menores de 25")
            return False

    # Hacemos override  a muestraDatos
    def muestraDatos(self):

        print("Nombre ", self.nombre)
        if self.mayorEdad() == True:
            print("---Información del empleado ---", self.puesto)
            print("Puesto ", self.puesto)
            print("Sueldo $", self.sueldo)


# Creamos una instancia
p1 = Persona("Ana", 25)

print(p1.mayorEdad())
p1.muestraDatos()

print("--------")

e1 = Empleado("Juan", 22, 15000, "Analista")
print(e1.mayorEdad())
e1.muestraDatos()
