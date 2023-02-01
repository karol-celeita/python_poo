# Cuando trabajamos con variables en la clase, tenemos
# las variables de instancia. Estas variables se reconocen por que
# tienen el prefijo self y son las que hemos usado hasta el momento

# Tambien se tienen las variables de clase, que se definen y pertenecen a la
# clase y no a la instancia. estas variables existen independientemente de
# cuantas instancias se hayan creado

# Todos los objetos creados tienen acceso a las variables de clase
# usualmente se usan para definir una constante que todas las instancias puedan
# usar, tambien para contadores o para tener un valor compartido entre todas
# las instancias

# Funcionalmente se parecen a las variables estaticas de C#
# Se definen entre class y el primer def que tengamos


class cuentaBanco:
    tipoCambio = 20.22

    def __init__(self, cantidad):
        self.cantidad = cantidad

    # Asi se invoca una variable de clase
    def convertirDolares(self):
        print(self.cantidad / cuentaBanco.tipoCambio)


# Creamos un par de instancias
cuenta1 = cuentaBanco(500)
cuenta2 = cuentaBanco(2357)

# Invocamos al metodo
cuenta1.convertirDolares()
cuenta2.convertirDolares()

print("-------")

# Hacemos el cambio a la variable de clase
# El cambio es visto por todas las instancias
cuentaBanco.tipoCambio = 18.57
