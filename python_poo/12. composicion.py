# Se parece a la agregacion pero se diferencia en que
# en la composicion las instancias no tienen vidas separadas
# si se elimina la clase contenedora se eliminan las instancias de la
# clase contenida

# Ejemplo: Tengo mi clase auto pero si lo destruyo tambien daño el motor


# Creamos la clase contenida
class Motor:
    def __init__(self, cilindros, hp):
        self.cilindros = cilindros
        self.hp = hp

    def __repr__(self):
        return f"El motor de {self.cilindros} cilindros tiene {self.hp} hp"

    def trabajar(self):
        for i in range(self.hp):
            print(i, end=",")
        print()


class Auto:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

        # Hacemos la composicion
        # La instancia existe adentro de auto
        self.motor = Motor(4, 100)

    def __repr__(self):
        return f"El auto {self.modelo} con motor {self.motor} cuesta {self.precio}"

    def encender(self):
        print("Encendemos motor")
        self.motor.trabajar()


# Creamos un auto
auto1 = Auto("Brum200", 23000)
print(auto1)

auto1.encender()
