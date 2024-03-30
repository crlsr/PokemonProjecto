#Clase dedicada a la creación  del usuario
class Pokeusuario:
    def __init__(self, nombre, genero, region_dor, pokemons = None, gimnasios = None, liga = False, objects = None , pokecoins = 0):
        self.nombre = nombre
        self.genero = genero
        self.region_dor = region_dor
        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons
        if gimnasios is None:
            gimnasios = []
        self.gimnasios = gimnasios
        self.liga = liga
        if objects is None:
            objects = []
        self.objects = objects
        self.pokecoins = pokecoins
