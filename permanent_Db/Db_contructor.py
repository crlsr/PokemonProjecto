'''
Este modulo tiene como fin cosntruir la base de datos en caso de que el programa no encuentre la base de datos.
'''
#Script utrilizado para allar la ubicación absoluta de cualquier modulo o carpeta que solucitemos con el fin de evitar importación circular.
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)


#Importamos funciones utiles para la validación de elecciones
from funtions.funciones import validation, int_validatión

#Importamso las clases para poder utilizarlas durante la contrucción de la base de datos.
from Class.pokeclases import Pokemon, Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Ataque
from Class.rutas import PokeRutas


#Lista de tipos
tipos = [Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal]

#Array donde se guardan los pokemons, los ataques, las rutas, los gimnasios y los pueblos.
pokes = []
ataques = []
rutas = []
pubs = []

'''
Estas funciones tienen como fin crear los objetos que vamos a mete rne la base de datos (crear nuestra base de datos en caso de que no la tengamos)
'''
#Creación de ataques
def atq_constructor(atq, tipos):
    print('SE HA INICIALIZADO EL CREADOR DE ATAQUES💻')
    elec = validation(int_validatión('Cuantos ataques quiere poner de cada tipo?\n>>>'), 1, 100)
    for i in range(len(tipos)*elec):
        name = input(f'Diga el nombre del ataque nro {i+1}: ')
        cc = 1
        print('🌀TIPOS🌀'.center(125))
        for i in tipos:
            print(f'{cc}. {i.show(i)}')
            cc+=1
        elec2 = validation(int_validatión('Escriba del número del tipo de ataque que sea: '), 1, len(tipos)) 
        type = tipos[elec2-1]
        dmg = validation(int_validatión(f'Cuanto daño hace el ataque {name}?: '), 10, 125)
        elec3 = validation(int_validatión('Su ataque es de tipo\n>1. Especial\n>2. Físico\n>>>'), 1, 2)
        if elec3 == 1:
            ty_dmg = 'Especial'
        else:
            ty_dmg = 'Fisico'
        x = Ataque(name, type, dmg, ty_dmg)
        atq.append(x)
        os.system('clear')
        print(f'Su ataque {x.get_name()} se agrego exitosamente...')
    print('ATAQUES CREADOS EXITOSAMENTE✅...')
    return atq


#Creación de pokemones (instancias).
def poke_constr(pokemons, tipos):
    print('SE HA INICIALIZADO EL CREADOR DE POKEMONES💻')
    elec = validation(int_validatión('Cuantos pokemons quiere poner de cada tipo?\n>>>'), 1, 100)
    for i in range(len(tipos)*elec):
        name = input(f'Diga el nombre del pokemon nro {i}: ')
        def_fis = validation(int_validatión(f'Cuanta es la defensa física de {name}: '), 1, 100)
        def_esp = validation(int_validatión(f'Cuanta es la defensa especial de {name}: '), 1, 100)
        atq_fis = validation(int_validatión(f'Cuanta es el ataque físico de {name}: '), 1, 100)
        atq_esp = validation(int_validatión(f'Cuanta es el ataque especial de {name}: '), 1, 100)
        vel = validation(int_validatión(f'Cuanta es la velocidad de {name}: '), 1, 100)
        os.system('clear')
        cc = 1
        print('🌀TIPOS🌀'.center(125))
        for i in tipos:
            print(f'{cc}. {i}')
        elec2 = validation(int_validatión('Diga el número del tipo del pokemon: '), 1, len(tipos))
        elec3 = validation(int_validatión('Diga el número del segundo tipo del pokemon (si no tiene, escriba 0): '), 0, len(tipos))
        if elec3 > 0:
            x = Pokemon(name, 100, def_fis, def_esp, atq_fis, atq_esp, vel, [tipos[elec2], tipos[elec3]])
        else:
            x = Pokemon(name, 100, def_fis, def_esp, atq_fis, atq_esp, vel, [tipos[elec2]])
        print(f'El pokemon {x.nombre} se agrego exitosamente...')
    print('POKEMONES CREADOS EXITOSAMENTE✅...')
    return pokemons


#Creador de rutas
def rut_constr(rutas):
    print('SE HA INICIALIZADO EL CREADOR DE RUTAS💻')
    for i in range(0):
        x = PokeRutas([], i+1)
        rutas.append(x)
    print('RUTAS CREADAS EXITOSAMENTE✅...')


#Creador de pueblos.
def pub_constr(pueblos):
    print('SE HA INICIALIZADO EL CREADOR DE PUEBLOS 💻')
    print('PUEBLOS CREADOS EXITOSAMENTE✅...')
    pass


'''
Estas funciones tienen como fin meter la sinstancias que creamso en nuestra base de datos, inicializandola.
'''
#Estructura de los ataques en la base de datos.
def atq_db_structure(atq):
    with open('Db//db_atq', 'w', encoding='UTF-8') as data:
        for i in atq:
            data.write(f'{i.name};{i.type.show(i.type)};{i.damage};{i.damage_type}\n')

#Estructura de los pokemons en la base de datos.
def poke_db_structure(pokemons):
    with open('Db//db_poke', 'w', encoding='UTF-8') as data:
        for i in pokemons:
            data.write(f'{i.nombre};{i.stats};{i.tipo.show(i.tipo)};{i.ataques};{i.batallas_ganadas};{i.ps_max}\n')
   
#Estructura de las rutas en la base de datos.
def rut_db_structure(rut):
    with open('Db//db_rutas', 'w', encoding= 'UTF-8') as data:
        for i in rut:
            data.write(f'{i.pokes};{i.nro}\n')

#Estructura de los pueblos en la base de datos.
def pub_db_structure():
    pass


'''
Ejecución del programa
'''
#Ejecución de los constructores de la estructura de datos.
#atq_constructor(ataques, tipos)
#atq_db_structure(ataques)
poke_constr(pokes, tipos)
poke_db_structure(pokes)
rut_constr(rutas)
rut_db_structure(rutas)
#pub_constr(pubs)
#pub_db_structure(pubs)




