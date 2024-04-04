'''
Este modulo esta dedicado a la creación de las clases mediante las cuales se van a estructurar todas las instancias para los pokemones de nuestro juego
-> Creación de pokemones
-> Creación de Ataques
-> Creación de enemigos
'''
# Entrenador, clase que maneja a los pokemon, que maneja a las clases tipo y ataque
#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from funtions.funciones import validation, int_validatión
class Trainer:
    def __init__(self, nombre, pokemones = None, objetos = None, ubicacion = None):
        self.nombre = nombre
        if pokemones is None:
            pokemones = []
        self.pokemones = pokemones
        if objetos is None:
            objetos = []
        self.objetos = objetos
        self.ubicacion = ubicacion
    def get_pokes(self):
        array = []
        for i in self.pokemones:
            array.append(i.nombre)
        return array
    
    def obj_num(self):
        return len(self.objetos)
    

    def reset_stats_pkmn(self):
        for pokemon in self.pokemones:
            pokemon.reset_stats()
    def get_available_pokemon(self):
        number_of_pokemon = len(self.pokemones)
        for pokemon in self.pokemones:
            if pokemon.Is_Alive() is False:
                number_of_pokemon -= 1
        return number_of_pokemon
    def get_name(self):
        return self.nombre
    def get_next_pokemon(self):
        for pokemon in self.pokemones:
            if pokemon.Is_Alive() is True:
                return pokemon
        return None
    def get_objects(self):
        return self.objetos
    
    def __repr__(self) -> str:
        return f'{self.nombre}'


#Usuario Pokemon
class Pokeusuario(Trainer):
    def __init__(self, nombre, genero, region_dor, pokemons = None, gimnasios = None, liga = False, objects = None , pokecoins = 0, final_position = None):
        super().__init__(nombre, pokemons, objects)
        self.genero = genero
        self.region_dor = region_dor
        if gimnasios is None:
            gimnasios = []
        self.gimnasios = gimnasios
        self.liga = liga
        self.pokecoins = pokecoins
        self.batallas_ganadas = 0
        if final_position is None:
            final_position = 0
        self.final_position = final_position

    def add_win(self):
        self.batallas_ganadas += 1

    def check_for_new_move(self):
        if self.batallas_ganadas % 3 == 0:
            return True
        return False
    
    def get_medallas(self):
        array = []
        for i in self.gimnasios:
            array.append(i)
        return array
    
    def get_objetos(self):
        array = []
        for i in self.objetos:
            array.append(i.nombre)
        return array

#Objetos, para aumentar la vida, ataque, defensa
class Objeto:
    def __init__(self, nombre, mod_vida=0, mod_ataque=1, mod_defensa=1):
        self.nombre = nombre
        self.mod_vida = mod_vida
        self.mod_ataque = mod_ataque
        self.mod_defensa = mod_defensa
    def get_life(self):
        return self.mod_vida
    def get_attack(self):
        return self.mod_ataque
    def get_defense(self):
        return self.mod_defensa
    def get_name(self):
        return self.nombre

