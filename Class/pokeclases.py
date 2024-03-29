'''
Este modulo esta dedicado a la creación de las clases mediante las cuales se van a estructurar todas las instancias para los pokemones de nuestro juego
-> Creación de pokemones
-> Creación de Ataques
-> Creación de enemigos
'''
# Entrenador, clase que maneja a los pokemon, que maneja a las clases tipo y ataque

class Trainer:
    def __init__(self, nombre, pokemones = None, objetos = None):
        self.nombre = nombre
        if pokemones is None:
            pokemones = []
        self.pokemones = pokemones
        if objetos is None:
            objetos = []
        self.objetos = objetos

#Pokemon, posee atributos ataque y tipo, las interacciones de daño no se guardan en el porque requieren de datos de otro pokemon:
class Pokemon:
    def __init__(self, nombre, ps_max, defensa_fisica= None, defensa_especial = None, ataque_fisico = None, ataque_especial = None, velocidad = None, tipos = None, ataques=None):
        self.nombre = nombre #nombre dle pokemon
        self.ps_max = ps_max
        #ps_actuales es el que se modifica, nunca modificar ps_max, no tenemos niveles
        self.ps_actuales = ps_max
        self.defena_stats = (defensa_fisica, defensa_especial)
        self.ataque_stats = (ataque_fisico, ataque_especial)
        self.velocidad = velocidad
        if tipos is None:
            tipos = []
        self.tipos = tipos
        if ataques is None:
            ataques = []
        self.ataques = ataques
        self.batallas_ganadas = 0
    def __repr__(self): #Representación del objeto pokemon dentro de un sistema de datos como array. Retorna un str
        return f'{self.name}'
    def __str__(self): #Representación del objeto pokemon al imprimirlo. Retorna un str
        return f'{self.name}'

#Ataque
    
class Ataque:
    def __init__(self, name, type = None, damage = None, damage_type = None):
        self.name = name
        if type is None:
            type = object
        self.type = type
        if damage is None:
            damage = 0
        self.damage = damage
        self.damage_type = damage_type

    def get_type(self):
        return self.type

    def get_damage(self):
        return self.damage
    
    def get_attack_type(self):
        return self.damage_type
    
    def get_name(self):
        return f'{self.name}'
    
    def show(self):
        return "{}, Tipo: {}, Daño: {}, {}".format(self.name, self.type.show(), self.damage, self.damage_type)
    
    def __repr__(self) -> str:
        return f'{self.name}'

#Tipos:

class Normal:
    Resistencia = []
    Inmunidades = ["Fantasma"]
    Debilidades = ["Lucha"]

    def show(self) -> str:
        return 'Normal'

class Lucha:
    Resistencia = ["Roca", "Bicho", "Siniestro"]
    Inmunidades = []
    Debilidades = ["Volador", "Psiquico"]
    def show(self) -> str:
        return 'Lucha'

class Volador:
    Resistencia = ["Lucha", "Bicho", "Planta"]
    Inmunidades = ["Tierra"]
    Debilidades = ["Roca", "Electrico", "Hielo"]
    def show(self) -> str:
        return 'Volador'

class Veneno:
    Resistencia = ["Lucha", "Veneno", "Bicho", "Planta"]
    Inmunidades = []
    Debilidades = ["Tierra", "Psiquico"]
    def show(self) -> str:
        return 'Veneno'

class Tierra:
    Resistencia = ["Veneno", "Roca"]
    Inmunidades = ["Electrico"]
    Debilidades = ["Agua", "Planta", "Hielo"]
    def show(self) -> str:
        return 'Tierra'

class Roca:
    Resistencia = ["Normal", "Volador", "Veneno", "Fuego"]
    Inmunidades = []
    Debilidades = ["Lucha", "Tierra", "Acero", "Agua", "Planta"]
    def show(self) -> str:
        return 'Roca'

class Bicho:
    Resistencia = ["Lucha", "Tierra", "Planta"]
    Inmunidades = []
    Debilidades = ["Volador", "Roca", "Fuego"]
    def show(self) -> str:
        return 'Bicho'

class Fantasma:
    Resistencia = ["Veneno", "Bicho"]
    Inmunidades = ["Normal", "Lucha"]
    Debilidades = ["Fantasma", "Siniestro"]
    def show(self) -> str:
        return 'Fantasma'

class Acero:
    Resistencia = ["Normal", "Volador", "Roca", "Bicho", "Acero", "Planta", "Psiquico", "Hielo", "Dragon"]
    Inmunidades = ["Veneno"]
    Debilidades = ["Lucha", "Tierra", "Fuego"]
    def show(self) -> str:
        return 'Acero'

class Fuego:
    Resistencia = ["Bicho", "Acero", "Fuego", "Planta"]
    Inmunidades = []
    Debilidades = ["Tierra", "Roca", "Agua"]
    def show(self) -> str:
        return 'Fuego'

class Agua:
    Resistencia = ["Acero", "Fuego", "Agua", "Hielo"]
    Inmunidades = []
    Debilidades = ["Planta", "Electrico"]
    def show(self) -> str:
        return 'Agua'

class Planta:
    Resistencia = ["Tierra", "Agua", "Planta", "Electrico"]
    Inmunidades = []
    Debilidades = ["Volador", "Veneno", "Bicho", "Fuego", "Hielo"]
    def show(self) -> str:
        return 'Planta'

class Electrico:
    Resistencia = ["Volador", "Acero", "Electrico"]
    Inmunidades = []
    Debilidades = ["Tierra"]
    def show(self) -> str:
        return 'Electrico'

class Psiquico:
    Resistencia = ["Lucha", "Psiquico"]
    Inmunidades = []
    Debilidades = ["Bicho", "Fantasma", "Siniestro"]
    def show(self) -> str:
        return 'Psiquico'

class Hielo:
    Resistencia = ["Hielo"]
    Inmunidades = []
    Debilidades = ["Lucha", "Roca", "Acero", "Fuego"]
    def show(self) -> str:
        return 'Hielo'

class Dragon:
    Resistencia = ["Fuego", "Agua", "Planta", "Electrico"]
    Inmunidades = []
    Debilidades = ["Hielo", "Dragon"]
    def show(self) -> str:
        return 'Dragon'

class Siniestro:
    Resistencia = ["Fantasma", "Siniestro"]
    Inmunidades = ["Psiquico"]
    Debilidades = ["Lucha", "Bicho"]
    def show(self) -> str:
        return 'Siniestro'

