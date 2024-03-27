'''
Este modulo esta dedicado a la creación de las clases mediante las cuales se van a estructurar todas las isntancias de nuestro juego
'''


#Clase padre(Pokemon):
class Pokemon:
    def __init__(self, nombre, vida , defensa, tipo, ataques = [], batallas_ganadas = 0, ps_max = 100):
        self.nombre = nombre #nombre dle pokemon
        self.stats = tuple([vida, defensa]) #stats del pokemon.
        self.tipo = tipo
        self.ataques = ataques
        self.batallas_ganadas = batallas_ganadas
        self.ps_max = ps_max
    def __repr__(self): #Representación del objeto pokemon dentro de un sistema de datos como array. Retorna un str
        return f'{self.tipo}'
    def __str__(self): #Representación del objeto pokemon al imprimirlo. Retorna un str
        return f'{self.name}'

#Tipos:

class Agua:
    def show(self) -> str:
        return 'Agua'

class Fuego:
    def show(self) -> str:
        return 'Fuego'

class Planta:
    def show(self) -> str:
        return 'Planta'

class Electrico:
    def show(self) -> str:
        return 'Electrico'

class Psiquico:
    def show(self) -> str:
        return 'Psiquico'

class Siniestro:
    def show(self) -> str:
        return 'Siniestro'

class Fantasma:
    def show(self) -> str:
        return 'Fantasma'

class Lucha:
    def show(self) -> str:
        return 'Lucha'

class Vuelo:
    def show(self) -> str:
        return 'Vuelo'

class Roca:
    def show(self) -> str:
        return 'Roca'

class Bicho:
    def show(self) -> str:
        return 'Bicho'

class Normal:
    def show(self) -> str:
        return 'Normal'




