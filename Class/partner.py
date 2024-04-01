#Clase dedicada a la creación del compañero humano
class Pokecompañero:
    def __init__(self, nombre, pokemons = None):
        self.nombre = nombre
        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons