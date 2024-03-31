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
from pokeclases import Objeto
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
    
    def menu_ruta(self, user, zonas, posicion):
        while True:
            num = randint(0, len(self.entrenadores))-1
            if num == -1:
                print('No hay batalla')
            else:
                Pokemon_Combat(user, self.entrenadores[num])
            elec = validation(int_validatión(f'>1. Avanzar a {zonas[posicion+1]}\n>2. Retroceder a {zonas[posicion-1]}\n>3. Salir de Pokemon\n>>>'))
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
            pass
        elif self.name == 'Azul':
            pass
        elif self.name == 'Rojo':
            pass
        elif self.name == 'Negro':
            pass
        elif self.name == 'Fuxia':
            pass
        elif self.name == 'Liga_Pokemon':
            pass
    def menu_pub(self, user, posicion):
        while True:
            elec = validation(int_validatión('>1. Preguntarle a tu compañero por la historia del pueblo\n>2. Ir al MedCenter\n>3. Ir a la PokeTienda\n>4. Ir al gym\n>5. Retroceder Ruta\n>6. Avanzar Ruta\n>7. Salir\n>>>'), 1, 7)
            os.system('clear') 
            if elec == 1:
                self.show()
            elif elec == 2:
                self.medcenter.menu(self.medcenter)
            elif elec == 3:
                self.pokeshop.menu(self.pokeshop)
            elif elec == 4:
                boolean = self.gym.menu(self.gym)
                if boolean == False:
                    for i in user.pokemons:
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
        
    def menu(self, user, curacion):
        self.curaciones.append(Objeto('Poción de curación', 45, 1, 1))
        while True:
            elec = validation(int_validatión('Que deseas comprar?\n>1. Curación: 1200\n>2. Posción de defensa: 900\n>3. Poción de ataque: 1000\n>4. Salir\n>>>'), 1, 4)
            os.system('clear')
            if elec == 1:
                if curacion in self.curaciones:
                    if user.pokecoins > self.curaciones[0].price:
                        user.pokecoins -= self.curaciones[0].price
                        user.objects.append(self.curaciones[0])
                        del self.curaciones[0]
                    else:
                        print('Saldo insuficiente...👎🏻')
                else:
                    print('Objeto acabado')
            
            else:
                print('Gracias por visitarnos...💪🏻')
                break
                                

#Clase para medcenter
class PokeMed:
    def __init__(self, pueblo):
        self.pueblo = pueblo
    def menu(self, user):
        while True:
            elec = validation(int_validatión('>1. Curar pokemones\n>2. Salir'), 1, 2)
            os.system('clear')
            if elec == 1:
                for i in user.pokemons:
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
        
    def menu(self, user, pueblo):
        while True:
            elec = validation(int_validatión('>1. Pelear contra el siguiente entrenador (o contra el primero)\n>2. Salir del gym'), 1, 2)
            os.system('clear') 
            if elec == 1:
                if len(self.entrenadores) > 0:
                    boolean = Pokemon_Combat(user, self.entrenadores[0])
                    if boolean == True:
                        del self.entrenadores
                        print('Entrenador derrotad, haz ganado 1200 Pokemonedas')
                        user.pokecoins += 1200
                        if len(self.entrenadores) == 0:
                            user.gimnasios.append(self.pueblo)
                    else:
                        print('Será llevado al centro Pokemon de la ciudad')
                        return boolean
            else:
                break   
        
    def get_trainers(self):
        array = []
        for i in self.entrenadores:
            array.append(i.nombre)
        return array