#Pokemon, posee atributos ataque y tipo, las interacciones de daño no se guardan en el porque requieren de datos de otro pokemon:
class Pokemon:
    def __init__(self, nombre, ps_max, defensa_fisica= None, defensa_especial = None, ataque_fisico = None, ataque_especial = None, velocidad = None, tipos = None, ataques=None, batallas_ganadas = None):
        self.nombre = nombre #nombre del pokemon
        self.ps_max = ps_max
        #ps_actuales es el que se modifica, nunca modificar ps_max, no tenemos niveles
        self.ps_actuales = ps_max
        self.defensa_stats = (defensa_fisica, defensa_especial)
        self.defensa_temp = self.defensa_stats
        self.ataque_stats = (ataque_fisico, ataque_especial)
        self.ataque_temp = self.ataque_stats
        self.velocidad = velocidad
        if tipos is None:
            tipos = []
        self.tipos = tipos
        if ataques is None:
            ataques = []
        self.ataques = ataques
        if batallas_ganadas is None:
            batallas_ganadas = 0
        self.batallas_ganadas = batallas_ganadas
    
    def get_name(self):
        return self.nombre
    
    def default_fix(self):
        self.ataques.append(Ataque('Placaje', Normal, 40, 'Fisico'))

    def get_types(self):
        array = []
        for i in self.tipos:
            array.append(i.show(i))
        return array
    
    def get_types_object(self):
        return self.tipos

    def get_attacks(self):
        return self.ataques
    
    def get_speed(self):
        return self.velocidad

    def load_ps(self, ps):
        self.ps_actuales = ps

    def Update_hp(self, change_hp):
        if self.ps_actuales + change_hp > self.ps_max:
            self.ps_actuales = self.ps_max
        elif self.ps_actuales <= 0:
            self.ps_actuales = 0
        else:
            self.ps_actuales += change_hp

    def Update_attack(self, mult):
        self.ataque_temp = (self.ataque_temp[0]*mult, self.ataque_temp[1]*mult)

    def Update_defense(self, mult):
        self.defensa_temp = (self.defensa_temp[0]*mult, self.defensa_temp[1]*mult)

    def Get_attack_stat(self):
        return self.ataque_temp
    
    def Get_defense_stat(self):
        return self.defensa_temp
    
    def Get_ps(self):
        return self.ps_actuales
    
    def Get_ps_max(self):
        return self.ps_max

    def reset_stats(self):
        self.ataque_temp = self.ataque_stats
        self.defensa_temp = self.defensa_stats

    def Is_Alive(self):
        if self.ps_actuales > 0:
            return True
        return False

    def full_heal(self):
        self.ps_actuales = self.ps_max
        
    def lern_new_attack(self, attacks):
        cc = 0
        for i in attacks:
            print(f'>{cc}. {i}')
            cc += 1
        elec = validation(int_validatión('Escriba el número del ataque que desea aprender: '), 1, len(attacks))
        if len(self.ataques) < 6:
            self.ataques.append(attacks[elec-1])
        else:
            tt = 0
            for i in self.ataques:
                print(f'>{tt}. {i}')
                tt += 1
            elec2 = validation(int_validatión('Escriba el número del ataque con el cual deseas sutituir tu nuevo ataque: '), 1, 6)
            del self.ataques[elec2-1]
            self.ataques.append(attacks[elec])

    def __repr__(self): #Representación del objeto pokemon dentro de un sistema de datos como array. Retorna un str
        return f'{self.nombre}'
    
    def __str__(self): #Representación del objeto pokemon al imprimirlo. Retorna un str
        return f'{self.nombre}'

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
        return f'{self.type}'
    
    def get_type_object(self):
        return self.type

    def get_damage(self):
        return self.damage
    
    def get_attack_type(self):
        return self.damage_type
    
    def get_name(self):
        return f'{self.name}'
    
    def show(self):
        return f'{self.name}, Tipo: {self.type.show(self.type)}, Daño: {self.damage}, {self.damage_type}'
    
    def __repr__(self) -> str:
        return f'{self.name}'

#Tipos:

class Type:
    Resistencia = []
    Inmunidades = []
    Debilidades = []

    def type_multiplier(self, type):
        if type in self.Resistencia:
            return 1/2
        elif type in self.Debilidades:
            return 2
        elif type in self.Inmunidades:
            return 0
        else:
            return 1
        


class Normal(Type):
    Resistencia = []
    Inmunidades = ["Fantasma"]
    Debilidades = ["Lucha"]

    def show(self) -> str:
        return 'Normal'
    

class Lucha(Type):
    Resistencia = ["Roca", "Bicho", "Siniestro"]
    Inmunidades = []
    Debilidades = ["Volador", "Psiquico"]
    def show(self) -> str:
        return 'Lucha'
    

class Volador(Type):
    Resistencia = ["Lucha", "Bicho", "Planta"]
    Inmunidades = ["Tierra"]
    Debilidades = ["Roca", "Electrico", "Hielo"]
    def show(self) -> str:
        return 'Volador'
    

class Veneno(Type):
    Resistencia = ["Lucha", "Veneno", "Bicho", "Planta"]
    Inmunidades = []
    Debilidades = ["Tierra", "Psiquico"]
    def show(self) -> str:
        return 'Veneno'
    

class Tierra(Type):
    Resistencia = ["Veneno", "Roca"]
    Inmunidades = ["Electrico"]
    Debilidades = ["Agua", "Planta", "Hielo"]
    def show(self) -> str:
        return 'Tierra'
    

class Roca(Type):
    Resistencia = ["Normal", "Volador", "Veneno", "Fuego"]
    Inmunidades = []
    Debilidades = ["Lucha", "Tierra", "Acero", "Agua", "Planta"]
    def show(self) -> str:
        return 'Roca'
    

class Bicho(Type):
    Resistencia = ["Lucha", "Tierra", "Planta"]
    Inmunidades = []
    Debilidades = ["Volador", "Roca", "Fuego"]
    def show(self) -> str:
        return 'Bicho'
    

class Fantasma(Type):
    Resistencia = ["Veneno", "Bicho"]
    Inmunidades = ["Normal", "Lucha"]
    Debilidades = ["Fantasma", "Siniestro"]
    def show(self) -> str:
        return 'Fantasma'
    

class Acero(Type):
    Resistencia = ["Normal", "Volador", "Roca", "Bicho", "Acero", "Planta", "Psiquico", "Hielo", "Dragon"]
    Inmunidades = ["Veneno"]
    Debilidades = ["Lucha", "Tierra", "Fuego"]
    def show(self) -> str:
        return 'Acero'


class Fuego(Type):
    Resistencia = ["Bicho", "Acero", "Fuego", "Planta"]
    Inmunidades = []
    Debilidades = ["Tierra", "Roca", "Agua"]
    def show(self) -> str:
        return 'Fuego'
    

class Agua(Type):
    Resistencia = ["Acero", "Fuego", "Agua", "Hielo"]
    Inmunidades = []
    Debilidades = ["Planta", "Electrico"]
    def show(self) -> str:
        return 'Agua'
    
class Planta(Type):
    Resistencia = ["Tierra", "Agua", "Planta", "Electrico"]
    Inmunidades = []
    Debilidades = ["Volador", "Veneno", "Bicho", "Fuego", "Hielo"]
    def show(self) -> str:
        return 'Planta'
    

class Electrico(Type):
    Resistencia = ["Volador", "Acero", "Electrico"]
    Inmunidades = []
    Debilidades = ["Tierra"]
    def show(self) -> str:
        return 'Electrico'
    

class Psiquico(Type):
    Resistencia = ["Lucha", "Psiquico"]
    Inmunidades = []
    Debilidades = ["Bicho", "Fantasma", "Siniestro"]
    def show(self) -> str:
        return 'Psiquico'
   

class Hielo(Type):
    Resistencia = ["Hielo"]
    Inmunidades = []
    Debilidades = ["Lucha", "Roca", "Acero", "Fuego"]
    def show(self) -> str:
        return 'Hielo'
    

class Dragon(Type):
    Resistencia = ["Fuego", "Agua", "Planta", "Electrico"]
    Inmunidades = []
    Debilidades = ["Hielo", "Dragon"]
    def show(self) -> str:
        return 'Dragon'
    

class Siniestro(Type):
    Resistencia = ["Fantasma", "Siniestro"]
    Inmunidades = ["Psiquico"]
    Debilidades = ["Lucha", "Bicho"]
    def show(self) -> str:
        return 'Siniestro'
    
