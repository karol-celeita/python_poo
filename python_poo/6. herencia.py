# La herencia es una forma de la POO para llevar a cabo reutilizacion de codigo
# con la herencia creamos una relacion del tipo "es un "
# Tenemos una clase base que es extendida por la clase hija
# Adquiere todo lo que exite en la clase y adiciona lo suyo propio

# Hay una clase especial construida en el lenguaje llamado object
# Prevee ciertos metadatos y algunos comportamientos que le permiten
# a python tratar a todos los objetos de forma consistente

# Todos los objetos descienden de object, pero no neesitamos
# colocarlo de forma explicita, el leguaje lo hace por nosotros

import statistics as st


# Definimos la clase,esta sera la clase base
class Calificaciones:
    def __init__(self, lista):
        self.lista = lista

    def minimo(self):
        return min(self.lista)

    def maximo(self):
        return max(self.lista)


# Llevamos a cabo la herencia
# La clase de la cual desciende se coloca entre parentesis


class Estadistica(Calificaciones):

    # Adicionamos nuestros propios metodos
    def promedio(self):
        return st.mean(self.lista)

    def mediana(self):
        return st.median(self.lista)

    def moda(self):
        return st.mode(self.lista)


# Creamos la lista
calif = [5, 3, 2, 6, 9, 2, 4, 7, 8, 5, 62, 3, 5]

# creamos la instancia de calificaciones
MisCalifs = Calificaciones(calif)

# Invocamos sus metodos
print(MisCalifs.minimo())
print(MisCalifs.maximo())

print("----------")

# Creamos la instancia de la clase estadistica
MiEst = Estadistica(calif)

# Comprombamos metodos de la clase base
print(MiEst.maximo())

print(MiEst.promedio())
print(MiEst.moda())
print(MiEst.mediana())

# La clase base no tiene acceso a la clase hija
# print(MisCalifs.promedio())
