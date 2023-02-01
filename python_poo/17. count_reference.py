# Tiempo de vida del objeto

# El tiempo que pasa desde la instanciacion del objeto hasta que es destruido
# se conoce como tiempode vida del objeto

# Conteo de referencia
# En python los programadores no se deben preocupar por el manejo de memoria
# pero es bueno conpmrender que es lo que sucede en el lenguaje
# cuando un programa instancia un objetom se reserva parte de la memoria para
# guardar las variables de instacia de esa clase

# Cada objeto tiene un campo interno que se conoce cono conteo de referencia
# este nos indica cuantas variables diferentes se refieren al mismo objeto

# Incremento de reference count
# 1. Cuando una variable adicional es asignada al mismo objeto
#    objeto2=objeto1

# 2. Cuando un objeto se pasa a una funcion y la variable del parametro local
# es referenciada al objeto
#   mifuncion(objeto1)

# 3. Cuando un objeto es colocado en un contenedor como una lista o diccionario
# milista[objeto1, objeto2, objeto3]

import sys


# creamos una clase
class clase1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


objeto1 = clase1(2, 3)


# Imprimimos su conteo de referencia
# El valor quiza confunda pero en la documentacion leemos que
# el valor regresado es generalmente mayor en 1 por que incluye la
# referencia temporal como argumento al invocar getfercount

print(sys.getrefcount(objeto1))

# Asignamos variable adicional caso 1
objeto2 = objeto1
print(sys.getrefcount(objeto1))


# Asignamos variable adicional caso 3
milista = [objeto1]
print(sys.getrefcount(objeto1))


# Si creamos una nueva instancia cada quien tiene su reference count
objeto3 = clase1(8, 9)
print(sys.getrefcount(objeto1))
print(sys.getrefcount(objeto3))
