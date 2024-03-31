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
from Class.user import Pokeusuario

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
            df = eval(array[3])
            at = eval(array[4])
            tp = eval(array[6])
            atq = eval(array[7])
            x = Pokemon(array[0], array[1], df[0], df[1], at[0], at[1], array[5], tp, atq)
            pokes.append(x)
            

#Creación de rutas
def ruta_creator(rutas):
    with open('Db//db_rutas.txt', 'r', encoding= 'UTF-8') as data:
        for i in data:
            array = i.split(';')
            del array[-1]
            x = PokeRutas(array[0], array[1])
            rutas.append(x)


#Creación de pueblos
def pubs_creator(pueblos):
    with open('Db//db_pub.txt', 'r', encoding='UTF-8') as data:
        for i in data:
            array = i.split(';')
            del array[-1]
            if 'pub' in array:
                x = PokePueblos(array[0], array[1], array[2], array[3])
            elif 'gym' in array:
                y = PokeGym(array[0], array[1])
                x.gym = y
            elif 'med' in array:
                y = PokeMed(array[0])
                x.medcenter = y
            elif 'shop' in array:
                y = PokeShop(array[0], array[1], array[2], array[3])
                x.pokeshop = y
                pueblos.append(x)
            
            
#Creación de los Entrenadores
def trainers_creator(trainers):
    with open('Db//db_trainers.txt', 'r', encoding='UTF-8') as data:
        for i in data:
            array = i.split(';')
            del array[-1]
            pokes = eval(array[1])
            x = Trainer(array[0], pokes, array[2], array[3])
            trainers.append(x)

#Creación del Usuario
def create_user(user):
    print('Bienvenido a Pokemon!💻')
    name = input('Diga su nombre: ')
    gender = input('Diga su genero (el que usted desee): ')
    region = input('Diga su region de origen: : ')
    user = Pokeusuario(name, gender, region)
    return user


'''
En este apartado realizamos todos los procesos de empaquetamiento de datos (meter los pokemons dentro de sus repectivos entrenadores, meter las edificaciones dentro de sus respectivos pueblos, y los pokemons salvajes dentro de sus respectivas rutas)
'''


'''
Ejecución del programa
'''


trainers_creator([])
