from pokeclases import Trainer
class Pokeusuario(Trainer):
    def __init__(self, nombre, genero, region_dor, pokemons = None, gimnasios = None, liga = False, objects = None , pokecoins = 0):
        super().__init__(nombre, pokemons, objects)
        self.genero = genero
        self.region_dor = region_dor
        if gimnasios is None:
            gimnasios = []
        self.gimnasios = gimnasios
        self.liga = liga
        self.pokecoins = pokecoins