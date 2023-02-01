# estas clases abs tiene metodos abs que se implemtan para las clases
# que desciendan de la clase abstracta

# Tenemos que import abc, permite crear clases abs
# importamos la clase y el decorador para el metodo abstracto

from abc import ABC, abstractmethod

# Creamos nuestra clase abstracta, desdecendiente de ABC
# con esto no vamos a poder crear instancias de la clase
# directamente, solo de quellas que descienden de ella


class Figura(ABC):

    # Creamos un metodo abstracto para el area
    # no tiene codigo en su interior es un metodo vacio
    # las clases hijas se ven obligadas a implemetarlo
    # Hacemos uso del decorador abstractmethod

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# Ahora creamos una clase que desciende de la figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4


# Ahora creamos otra clase que desciende de la figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.14159 * self.radio


# Comprobamos que no se puede instanciar Figura
# f1 = Figura()   TypeError: Can't instantiate abstract class Figura with abstract methods area, perimetro

# Instanciamos el cuadrado
c1 = Cuadrado(5)
print("El area es ", c1.area())
print("El perimetro es ", c1.perimetro())


# Instanciamos el cuadrado
c2 = Circulo(5)
print("El area es ", c2.area())
print("El perimetro es ", c2.perimetro())
