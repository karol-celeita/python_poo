# Python a diferencia de C# no tiene un mecanismo directo
# para definir interfaces

# Las interfaces nos permiten definir las propiedades y comportamientos
# de un objeto


# Con ellas podemos crear software que:
# -Depende de objetos que aun no existen pero que pueden existir en el futuro,
# como los plugins

# - Permite tener objetos intercambiables con el mismo comportamiento central
# pero con formas diferentes de implementarlo

# - Aisla la logica central de las dependecias externas

# Muchas bibliotecas usan interfaces, si vas a crear Apis necesitaras de
# interfaces y es una tecnica esperada en POO

# Existen varias formas de declarar interfaces en Python
# Informal
# Por clases abstractas
# Protocol#Esta tecnica se crea usando una clase normal

# Los metodos no se implementan, solo se colocan los annotations , es decir el
# tipo de parametro esperado y el valor de retorno
# y el docstring para documentar


class IAnimal:
    """Esta es la clase que defina la interfaz animal"""

    def colocaDatos(self, nombre: str, peso: float) -> bool:
        """
        Args:
            nombre (str): nombre del animal
            peso (float): peso del animal

        Returns:
            bool: Indica si el animal tiene sobrepeso
        """

    def caminar(self, metros: int):
        """
        Args:
            metros (int): Cantidad de metros que camina

        Returns: None
        """


# Para usar la interfaz necesitamos hacer una herencia y override
# a los metodos, para crear su implementacion


class Gato(IAnimal):
    def colocaDatos(self, nombre: str, peso: float) -> bool:
        self.nombre = nombre
        self.peso = peso

        if self.peso > 7:
            return True
        else:
            return False

    def caminar(self, metros: int):
        if metros > 70 and metros < 850:
            print("Tu gato camina lo suficiente")
        else:
            print("Vigila cuanto camina tu gato ")

    def __repr__(self) -> str:
        return f"Tu gato {self.nombre} pesa {self.peso} kg"


miGato = Gato()
print(miGato.colocaDatos("Michi", 6.5))
miGato.caminar(350)
print(miGato)
