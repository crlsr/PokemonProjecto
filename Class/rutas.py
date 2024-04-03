'''
En este modulo vamos a crear todas las clases dedicadas a las edificaciones, rutas y pueblos del juego.
Se trataran temas tales como:
-> Creación de Rutas
-> Creación de Pueblos 
-> Creación de edificaciones complementarias de los pueblos (shop, gym, med)
->  Empaquetameinto de estructuras dentro de los pueblos
'''
#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)


from Combate import Pokemon_Combat
from Class.pokeclases import Objeto
from funtions.funciones import validation, int_validatión
from random import randint
import os

#Clase dedicad aa la creación de rutas
class PokeRutas:
    def __init__(self, entrenadores = None, nro = int):
        if entrenadores is None:
            entrenadores = []
        self.entrenadores = entrenadores
        self.nro = nro
    def __repr__(self):
        return f'Ruta {self.nro}'
    
    def get_trainers(self):
        array = []
        for i in self.entrenadores:
            array.append(i.get_pokes()[0])
        return array
    
    def menu_ruta(self, user, posicion, ataques):
        while True:
            num = randint(0, len(self.entrenadores))-1
            if num == -1:
                print('No hay batalla')
            else:
                Pokemon_Combat(user, self.entrenadores[num], ataques)
            elec = validation(int_validatión(f'>1. Avanzar a la siguiente zona \n>2. Retroceder a zona anterior\n>3. Salir de Pokemon\n>>>'), 1, 3)
            if elec == 1:
                return posicion+1
            elif elec == 2:
                return posicion-1
            else:
                posicion = -1
                return posicion
            

#Clase para pueblos
class PokePueblos:
    def __init__(self, name, gym = None, medcenter = None, pokeshop = None):
        self.name = name
        self.gym: object = gym
        self.medcenter: object = medcenter
        self.pokeshop: object = pokeshop
    def show(self): #Historia del pueblo
        if self.name == 'Naranja':
            print('Pueblo naranja es un maravilloso pueblo el cual se enfoca en la pesca ya que vive\nse encuentra en la zona pesquera, este posee uno de los\nmejores gimnasios para iniciarse como entrenador pokemon.')
        elif self.name == 'Azul':
            print('Pueblo Azul es el pueblo de las olas donde se gozan de las mejores marras para surfear y de las mejores piscinas para nadar\nSu gimnasio de tipo agua puede ser complicado pero con habilidad se puede superar')
        elif self.name == 'Rojo':
            print('Pueblo Rojo se encuentra en lo alto de una montaña donde predomina la lava y el calor\n Su gimnasio de tipo fuego es desafiante pero muy entretenido')
        elif self.name == 'Negro':
            print('Pueblo Negro el pueblo de los fantasmas, ubicado en un cementerio, el pueblo negro se destaca por ser el \npueblo más espeluznante de todos, el gimnasio es terrorificamente complicado')
        elif self.name == 'Fuxia':
            print('Pueblo Fuxia más peligroso y con mayor tasa de criminalidad, se destaca por los maleantes que recorren sus calles.\nLos peores criminales tomaron el gimnasio, estos te esperan para que los enfrentes')
        elif self.name == 'Plata':
            print('El pueblo plateado es el pueblo de las maquinas, todos los reconocidos herreros han salido de aquií, o en el gimnasio\n esperando un digno rival')
        elif self.name == 'Liga_Pokemon':
            print('La liga pokemon es la liga donde los mejores entrenadores se enfrentan para ver quien es el mejor, el que logre ganarle al alto mando se corona como nuevo campeon pokemon\n He de aclarar que es extremadamente dificil')
    def menu_pub(self, user, posicion, ataques):
        while True:
            print(f'\nBienvenid@ a Pueblo {self.name}')
            elec = validation(int_validatión('>1. Preguntarle a tu compañero por la historia del pueblo\n>2. Ir al MedCenter\n>3. Ir a la PokeTienda\n>4. Ir al gym\n>5. Retroceder Ruta\n>6. Avanzar Ruta\n>7. Salir\n>>>'), 1, 7)
            os.system('clear') 
            if elec == 1:
                self.show()
            elif elec == 2:
                self.medcenter.menu(user)
            elif elec == 3:
                self.pokeshop.menu(user)
            elif elec == 4:
                boolean = self.gym.menu(user, ataques)
                if boolean == False:
                    for i in user.pokemones:
                        i.ps_actuales = i.ps_max
                    print('Listo, sus pokemones se han recuperado exitosamente...💪🏻')
            elif elec == 5:
                return posicion-1
            elif elec == 6:
                return posicion+1
            else:
                posicion = -1
                return posicion
    def __repr__(self):
        return f'{self.name}'


