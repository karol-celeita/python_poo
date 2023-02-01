# Metodo __del__
# Cuando el objeto tiene un reference count de 0, Python puede eliminarlo
# antes de hacerko invoca automaticamente un metodo llamado __del__

# Es un buen lugar para hacer finalizaciones, cerrar archivos,
# cerrar una conexion de red, etc

# Conceptualmente es equivalente al destructor de otros lenguajes
# Si el objeto a ser destruido tiene variables de instancia que se referenciaan
# a otros objetos, en este caso los reference count de esos objetos tambien es
# decrementato y si llega a cero son eliminados

import sys


# creamos una clase
class clase1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print("El objeto esta por ser destruido")
        print("Bye")


objeto1 = clase1(1, 3)
objeto2 = objeto1
print(sys.getrefcount(objeto1))

objeto2 = None
objeto1 = None
