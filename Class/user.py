#Clase dedicada a la creación  del usuario
class Pokeusuario:
    def __init__(self, nombre, genero, region_dor, pokemons = [], gimnasios = [], liga = False):
        self.nombre = nombre
        self.genero = genero
        self.region_dor = region_dor
        self.pokemons = pokemons
        self.gimnasios = gimnasios
        self.liga = liga
