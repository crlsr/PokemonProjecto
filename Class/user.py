'''
Este modulo es dedicado a la creación de la clase Usuario (clase la cual va a heredar de Entrenador)
'''

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
        self.batallas_ganadas = 0

    def add_win(self):
        self.batallas_ganadas += 1