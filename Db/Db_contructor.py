'''
Este modulo tiene como fin cosntruir la base de datos en caso de que el programa no encuentre la base de datos.
'''
#Script utrilizado para allar la ubicación absoluta de cualquier modulo o carpeta que solucitemos con el fin de evitar importación circular.
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)


#Importamso las clases para poder utilizarlas durante la contrucción de la base de datos.
from Class.pokeclases import Pokemon, Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Vuelo, Bicho, Roca, Normal


#Array donde se guardan los pokemons
array = []


#Creación de pokemones (instancias).
def poke_constr(pokemons):
    for i in range(60):
        name = input(f'{i}. Diga el nombre del pokemon que va a agregar: ')
        while name in pokemons:
            name = input(f'{i}. Diga otra vez el nombre del pokemon que va a agregar (no se aceptan repetidos): ')
        if i>= 0 and i<5: #Pokemons tipo fuego
            x = Pokemon(name, 100, 100, Fuego)
            pokemons.append(x)
        elif i>=5 and i<10: #Pokemons tipo Agua
            x = Pokemon(name, 100, 100, Agua)
            pokemons.append(x)
        elif i>=10 and i<15: #Pokemons tipo Planta
            x = Pokemon(name, 100, 100, Planta)
            pokemons.append(x)
        elif i>=15 and i<20: #Pokemons tipo Electrico
            x = Pokemon(name, 100, 100, Electrico)
            pokemons.append(x)
        elif i>= 20 and i<25: #Pokemons tipo Psiquico
            x = Pokemon(name, 100, 100, Psiquico)
            pokemons.append(x)
        elif i>= 25 and i<30: #Pokemons tipo Siniestro
            x = Pokemon(name, 100, 100, Siniestro)
            pokemons.append(x)
        elif i>=30 and i<35: #Pokemons tipo Fantasma
            x = Pokemon(name, 100, 100, Fantasma)
            pokemons.append(x)
        elif i>=35 and i<40: #Pokemons tipo Lucha
            x = Pokemon(name, 100, 100, Lucha)
            pokemons.append(x)
        elif i>=40 and i<45: #Pokemons tipo Vuelo
            x = Pokemon(name, 100, 100, Vuelo)
            pokemons.append(x)
        elif i>=45 and i<50: #Pokemons tipo Bicho
            x = Pokemon(name, 100, 100, Bicho)
            pokemons.append(x)
        elif i>=50 and i<55: #Pokemons tipo Roca
            x = Pokemon(name, 100, 100, Roca)
            pokemons.append(x)
        else: #Pokemons tipo Normal
            x = Pokemon(name, 100, 100, Normal)
            pokemons.append(x)
    return pokemons


#Creador de rutas
def rut_constr():
    pass


#Creador de pueblos
def puebl_contr():
    pass

#Estructura de los pokemons en la base de datos.
def db_structure(pokemons):
    with open('Db//db_poke', 'w', encoding='UTF-8') as data:
        for i in pokemons:
            data.write(f'{i.nombre};{i.stats};{i.tipo.show(i)};{i.ataques};{i.batallas_ganadas};{i.ps_max}\n')
    
     
#Ejecución de los constructores
#poke_constr(array)
#db_structure(array)




