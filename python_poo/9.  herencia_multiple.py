# Creamos una primera clase
# En lo general no se recomienda utilizarla
# Es cuando una clase desciende de dos clases o mas


class Producto:
    def __init__(self, cantidad, costo):
        self.cantidad = cantidad
        self.costo = costo

    def calculaTotal(self):
        self.total = self.cantidad * self.costo
        print("Se tiene en total $", self.total)

    def muestraProducto(self):
        print("Se tienen", self.cantidad, "productos")
        print("El costo del producto es", self.costo)
        self.calculaTotal()


# Creamos otra clase
class Fruta:
    def __init__(self, nombre, origen):
        self.nombre = nombre
        self.origen = origen

    def muestraFruta(self):
        print("Fruta", self.nombre)
        print("Origen", self.origen)


# Creamos una clase con herencia multiple


class Articulo(Producto, Fruta):
    def __init__(self, nombre, origen, cantidad, costo):
        Fruta.__init__(self, nombre, origen)
        Producto.__init__(self, cantidad, costo)

    def muestraArticulo(self):
        Fruta.muestraFruta(self)
        Producto.muestraProducto(self)


manzana = Articulo("manzana", "Mexico", 500, 20.36)
manzana.muestraArticulo()

# La idea es saber que existe , pero no es recomendable porque
# puede llevar a problemas dificiles de corregir, como el problema del diamante
