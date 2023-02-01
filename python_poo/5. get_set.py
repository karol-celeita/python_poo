# Las funciones de interfaz permiten acceder a  atributos
# privados,de acuerdo a las reglas del objeto
# Podemos poner codigo de seguridad para recibir o enviar info al objeto
# Si los atributos siempre son publicos en Python se uisan get y set
# get para leer informacion del objeto desde el exterior
# set es para colocar valores dese el exterior del objeto

# Creamos una clase
class Producto:
    def __init__(self, costo):
        self._costo = costo

        # Invocamos un metodo de la propia clase
        self._precioventa = self._calculaPVenta()

    # Este metodo se considera privado
    def _calculaPVenta(self):
        return self._costo * 1.30

    # Creamos el getter para el atributo precioventa
    # Si la funcion va a actuar de getter se debe poner get al inicio

    def getPrecioVenta(self):
        return self._precioventa

    # Creamos el setter para el atributo costo
    def setCosto(self, valor):

        # Podemos colocar codigo de seguridad
        if valor > 0:
            self._costo = valor
            self._precioventa = self._calculaPVenta()

        else:
            print("Valor invalido")
            self.costo = 0

    # Creamos el getter de costo
    def getCosto(self):
        return self._costo

    # Usamos __repr__ para facilitar la impresion
    def __repr__(self):
        return f"Costo=${self._costo}, Precio venta=${self._precioventa}"


# Creamos el objeto
manzana = Producto(12.5)

# imprimimos
print(manzana)

# Obtenemos el precio venta
pv = manzana.getPrecioVenta()
print("el impuesto es $", pv * 0.16)

manzana.setCosto(-11.20)

# modificamos el costo
print(manzana.getCosto())

# Imprimimos el objeto
print(manzana)
