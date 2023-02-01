# La sobrecarga de los operadores relacionales deben
# devolver un booleano para funcionar


class Libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __add__(self, otro):
        return self.paginas + otro.paginas

    def __gt__(self, otro):
        return self.paginas > otro.paginas


# Se debe tener en cuenta si es uniario o binario es decir si recibe
# uno o dos parametros

libro1 = Libro(50)
libro2 = Libro(300)

print(libro1 + libro2)

if libro1 > libro2:
    print("El segundo libro es mas grande")
else:
    print("El primer libro es mas grande")


# Si tenemos una clase con el mismo nombre de la sobrecarga nos
# permite llevar a cabo loa operacion
class revista:
    def __init__(self, paginas):
        self.paginas = paginas


revista1 = revista(25)

if libro1 > revista1:
    print("El  libro es mas grande")
else:
    print("La revista libro es mas grande")
