'''
Este modulo esta dedicado a la creación de las clases mediante las cuales se van a estructurar todas las isntancias de nuestro juego
'''


#Clase padre(Pokemon):
class Pokemon:
    def __init__(self, nombre, vida, defensa):
        self.nombre = nombre #nombre dle pokemon
        self.stats = int(tuple(vida, defensa)) #stats del pokemon

#Clase para la creación de ataques
class Ataques:
    def __init__(self, daño, efecto):
        self.daño = int(daño)
        self.efecto = int(efecto)
        
        
#Clases hijo(Pokemon):
class PokemonFuego(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonAgua(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonLucha(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonPsiquico(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonVuelo(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonNormal(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]
    
class PokemonBicho(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]

class PokemonRayo(Pokemon):
    def __init__(self, nombre, vida, defensa, ataques):
        super().__init__(nombre, vida, defensa)
        self.ataques = [ataques]



#Clase dedicada a la creación  del usuario
class Pokeusuario:
    def __init__(self, nombre, genero, regiondor, pokemon):
        self.nombre = nombre
        self.genero = genero
        self.regiondor = regiondor
        self.pokemon = [pokemon]

#Clase dedicad aa la creación de rutas
class PokeRutas:
    def __init__(self) -> None:
        pass


#Clase dedicada a la creación del compañero humano
class Pokecompañero:
    def __init__(self) -> None:
        pass
