import math


# Clase
class Vector:

    # Un constructor es un metodo que se invoca automaticamente cuando
    # el objeto es instanciado.
    # El constructor en python  es el metodo __new__,
    # pero se usa en casos avanzados.
    # El metodo init tambien se invoca automaticamente
    # en el proceso de instanciacion y es la opcion preferida para llevar
    # a cabo las inicializaciones del objeto en python.

    # Añadimos valores de defaut a los parametros
    def __init__(self, x=5, y=5):
        # Atributos, estos pueden ser usados en toda la clase
        self.x = x
        self.y = y

    def muestra(self):
        print(self.x, self.y)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)


# Creamos la instancia
v1 = Vector(4, 5)

# Invocamos al metodo
v1.muestra()

m = v1.magnitud()
print(m)
