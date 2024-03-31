'''
Este modulo se va a encargar de crear la ROM de nuestro juego, creando iuna nueva partida.
'''

#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)


#Importamos las clases necesarias para la contruccion de nuestros objetos
from Class.pokeclases import Pokemon, Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Dragon, Acero, Veneno, Ataque, Trainer
Ataque
from Class.rutas import PokeRutas, PokePueblos, PokeMed, PokeGym, PokeShop

#Creación de ataques
def atq_creator(ataques):
    with open('Db//db_atq.txt', 'r', encoding= 'UTF-8') as data:
        for i in data:
            array = i.split(';')
            del array[-1]
            x = Ataque(array[0], array[1], int(array[2]), array[3])
            ataques.append(x)
            

#Creación de pokemons
def poke_creator(pokes):
    with open('Db//db_poke.txt', 'r', encoding='UTF-8') as data:
        for i in data:
            array = i.split(';')
            del array[-1]
            df = eval(array[4])
            at = eval(array[5])
            tp = eval(array[7])
            atq = eval(array[8])
            x = Pokemon(array[0], array[1], df[0], df[1], at[0], at[1], array[6], tp, atq)
            pokes.append(x)
        print(x)
            

#Creación de rutas
def ruta_creator(rutas):
    pass

#Creación de pueblos
def pubs_creator(pueblos):
    pass

#Creación de los Entrenadores
def trainers_creator(trainers):
    pass

#Creación del Usuario
def create_user(user):
    pass


'''
En este apartado realizamos todos los procesos de empaquetamiento de datos (meter los pokemons dentro de sus repectivos entrenadores, meter las edificaciones dentro de sus respectivos pueblos, y los pokemons salvajes dentro de sus respectivas rutas)
'''


'''
Ejecución del programa
'''
poke_creator([])

