# Python ve todos los metodos y datos como si todos fuera publicos y
# deja a voluntad del programador el acceso al dato

# Para indicar que un dato es privado se recomienda colocar la
# informacion en el docstring

# Por convencion si deseamos que sea privado colocamos
# un guion bajo antes de la variable


class Producto:
    def __init__(self) -> None:
        self.cantidad = 10

        # Indicamos que cosro es privado
        self._costo = 5


# Creamos la instancia
manzana = Producto()

# Usamos cantidad
print(manzana.cantidad)

# Ahora que usamos costo aunque no deberiamos
# por  estar indicado como privado, pero nada en el
# lenguaje nos impide usarlo

print(manzana._costo)
manzana._costo = 56
print(manzana._costo)

# El usar _ es por convencion
# El usar __ no es una convencion. se usa para evitar
# colisiones cuando se definen las subclases
# Esto se llama mangling, el interprete cambia el nombre para que sea
# menos posible tener coliciones si la clase se extiende


class Producto2:
    def __init__(self) -> None:
        self.cantidad = 10

        # Indicamos que el costo es privado
        self._costo = 5

        # Creamos el atributo con __
        self.__impuesto = 0.16


# Al usar __ podemos pensar que tenemos un acceso privado pero no es asi

pera = Producto2()

print(pera.cantidad, pera._costo)
# print(pera.__impuesto)
# AttributeError: 'Producto2' object has no attribute '__impuesto'

# Veamos por que sucede
# Al nombre del atributo se le ha adicionado _Producto2

# dir(pera)

# Si ponemos el nombre completo podemos hacer uso directo de este
# lo que comprueba que no es un atributo privado, esto se llama name_mangling


print(pera._Producto2__impuesto)


#El usar _ al final de una variable es usado para evitar conflictos 
# con palabras reservadas de python

def funcion1(class, nombre):
    pass

#Aqui no pone problema si nuestra variable se llama class
def funcion1(class_, nombre):
    pass