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
from Initializers.updater import db_user_updater
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
    user = ''
    user2 = None
    moment_position = None
    general_db_load(ataques, pokemons, rutas, pueblos, entrenadores)
    load_data(ataques, tipos, pokemons, rutas, pueblos, entrenadores)
    randomizers(pokemons, ataques, pueblos)
    try: user = user_load()
    except IndexError: pass
    poke_liga(pueblos, pokemons)
    while True: #Menú de cargado
        elec = validation(int_validatión('Bienvenido a Metromon!\n>1. Iniciar nueva aventura\n>2. Cargar Aventura\n>3. Salir\n>>> '), 1, 3)
        if elec == 1:
            user = create_user(user)
            x = input('Elija el nombre de su poke compañero: ')
            user2 = Pokecompañero(x)
            print('Perfecto, ahora realizaremos tu combate inicial con tu pokecompañero')
            seleccion_inicial(user, user2, pokemons, ataques)
            break
        elif elec == 2:
            if len(user.nombre) == 0:
                print('Error, no hay partidas guardadas')    
                continue
            else:
                load_user_pokes(pokemons, user)
                get_objects(user)
                break
        else:
            print('Vuelva pronto')
            return
    
    posicion = user.final_position #Posición absoluta del personaje desde la cual va a reaparecer
    while True: #Juego
        if posicion == 0:
            print('Si desea salir también puede retroceder de zona')
            moment_position = posicion
            posicion = pueblos[0].menu_pub(user, posicion, ataques)
        elif posicion == 1:
            moment_position = posicion
            posicion = rutas[0].menu_ruta(user, posicion, ataques)
        elif posicion == 2:
            moment_position = posicion
            posicion = rutas[1].menu_ruta(user, posicion, ataques)
        elif posicion == 3:
            moment_position = posicion
            posicion = pueblos[1].menu_pub(user, posicion, ataques)
        elif posicion == 4:
            moment_position = posicion
            posicion = rutas[2].menu_ruta(user, posicion, ataques)
        elif posicion == 5:
            moment_position = posicion
            posicion = rutas[3].menu_ruta(user, posicion, ataques)
        elif posicion == 6:
            moment_position = posicion
            posicion = pueblos[2].menu_pub(user, posicion, ataques)
        elif posicion == 7:
            moment_position = posicion
            posicion = rutas[4].menu_ruta(user, posicion, ataques)
        elif posicion == 8:
            moment_position = posicion
            posicion = rutas[5].menu_ruta(user, posicion, ataques)
        elif posicion == 9:
            moment_position = posicion
            posicion = pueblos[3].menu_pub(user, posicion, ataques)
        elif posicion == 10:
            moment_position = posicion
            posicion = rutas[6].menu_ruta(user, posicion, ataques)
        elif posicion == 11:
            moment_position = posicion
            posicion = rutas[7].menu_ruta(user, posicion, ataques)
        elif posicion == 12:
            moment_position = posicion
            posicion = pueblos[4].menu_pub(user, posicion, ataques)
        elif posicion == 13:
            moment_position = posicion
            posicion = rutas[8].menu_ruta(user, posicion, ataques)
        elif posicion == 14:
            moment_position = posicion
            posicion = rutas[9].menu_ruta(user, posicion, ataques)
        elif posicion == 15:
            moment_position = posicion
            posicion = pueblos[5].menu_pub(user, posicion, ataques)
        elif posicion == 16:
            moment_position = posicion
            posicion = rutas[10].menu_ruta(user, posicion, ataques)
        elif posicion == 17:
            moment_position = posicion
            posicion = rutas[11].menu_ruta(user, posicion, ataques)
        elif posicion == 18:
            moment_position = posicion
            posicion = pueblos[6].menu_pub(user, posicion, ataques)
        elif posicion == -1:
            user.final_position = moment_position
            break
    
    #Update de la base de datos:
    #db_updater(ataques, pokemons, rutas, pueblos, entrenadores, user)
    db_user_updater(user)
    
Metromon()

    
    
    

        