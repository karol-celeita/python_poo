# Otra forma de crear interfaces es por medio de clases abstractas
# Al usarlas se resuelven algunos de los problemas que se tienen
# con las interfaces informales

# Creamos la interfaz con la clase que hereda de ABC el decorador
# abstacmethod es usado para los metodos

# Con esta tecnica obtenemos:
# Claridad , se nota que no es una clase comun
# Al ser abstracta, desde luego se debe de implementar
# Si no implementamos un metodo se levanta una excepcion
# Si intentamos instanciar obtenemos una excepcion

# La desventaja que tiene, es que es muy general,
# no sabemos si la clase es una interfaz o si es otra cosa

from abc import ABC, abstractmethod


class IAnimal(ABC):
    """Esta esla clase que define la interfazIAnimal"""

    @abstractmethod
    def colocaDatos(self, nombre: str, peso: float) -> bool:
        """
        Args:
            nombre (str): nombre del animal
            peso (float): peso del animal

        Returns:
            bool: Indica si el animal tiene sobrepeso
        """

    @abstractmethod
    def caminar(self, metros: int):
        """
        Args:
            metros (int): Cantidad de metros que camina

        Returns: None
        """


# Para usar la interfaz necesitamos hacer  herencia y override
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


# Ejemplo sin un metodo de la interfaz


class Perro(IAnimal):
    def caminar(self, metros: int):
        if metros > 70 and metros < 850:
            print("Tu perro camina lo suficiente")
        else:
            print("Vigila cuanto camina tu perro ")


miPerro = Perro()


# Tampoco podemos instanciar directamente
miOtroGato = IAnimal()
