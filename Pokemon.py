'''
En este apartado se va a desarollar y ejecutar y todo el juego
'''

#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Initializers.first_time_load import general_db_load, load_data, randomizers, create_user, seleccion_inicial, poke_liga
from Initializers.current_load import user_load, load_user_pokes, get_objects
from Initializers.updater import db_updater
from funtions.funciones import validation, int_validatión
from Class.pokeclases import Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Dragon, Acero, Veneno
from Class.partner import Pokecompañero


def Metromon():
    tipos = [Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Dragon, Acero, Veneno]
    ataques = []
    pokemons = []
    pueblos = []
    rutas = []
    entrenadores = []
    user = None
    user2 = None
    general_db_load(ataques, pokemons, rutas, pueblos, entrenadores)
    try: user_load(user)
    except IndexError: pass
    poke_liga(pueblos, pokemons)
    while True: #Menú de cargado
        elec = validation(int_validatión('Bienvenido a Metromon!\n>1. Iniciar nueva aventura\n>2. Cargar Aventura\n>3. Salir'), 1, 3)
        if elec == 1:
            load_data(ataques, tipos, pokemons, rutas, pueblos, entrenadores)
            randomizers(pokemons, ataques, pueblos)
            create_user(user)
            x = input('Elija el nombre de su poke compañero: ')
            user2 = Pokecompañero(x)
            print('Perfecto, ahora realizaremos tu combate inicial con tu pokecompañero')
            seleccion_inicial(user, user2, pokemons)
            break
        elif elec == 2:
            if len(user) == 0:
                print('Error, no hay partidas guardadas')    
                continue
            else:
                load_user_pokes(pokemons, user)
                get_objects(user)
                break
    
    posicion = user.final_position #Posición absoluta del perosnaje
    while True: #Juego
        if posicion == 0:
            moment_position = pueblos[0].menu(user, posicion)
            posicion = moment_position
        elif posicion == 1:
            moment_position = rutas[0].menu(user)
            posicion = moment_position
        elif posicion == 2:
            moment_position = rutas[1].menu(user)
            posicion = moment_position
        elif posicion == 3:
            moment_position = pueblos[1].menu(user)
            posicion = moment_position
        elif posicion == 4:
            moment_position = rutas[2].menu(user)
            posicion = moment_position
        elif posicion == 5:
            moment_position = rutas[3].menu(user)
            posicion = moment_position
        elif posicion == 6:
            moment_position = pueblos[2].menu(user)
            posicion = moment_position
        elif posicion == 7:
            moment_position = rutas[4].menu(user)
            posicion = moment_position
        elif posicion == 8:
            moment_position = rutas[5].menu(user)
            posicion = moment_position
        elif posicion == 9:
            moment_position = pueblos[3].menu(user)
            posicion = moment_position
        elif posicion == 10:
            moment_position = rutas[6].menu(user)
            posicion = moment_position
        elif posicion == 11:
            moment_position = rutas[7].menu(user)
            posicion = moment_position
        elif posicion == 12:
            moment_position = pueblos[4].menu(user)
            posicion = moment_position
        elif posicion == 13:
            moment_position = rutas[8].menu(user)
            posicion = moment_position
        elif posicion == 14:
            moment_position = rutas[9].menu(user)
            posicion = moment_position
        elif posicion == 15:
            moment_position = pueblos[5].menu(user)
            posicion = moment_position
        elif posicion == 16:
            moment_position = rutas[10].menu(user)
            posicion = moment_position
        elif posicion == 17:
            moment_position = rutas[11].menu(user)
            posicion = moment_position
        elif posicion == 18:
            moment_position = pueblos[6].menu(user)
            posicion = moment_position
        elif posicion == -1:
            user.final_position = moment_position
            break
    
    #Update de la base de datos:
    db_updater(ataques, pokemons, rutas, pueblos, entrenadores, user)
    
Metromon()
    
    
    

        