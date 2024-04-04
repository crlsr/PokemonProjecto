'''
Este modulo se va a encargar de realizar el proceso de cargado normal en nuestro juego.
'''
#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.pokeclases import Pokeusuario, Objeto

                
#Cargando al usuario:
def user_load(attacks, pokemons):
    with open('Db//db_user.txt', 'r', encoding= 'UTF-8') as data:
        x = data.readline()
        user = x.split(';')
        pokes = eval(user[3])
        atq = eval(user[4])
        
        #Cargado de pokemons del user
        for i in pokes:
            cc = 0
            for poke in pokemons:
                if i == poke.nombre:
                    pokes[cc] = poke
        
        #Cargado de los ataques del pokemon del user     
        for i in atq: 
            cc = 0
            for ataque in attacks:
                if ataque.name == i:
                    pokes[0].ataques.append(ataque)
                    
    
        gyms = eval(user[5])
        objs = eval(user[7])
        memory_user = Pokeusuario(user[0], user[1], user[2], pokes, gyms, user[6], objs, int(user[8]), int(user[9]))
        #Retornamos al usuario 
        return memory_user
        
           
#Cargar los objetos del user
def get_objects(user):
    cc = 0
    for i in user.objetos:
        if i == 'Poción de curación':
            x = Objeto('Poción de curación', 50, 1, 1)
            user.objetos[cc] = x
            cc += 1
        elif i == 'Defensa X':
            x = Objeto("Defensa X", 0, 1, 10)
            user.objetos[cc] = x
            cc += 1
        else:
            x = Objeto("Ataque X", 0, 15, 1)
            user.objetos[cc] = x
            cc += 1
            
        