#Clase para tienda pokemon
class PokeShop:
    def __init__(self, pueblo, curaciones = None):
        self.pueblo = pueblo
        if curaciones is None:
            curaciones = []
        self.curaciones = curaciones
        
    def menu(self, user):
        self.curaciones.append(Objeto('Poción de curación', 45, 1, 1))
        self.curaciones.append(Objeto("Defensa X", 0, 1, 2))
        self.curaciones.append(Objeto("Ataque X", 0, 2, 1))
        while True:
            elec = validation(int_validatión('Que deseas comprar?\n>1. Curación: 1200\n>2. Posción de defensa: 900\n>3. Poción de ataque: 1000\n>4. Salir\n>>>'), 1, 4)
            os.system('clear')
            if elec == 1:
                if user.pokecoins > 1200:
                    user.pokecoins -= 1200
                    user.objects.append(self.curaciones[0])
                else:
                    print('Saldo insuficiente...👎🏻')
            elif elec == 2:
                if user.pokecoins > 900:
                    user.pokecoins -= 900
                    user.objects.append(self.curaciones[1])
                else:
                    print('Saldo insuficiente...👎🏻')
            elif elec == 3:
                if user.pokecoins > 1000:
                    user.pokecoins -= 1000
                    user.objects.append(self.curaciones[2])
                else:
                    print('Saldo insuficiente...👎🏻')
            
            else:
                print('Gracias por visitarnos...💪🏻')
                break
                                

#Clase para medcenter
class PokeMed:
    def __init__(self, pueblo):
        self.pueblo = pueblo
    def menu(self, user):
        while True:
            elec = validation(int_validatión('>1. Curar pokemones\n>2. Salir\n>>>'), 1, 2)
            os.system('clear')
            if elec == 1:
                for i in user.pokemones:
                    i.ps_actuales = i.ps_max
                print('Listo, sus pokemones se han recuperado exitosamente...💪🏻')
            else:
                print('Ok, vuelva pronto...👍🏻')
                break
                

#Clase para gimnasios o liga
class PokeGym:
    def __init__(self, pueblo, entrenadores = None):
        self.pueblo = pueblo
        if entrenadores is None:
            entrenadores = []
        self.entrenadores = entrenadores
        
    def menu(self, user, ataques):
        while True:
            elec = validation(int_validatión('>1. Pelear contra el siguiente entrenador (o contra el primero)\n>2. Salir del gym\n>>>'), 1, 2)
            os.system('clear') 
            if elec == 1:
                if not self.pueblo in user.gimnasios:
                    boolean = Pokemon_Combat(user, self.entrenadores[0], ataques)
                    if boolean == True:
                        del self.entrenadores[0]
                        print('Entrenador derrotad, haz ganado 1200 Pokemonedas')
                        user.pokecoins += 1200
                        if len(self.entrenadores) == 0:
                            user.gimnasios.append(self.pueblo)
                    else:
                        print('Será llevado al centro Pokemon de la ciudad')
                        return boolean
                else:
                    print('No puedes luchar en este gym, ya que ya lo completaste...')
                    break
            else:
                break   
        
    def get_trainers(self):
        array = []
        for i in self.entrenadores:
            array.append(i.nombre)
        return array