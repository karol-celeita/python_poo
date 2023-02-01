# La serializacion permite tomar el estdo de un objeto y
# colocarlo en un medio de almacenamiento o transmitirlo

# pickle es una libreria para esto pero tiene algunos problemas
# de seguridad, se pueden modificar los archivos creados con pickle
# usar solo paa guardar datos en el pc local

import pickle


class Auto:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

    def __repr__(self):
        return f"Mi auto {self.modelo} cuesta {self.precio}"


miauto = Auto("runrun200", 28000)
print(miauto)

# Salvamos el objeto

# Abrimos el archivo para escritura que pide dos parametros, el nombre del
# archivo con extension opcional y los permisos w write,b para formato binario

autoOut = open("miobjeto", "wb")

# Pasamos el objeto y el archivo
pickle.dump(miauto, autoOut)

# cerramos el archivo
autoOut.close()


# Hacemos la lectura

# abrimos el archivo para lectura
autoIn = open("miobjeto", "rb")

# Leemos el archivo
auto2 = pickle.load(autoIn)

# Crea una nueva instancia del estado del objeto
print(auto2)
