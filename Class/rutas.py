from funtions.funciones import validation, int_validatión
from random import randint

#Clase dedicad aa la creación de rutas
class PokeRutas:
    def __init__(self, entrenador, nro = int):
        self.entrenador = entrenador
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
    def __init__(self, name, gym, dialoge):
        self.name = name
        self.gym: object = gym
        self.dialoge = dialoge
    def menu_pub():
        pass    


#Clase para gimnasios o liga
class PokeGym:
    def __init__(self, color, entrenadores = None):
        self.color = color
        if entrenadores is None:
            entrenadores = []
        self.entrenadores = entrenadores
    def menu():
        pass
    
    def liga():
        pass