import math


# Clase
class Vector:

    # Método
    # self es la referencia que invoca al metodo,
    # tambien se le conoce como variable de instancia

    def inicialize(self, x, y):
        # Atributos, estos pueden ser usados en toda la clase
        self.x = 0
        self.y = 0

    def muestra(self):
        print(self.x, self.y)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)


# Creamos la instancia
v1 = Vector()

# Invocamos al metodo
v1.inicialize(4, 5)
