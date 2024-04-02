#Usamos script para evitar excepciones de importación circular
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

#Importamos trainer para crear pokecompañero como herencia de trainer
from Class.pokeclases import Trainer
#Clase dedicada a la creación del compañero humano
class Pokecompañero(Trainer):
    def __init__(self, nombre, pokemons = None, objetos = None, ubicacion = None):
        if pokemons is None:
            pokemons = []
        if objetos is None:
            objetos = []
        if ubicacion is None:
            ubicacion = ''
        super().__init__(nombre, pokemons, objetos, ubicacion)
        
        
