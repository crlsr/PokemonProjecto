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
def user_load():
    with open('Db//db_user.txt', 'r', encoding= 'UTF-8') as data:
        x = data.readline()
        user = x.split(';')
        pokes = eval(user[3])
        gyms = eval(user[4])
        objs = eval(user[6])
        return Pokeusuario(user[0], user[1], user[2], pokes, gyms, user[5], objs, int(user[7]), int(user[8]))
  
#Cargar pokemons del usuario      
def load_user_pokes(pokes, user):
    for i in user.pokemones:
        cc = 0
        for poke in pokes:
            if i == poke.nombre:
                user.pokemones[cc] = poke
        
            

#Cargar los objetos del user
def get_objects(user):
    cc = len(user.objetos)
    user.objetos = []
    for i in range(cc):
        x = Objeto('Pocion de vida', 50, 1, 1)
        user.objects.append(x)
        
