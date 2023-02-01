# Conteo de referencia parte II

# El conteo de referencia puede disminuir:

# 1. Cuando una variable que se referencia al objeto es reasignada objeto2 =5
# 2. Cuando una variable local que referencia la objeto sale del ambito
# 3. Cuando el objeto es removido del contenedor milista.pop()
# 4. Cuando el conteo de referencia del contenedor es cero Ej:  del milista()
# 5. Cuando explicitamnete eliminamos la variable que referencia
# al objeto del objeto2

import sys


def imprimir(objeto):
    print("En la funcion")
    print(sys.getrefcount(objeto))
    print(objeto.__dict__)
    print("Fin de la funcion")


# creamos una clase
class clase1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


objeto1 = clase1(2, 3)
objeto2 = objeto1
objeto3 = objeto1
objeto4 = objeto1
milista = [objeto1]
milista2 = [objeto1]
imprimir(objeto1)  # Caso 2

print(sys.getrefcount(objeto1))

# Caso 1
objeto2 = 5
print(sys.getrefcount(objeto1))


# Caso 3
milista.pop()
print(sys.getrefcount(objeto1))

# Caso 4
del milista2
print(sys.getrefcount(objeto1))


# Caso 5
del objeto3
print(sys.getrefcount(objeto1))

objeto4 = None
print(sys.getrefcount(objeto1))
