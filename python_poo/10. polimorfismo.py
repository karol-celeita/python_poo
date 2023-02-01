# Significa muchas formas, podemos tener una variable que puede adquirir
# diferentes referencias a objetos


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"El nombre es {self.nombre}"

    # Este metodo es generico y se va  adaptar al animal
    def Moverse(self):
        print("El animal se mueve")


class Perro(Animal):
    def Moverse(self):
        print(f" El perro {self.nombre} camina")


class Pez(Animal):
    def Moverse(self):
        print(f" El pez {self.nombre} nada")


class Reptil(Animal):
    def Moverse(self):
        print(f" El reptil {self.nombre} se arrastra")


# Tenemos una referencia y podemos trabajar
# con cualquier objeto que descienda al animal


def trabajaAnimal(animal):
    print(animal)
    animal.Moverse()


print("Que mascota quieres?")
print("1-Perro, 2-Pez, 3-Reptil")
opcion = int(input())

nombre = input("Que nombre tiene?")

if opcion == 1:
    miMascota = Perro(nombre)
elif opcion == 2:
    miMascota = Pez(nombre)
else:
    miMascota = Reptil(nombre)

# Invocamos a trabajaAnimal que funciona de forma polimorfica
trabajaAnimal(miMascota)

# Otro ejemplo

m1 = Perro("Max")
m2 = Pez("Dory")
m3 = Reptil("Drago")

mascotas = [m1, m2, m3]

for mascota in mascotas:
    print(mascota)
    mascota.Moverse()
