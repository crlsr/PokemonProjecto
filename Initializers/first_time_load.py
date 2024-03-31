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

from Class.pokeclases import Pokeusuario

from random import randint

from Class.rutas import PokeRutas, PokePueblos, PokeMed, PokeGym, PokeShop

#Lista de tipos
tipos = [Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Dragon, Acero, Veneno]

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
                lista = eval(array[1])
                y = PokeGym(array[0], lista)
                x.gym = y
            elif 'med' in array:
                y = PokeMed(array[0])
                x.medcenter = y
            elif 'shop' in array:
                y = PokeShop(array[0])
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
En este apartado realizamos todos los procesos de empaquetamiento de datos (meter los pokemons dentro de sus respectivos entrenadores, meter los ataques dentro de sus respectivos pokemons, y los pokemons salvajes dentro de sus respectivas rutas, etc...)
'''

#Función para asignarle a cada ataque, su tipo
def atq_class_asig(ataques, tipos):
    for i in ataques:
        cc = 0
        for tipo in tipos:
            if tipo.show(tipo) == i.type:
                i.type = tipo
                cc += 1
            else:
                continue

#Función para asignarle a cada pokemon su tipo:
def pokes_type_asig(pokes, tipos):
    for i in pokes:
        cc = 0
        for j in i.tipos:
            for tipo in tipos:
                if tipo.show(tipo) == j:
                    i.tipos[cc] = tipo
                    cc += 1
                else:
                    continue

#Función para asignarle cada pokemon a su ruta:
def rute_pokes_asig(rutas, pokes):
    for i in rutas:
        cc = 0
        for j in i.entrenadores:
            for poke in pokes:
                if poke.nombre == j:
                    i.entrenadores[cc] = Trainer(f'{j} Salvaje', [poke], None, i.nro)
                    cc += 1
                else:
                    continue
            

#Función para darle ataques aleatorios a los pokemons segun su tipo
def atq_randomizer(pokemons, ataques):
    for pokemon in pokemons:
        for i in ataques:
            if i.type in pokemon.tipos:
                proba = randint(1, 3)
                if proba == 1 and len(pokemon.ataques)<6:
                    pokemon.ataques.append(i)
                else:
                    continue
                
#Función para meter a cada entrenador en su pueblo
def trainer_pub(trainer, pueblos):
    for i in pueblos:
        for j in trainer:
            if j.ubicacion == i.name:
                i.gym.entrenadores.append(j)
            else:
                continue
                
#Función para darle a cada entrenador un pokemon random
def poke_random(pueblos, pokemons):
    for pueblo in pueblos:
        entrenadores = pueblo.gym.entrenadores
        for i in entrenadores:
            if i.ubicacion == 'Naranja': #Tipo Normal
                clase = [poke for poke in pokemons if (Normal in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<2:
                        i.pokemones.append(poke)
                    else:
                        continue
            elif i.ubicacion == 'Azul': #Tipo Agua
                clase = [poke for poke in pokemons if (Agua in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<3:
                        i.pokemones.append(poke)
                    else:
                        continue
            elif i.ubicacion == 'Rojo': #Tipo Fuego
                clase = [poke for poke in pokemons if (Fuego in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<4:
                        i.pokemones.append(poke)
                    else:
                        continue
            elif i.ubicacion == 'Negro': #Tipo Fantasma
                clase = [poke for poke in pokemons if (Fantasma in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<5:
                        i.pokemones.append(poke)
                    else:
                        continue
            elif i.ubicacion == 'Fuxia': #Tipo Siniestro
                clase = [poke for poke in pokemons if (Siniestro in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<5:
                        i.pokemones.append(poke)
                    else:
                        continue
            elif i.ubicacion == 'Plata': #Tipo Acero
                clase = [poke for poke in pokemons if (Acero in poke.tipos)]
                for poke in clase:
                    if randint(1,3) == 1 and len(i.pokemones)<6:
                        i.pokemones.append(poke)
                    else:
                        continue
            else:
                continue
#Esta función tiene como fin darle los pokemonsa los entrenadores de la liga.
def poke_liga(pueblos, pokemons):
    liga = pueblos[-1]
    liga.gym.entrenadores[0].pokemons = [pokemons[6], pokemons[29], pokemons[31], pokemons[41], pokemons[54], pokemons[71]]
    liga.gym.entrenadores[1].pokemons = [pokemons[22], pokemons[32], pokemons[35], pokemons[43], pokemons[44], pokemons[42]]
    liga.gym.entrenadores[2].pokemons = [pokemons[62], pokemons[53], pokemons[61], pokemons[70], pokemons[72], pokemons[67]]
    liga.gym.entrenadores[3].pokemons = [pokemons[74], pokemons[66], pokemons[66], pokemons[11], pokemons[9], pokemons[20]]
        


'''
Ejecución del programa
'''
array = []
array2 = []
arrayr = []
array3 = []
array4 = []
atq_creator(array2)
poke_creator(array)
ruta_creator(arrayr)
pubs_creator(array3)
trainers_creator(array4)

atq_class_asig(array2, tipos)
pokes_type_asig(array, tipos)
rute_pokes_asig(arrayr, array)
trainer_pub(array4, array3)

atq_randomizer(array, array2)
poke_random(array3, array)
poke_liga(array3, array)




