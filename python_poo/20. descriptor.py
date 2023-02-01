# Nos permiten hacer validacion de los tipos y valores que
# asignamos a un atributo


class Auto:
    def __init__(self, modelo, costo):
        self.modelo = modelo
        self.costo = costo

    def __repr__(self):
        return f"El auto {self.modelo}  cuesta {self.costo}"


# Como python no verifica los tipos podemos pasar informacion
# con los tipos que no se esperaban

miAuto = Auto(2018, "Mucho dinero")
print(miAuto)

# desde luego que podemos colocar en el __init__ codigo para verficar tipo o
# rangos pero podemos hacer un descriptor para que ese atributo
# tenga la verfificacion

# Creamos la clase ´para el descriptor


class costoDescriptor:
    def __init__(self):
        self.__costo = 0

    # Cuando leemos el atributo
    def __get__(self, instance, owner):
        return self.__costo

    def __set__(self, instance, valor):
        # Verificamos que sea del tipo
        if not isinstance(valor, int):
            raise TypeError("El costo debe ser un entero")
        # Verificamos que este en el rango

        if valor < 0 or valor >= 500000:
            raise ValueError("El costo debe ser mayor a 0 y menor a 50000")

        # Si todo esta bien , asignamos
        self.__costo = valor


# Redefinimos la clase
class Auto:
    # costo sera una instancia del descriptor
    costo = costoDescriptor()

    def __init__(self, modelo, costo):
        self.modelo = modelo
        self.costo = costo

    def __repr__(self):
        return f"El auto {self.modelo} cuesta {self.costo}"


miAuto = Auto(2018, -5)
print(miAuto)

miAuto = Auto(2018, 23000)
print(miAuto)
