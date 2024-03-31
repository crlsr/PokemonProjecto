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
        return f'{self.nombre}'
    
    def menu_ruta(self, zonas, posicion):
        while True:
            num = randint(0, len(self.pokes))-1
            if num == -1:
                print('No hay batalla')
            else:
                print(f'Hay batalla con {num}')
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
    def show(self):
        if self.color == 'Naranja':
            pass
        elif self.color == 'Azul':
            pass
        elif self.color == 'Rojo':
            pass
        elif self.color == 'Negro':
            pass
        elif self.color == 'Fuxia':
            pass
        else:
            pass
    def menu_pub(self):
        while True:
            elec = validation(int_validatión('>1. Ver la historia del pueblo\n>2. Ir al MedCenter\n>3. Ir a la PokeTienda\n>4. Ir al gym\n>5. Salir\n>>>'), 1, 5)
            os.system('clear') 
            if elec == 1:
                self.show()
            elif elec == 2:
                pass
            elif elec == 3:
                pass
            elif elec == 4:
                pass
            else:
                break


#Clase para tienda pokemon
class PokeShop:
    def __init__(self, pueblo, curaciones = None, defensas = None, ataques = None):
        self.pueblo = pueblo
        if curaciones is None:
            curaciones = []
        self.curaciones = curaciones
        if defensas is None:
            defensas = []
        self.defensas = defensas
        if ataques is None:
            ataques = []
        self.ataques = ataques
        
    def menu(self, user, curacion, defensa, ataque):
        self.curaciones.append(curacion)
        self.defensas.append(defensa)
        self.ataques.append(ataque)
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
            
            elif elec == 2:
                if defensa in self.defensas:
                    if user.pokecoins > self.defensas[0].price:
                        user.pokecoins -= self.defesas[0].price
                        user.objects.append(self.defensas[0])
                        del self.defensas[0]
                    else:
                        print('Saldo insuficiente...👎🏻')
                else:
                    print('Objeto acabado')
                    
            elif elec == 3:
                if ataque in self.ataques:
                    if user.pokecoins > self.ataques[0].price:
                        user.pokecoins -= self.ataques[0].price
                        user.objects.append(self.ataques[0])
                        del self.ataques[0]
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
        
    def menu(self):
        while True:
            elec = validation(int_validatión('>1. Pelear contra el siguiente entrenador (o contra el primero)\n>2. Salir del gym'), 1, 2)
            os.system('clear') 
            if elec == 1:
                pass 
            else:
                break   
        
    def get_trainers(self):
        array = []
        for i in self.entrenadores:
            array.append(i.nombre)
        return array