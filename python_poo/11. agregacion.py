# Forma de extender propiedades de un objeto sin usar la herencia
# usando un objeto contenido que tenga las propiedades que necesitamos
# El obj contenedor y el obj contenido tienen vidas independientes
# es decir que si ese elimina no afecta al otrp

# Creamos la clase contenida
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f" El libro es {self.titulo} por {self.autor}"


# Creamos la clase contenedora
class Biblioteca:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

        # Lo que hacemos es inicializar un metodo en none y
        # luego hacer la agregacion
        self.libro = None

    def muestraBilioteca(self):
        print(self.nombre)
        print(self.ciudad)

        # Verificamos si esta variable que referencia al objeto
        # ya tiene la referencia o no
        if self.libro is None:
            print("Dona libros a la bilbioteca")
        else:
            print(self.libro)

    # Sera el que adiciona el libro en la biblioteca
    # Como python no esta fuertemente tipificado hay que verificar que sea del
    # tipo que hay que agregar, para eso usamos isinstance, esta retorna true
    # si esa instancia pertenece a determinada clase

    def AgregaLibro(self, libro):
        if isinstance(libro, Libro):
            self.libro = libro

        else:
            print("Coloca un libro")


# Creamos un libro
libro1 = Libro("Programacion avanzada", "Nicosio")
biblioteca1 = Biblioteca("Biblioteca Central", "NYC")

biblioteca1.muestraBilioteca()
print("-----")

# Hacemos la agregacion
# Si bilioteca desaparece libro sigue existiendo

biblioteca1.AgregaLibro(libro1)
biblioteca1.muestraBilioteca()
print("-----")

# Intentamos hacer agregacion erronea
biblioteca1.AgregaLibro("hola")
