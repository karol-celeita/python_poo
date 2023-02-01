# Es una opcionnueva que viene con el PEP544 para Python.
# Es una forma implicita de declarar interfaces
# Solo es de ayuda si hacemos uso de type hints y verficacion
# estatica de tipos

# Es similar a las interfaces anteriores
# Type hints: son los valores que indicamos que recibe y retorna una clase

from typing import Protocol


class IAnimal(Protocol):
    """Esta esla clase que define la interfazIAnimal"""

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
