# Veamos algunos ejemplos basicos, estos son faciles porque ñas
# funcionalidades ya viene incorporadas en el lenguaje
a = 5
b = 6
print(a + b)

c = "hola"
d = " a todos"
print(c + d)


class Contenedor:
    def __init__(self, litros):
        self.litros = litros


c1 = Contenedor(12)
c2 = Contenedor(15)
# Ahora que pasaria si tengo mi clase con litros y quiero sumar estos dos
# print(c1 + c2) TypeError: unsupported operand type(s) for +: 'Contenedor' and 'Contenedor'

# Se resuelve a traves de sobrecarga de operadores, por medio de reglas
# le enseñamos como sumar


class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __add__(self, otro):
        return self.paginas + otro.paginas


# Se debe tener en cuenta si es uniario o binario es decir si recibe
# uno o dos parametros

libro1 = Libro(50)
libro2 = Libro(300)

print(libro1 + libro2)
# El sumando de la izquierda invoca la funcion y el de la derecha siempre
# se pasa como parametro

# Para el contenedor quedaria entonces:


class contenedor:
    def __init__(self, litros):
        self.litros = litros

    def __add__(self, otro):
        return contenedor(self.litros + otro.litros)

    def __repr__(self):
        return f" El contenedor tiene {self.litros} litros"


c1 = contenedor(15)
c2 = contenedor(25)
c3 = c1 + c2
print(c3)
