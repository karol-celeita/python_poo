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


# Una desventaja de este metodo es que se puedent ener clases que no
# implementan la interfaz, por lo que ni hay garantia de que la interfaz es
# implementada. Estos metodos regresaran none


class Perro(IAnimal):
    pass


miPerro = Perro()
print(miPerro.colocaDatos("Teddy", 12))

# Para solucionar esto necesitamos levantar una excepcion de tipo
# NotImplementedError


class IAnimal2:
    """Esta es la clase que define la inferfaz IAnimal"""

    def colocaDatos(self, nombre: str, peso: float) -> bool:
        """
        Args:
            nombre (str): nombre del animal
            peso (float): peso del animal

        Returns:
            bool: Indica si el animal tiene sobrepeso
        """
        raise NotImplementedError

    def caminar(self, metros: int):
        """
        Args:
            metros (int): Cantidad de metros que camina

        Returns: None
        """

        raise NotImplementedError


class Tortuga(IAnimal2):
    pass


mitortuga = Tortuga()
print(mitortuga.colocaDatos("Leo", 0.34))


# Otra desventaja es que podemos intanciar como si fuera una clase normal
miInstancia = IAnimal()
