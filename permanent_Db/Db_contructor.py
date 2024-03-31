'''
Este modulo tiene como fin cosntruir la base de datos en caso de que el programa no encuentre la base de datos.
'''
#Script utrilizado para allar la ubicación absoluta de cualquier modulo o carpeta que solucitemos con el fin de evitar importación circular.
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)


#Importamos funciones utiles para la validación de elecciones
from funtions.funciones import validation, int_validatión

#Importamso las clases para poder utilizarlas durante la contrucción de la base de datos.
from Class.pokeclases import Pokemon, Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Dragon, Acero, Veneno, Ataque, Trainer
Ataque
from Class.rutas import PokeRutas, PokePueblos, PokeMed, PokeGym, PokeShop


#Lista de tipos
tipos = [Fuego, Agua, Planta, Electrico, Psiquico, Siniestro, Fantasma, Lucha, Volador, Bicho, Roca, Normal, Hielo, Acero, Dragon, Veneno]

#Array donde se guardan los pokemons, los ataques, las rutas, los gimnasios, los pueblos y los entrenadores.
pokes = []
ataques = []
rutas = []
pubs = []
tra = []

'''
Estas funciones tienen como fin crear los objetos que vamos a mete rne la base de datos (crear nuestra base de datos en caso de que no la tengamos)
'''
#Creación de ataques
def atq_constructor(atq, tipos):
    print('SE HA INICIALIZADO EL CREADOR DE ATAQUES💻')
    elec = validation(int_validatión('Cuantos ataques quiere poner de cada tipo?\n>>>'), 1, 100)
    for i in range(len(tipos)*elec):
        name = input(f'Diga el nombre del ataque nro {i+1}: ')
        cc = 1
        print('🌀TIPOS🌀'.center(125))
        for i in tipos:
            print(f'{cc}. {i.show(i)}')
            cc+=1
        elec2 = validation(int_validatión('Escriba del número del tipo de ataque que sea: '), 1, len(tipos)) 
        type = tipos[elec2-1]
        dmg = validation(int_validatión(f'Cuanto daño hace el ataque {name}?: '), 10, 125)
        elec3 = validation(int_validatión('Su ataque es de tipo\n>1. Especial\n>2. Físico\n>>>'), 1, 2)
        if elec3 == 1:
            ty_dmg = 'Especial'
        else:
            ty_dmg = 'Fisico'
        x = Ataque(name, type, dmg, ty_dmg)
        atq.append(x)
        os.system('clear')
        print(f'Su ataque {x.get_name()} se agrego exitosamente...')
    print('ATAQUES CREADOS EXITOSAMENTE✅...')
   

#Creación de pokemones (instancias).
def poke_constr(pokemons, tipos):
    print('SE HA INICIALIZADO EL CREADOR DE POKEMONES💻')
    elec = validation(int_validatión('Cuantos pokemons quiere poner de cada tipo?\n>>>'), 1, 20)
    for i in range(len(tipos)*elec):
        name = input(f'Diga el nombre del pokemon nro {i+1}: ')
        ps_max = validation(int_validatión(f'Cuanta es la vida maxima de {name}: '), 1, 250)
        def_fis = validation(int_validatión(f'Cuanta es la defensa física de {name}: '), 1, 250)
        def_esp = validation(int_validatión(f'Cuanta es la defensa especial de {name}: '), 1, 250)
        atq_fis = validation(int_validatión(f'Cuanto es el ataque físico de {name}: '), 1, 250)
        atq_esp = validation(int_validatión(f'Cuanto es el ataque especial de {name}: '), 1, 250)
        vel = validation(int_validatión(f'Cuanta es la velocidad de {name}: '), 1, 250)
        os.system('clear')
        cc = 1
        print('🌀TIPOS🌀'.center(125))
        for i in tipos:
            print(f'{cc}. {i.show(i)}')
            cc+=1
        elec2 = validation(int_validatión('Diga el número del tipo del pokemon: '), 1, len(tipos))
        elec3 = validation(int_validatión('Diga el número del segundo tipo del pokemon (si no tiene, escriba 0): '), 0, len(tipos))
        if elec3 > 0:
            x = Pokemon(name, ps_max, def_fis, def_esp, atq_fis, atq_esp, vel, [tipos[elec2-1], tipos[elec3-1]])
        else:
            x = Pokemon(name, 100, def_fis, def_esp, atq_fis, atq_esp, vel, [tipos[elec2-1]])
        pokemons.append(x)
        os.system('clear')
        print(f'El pokemon {x.nombre} se agrego exitosamente...')
    print('POKEMONES CREADOS EXITOSAMENTE✅...')


#Creador de rutas
def rut_constr(rutas):
    print('SE HA INICIALIZADO EL CREADOR DE RUTAS💻')
    for i in range(14):
        array = []
        for i in range(3):
            y = input('Diga el nombre del pokemon que desea agregar a la ruta: ')
            array.append(y)
        x = PokeRutas(array, i+1)
        rutas.append(x)
    print('RUTAS CREADAS EXITOSAMENTE✅...')


#Creador de pueblos.
def pub_constr(pueblos):
    print('SE HA INICIALIZADO EL CREADOR DE PUEBLOS 💻')
    #Contrucción pueblo Naranja (Tipo Normal)
    Naranja = PokePueblos('Naranja', None, None, None)
    gym = PokeGym(Naranja.name, None)
    Naranja.gym = gym
    med = PokeMed(Naranja.name)
    Naranja.medcenter = med
    shop = PokeShop(Naranja.name, None, None, None)
    Naranja.pokeshop = shop
    pueblos.append(Naranja)
    
    #Contrucción pueblo Azul (Tipo Agua)
    Azul = PokePueblos('Azul', None, None, None)
    gym = PokeGym(Azul.name, None)
    Azul.gym = gym
    med = PokeMed(Azul.name)
    Azul.medcenter = med
    shop = PokeShop(Azul.name, None, None, None)
    Azul.pokeshop = shop
    pueblos.append(Azul)
    
    #Contrucción pueblo Rojo (Tipo Fuego)
    Rojo = PokePueblos('Rojo', None, None, None)
    gym = PokeGym(Rojo.name, None)
    Rojo.gym = gym
    med = PokeMed(Rojo.name)
    Rojo.medcenter = med
    shop = PokeShop(Rojo.name, None, None, None)
    Rojo.pokeshop = shop
    pueblos.append(Rojo)
    
    #Contrucción pueblo Negro (Tipo Fantasma)
    Negro = PokePueblos('Negro', None, None, None)
    gym = PokeGym(Negro.name, None)
    Negro.gym = gym
    med = PokeMed(Negro.name)
    Negro.medcenter = med
    shop = PokeShop(Negro.name, None, None, None)
    Negro.pokeshop = shop
    pueblos.append(Negro)
    
    #Contrucción pueblo Fuxia (Tipo Siniestro)
    Fuxia = PokePueblos('Fuxia', None, None, None)
    gym = PokeGym(Fuxia.name, None)
    Fuxia.gym = gym
    med = PokeMed(Fuxia.name)
    Fuxia.medcenter = med
    shop = PokeShop(Fuxia.name, None, None, None)
    Fuxia.pokeshop = shop
    pueblos.append(Fuxia)
    
    #Contrucción pueblo Plata (Tipo Acero)
    Plata = PokePueblos('Plata', None, None, None)
    gym = PokeGym(Plata.name, None)
    Plata.gym = gym
    med = PokeMed(Plata.name)
    Plata.medcenter = med
    shop = PokeShop(Plata.name, None, None, None)
    Plata.pokeshop = shop
    pueblos.append(Plata)
    
    #Contrucción Liga Pokemon (Batalla Final)
    Liga_Pokemon = PokePueblos('Liga_Pokemon', None, None, None)
    gym = PokeGym(Liga_Pokemon.name, None)
    Liga_Pokemon.gym = gym
    med = PokeMed(Liga_Pokemon.name)
    Liga_Pokemon.medcenter = med
    shop = PokeShop(Liga_Pokemon.name, None, None, None)
    Liga_Pokemon.pokeshop = shop
    pueblos.append(Liga_Pokemon)
    print('PUEBLOS CREADOS EXITOSAMENTE✅...')


#Creador de entrenadores para cada gimnasio
def trainer_contr(trainer, pueblos):
    #Entrenadores gimnasio Naranja
    trainernar1 = Trainer('Pedrito', None, None, pueblos[0].name)  
    trainer.append(trainernar1)   
    trainernar2 = Trainer('Dalto', None, None, pueblos[0].name)   
    trainer.append(trainernar2)     
    trainernar3 = Trainer('Joseca', None, None, pueblos[0].name)
    trainer.append(trainernar3)        
    trainernar4 = Trainer('Jaimito', None, None, pueblos[0].name)
    trainer.append(trainernar4)   
    
    #Entrenadores gimnasio Azul
    traineraz1 = Trainer('Andres Rojas', None, None, pueblos[1].name)
    trainer.append(traineraz1)        
    traineraz2 = Trainer('Carlos Rodriguez', None, None, pueblos[1].name)  
    trainer.append(traineraz2)           
    traineraz3 = Trainer('Cerati', None, None, pueblos[1].name) 
    trainer.append(traineraz3)            
    traineraz4 = Trainer('Michael Feels', None, None, pueblos[1].name)
    trainer.append(traineraz4)        
    
    #Entrenadores gimnasio Rojo
    trainerroj1 = Trainer('Jhonnathan', None, None, pueblos[2].name)   
    trainer.append(trainerroj1)        
    trainerroj2 = Trainer('Ferrero', None, None, pueblos[2].name)  
    trainer.append(trainerroj2)         
    trainerroj3 = Trainer('JulioProfe', None, None, pueblos[2].name) 
    trainer.append(trainerroj3)          
    trainerroj4 = Trainer('Nancy', None, None, pueblos[2].name)  
    trainer.append(trainerroj4)        
    
    #Entrenadores gimnasio Negro
    trainerneg1 = Trainer('Chris Andrade', None, None, pueblos[3].name)
    trainer.append(trainerneg1)        
    trainerneg2 = Trainer('Leo Rojas', None, None, pueblos[3].name)
    trainer.append(trainerneg2)        
    trainerneg3 = Trainer('Nacho Redondo', None, None, pueblos[3].name)
    trainer.append(trainerneg3)        
    trainerneg4 = Trainer('Eliu', None, None, pueblos[3].name)
    trainer.append(trainerneg4)        
    
    #Entrenadores gimnasio Fuxia
    trainerfuxia1 = Trainer('Neutro Shorty', None, None, pueblos[4].name)
    trainer.append(trainerfuxia1)        
    trainerfuxia2 = Trainer('Akapellah', None, None, pueblos[4].name)
    trainer.append(trainerfuxia2)        
    trainerfuxia3 = Trainer('Danny Ocean', None, None, pueblos[4].name)
    trainer.append(trainerfuxia3)        
    trainerfuxia4 = Trainer('Canserbero', None, None, pueblos[4].name)
    trainer.append(trainerfuxia4)        
    
    #Entrenadores gimnasio Plata
    trainerplata1 = Trainer('Electricista de Cantv', None, None, pueblos[5].name)
    trainer.append(trainerplata1)        
    trainerplata2 = Trainer('Trabajador de Fontana', None, None, pueblos[5].name)
    trainer.append(trainerplata2)        
    trainerplata3 = Trainer('Estudiante Unimetano', None, None, pueblos[5].name)
    trainer.append(trainerplata3)        
    trainerplata4 = Trainer('Andres Bello', None, None, pueblos[5].name)
    trainer.append(trainerplata4)        
    
    #Entrenadores Alto Mando
    trainerlig1 = Trainer('Margarita de Abreu', None, None, pueblos[-1].name)
    trainer.append(trainerlig1)        
    trainerlig2 = Trainer('Jose Quevedo', None, None, pueblos[-1].name)
    trainer.append(trainerlig2)        
    trainerlig3 = Trainer('Javier Texeira', None, None, pueblos[-1].name)
    trainer.append(trainerlig3)        
    trainerlig4 = Trainer('Fernando Torre Mora', None, None, pueblos[-1].name)
    trainer.append(trainerlig4)        


'''
Estas funciones tienen como fin meter la sinstancias que creamso en nuestra base de datos, inicializandola.
'''
#Estructura de los ataques en la base de datos.
def atq_db_structure(atq):
    with open('Db//db_atq.txt', 'w', encoding='UTF-8') as data:
        for i in atq:
            data.write(f'{i.name};{i.type.show()};{i.damage};{i.damage_type};\n')

#Estructura de los pokemons en la base de datos.
def poke_db_structure(pokemons):
    with open('Db//db_poke.txt', 'w', encoding='UTF-8') as data:
        for i in pokemons:
            data.write(f'{i.nombre};{i.ps_max};{i.ps_actuales};{i.defena_stats};{i.ataque_stats};{i.velocidad};{i.get_types()};{i.ataques};{i.batallas_ganadas};\n')
   
#Estructura de las rutas en la base de datos.
def rut_db_structure(rut):
    with open('Db//db_rutas.txt', 'w', encoding= 'UTF-8') as data:
        for i in rut:
            data.write(f'{i.entrenadores};{i.nro};\n')

#Estructura de los pueblos en la base de datos.
def pub_db_structure(pueblos):
    with open('Db//db_pub.txt', 'w', encoding='UTF-8') as data:
        for i in pueblos:
            data.write(f'{i.name};None;None;None;pub;\n')
            data.write(f'{i.gym.pueblo};{i.gym.get_trainers()};gym;\n')
            data.write(f'{i.medcenter.pueblo};med;\n')
            data.write(f'{i.pokeshop.pueblo};{len(i.pokeshop.curaciones)};{len(i.pokeshop.defensas)};{len(i.pokeshop.ataques)};shop;\n')
            
#Estructura para los entrnadores:
def trainer_db_Structure(trainers):
    with open('Db//db_trainers.txt', 'w', encoding='UTF-8') as data:
        for i in trainers:
            data.write(f'{i.nombre};{i.get_pokes()};{i.obj_num()};{i.ubicacion};\n')
            


'''
Ejecución del programa
'''
#Función de la construccion general de las instancias.
def exe_contructor(ataques, tipos, pokes, rutas, pubs, tra):
    atq_constructor(ataques, tipos)
    poke_constr(pokes, tipos)
    rut_constr(rutas)
    pub_constr(pubs)
    trainer_contr(tra, pubs)

#Función de la estrctura general de la base de datos.
def exe_db_structure(ataques, pokes, rutas, pubs, tra):
    atq_db_structure(ataques)
    poke_db_structure(pokes)
    rut_db_structure(rutas)
    pub_db_structure(pubs)
    trainer_db_Structure(tra)
    
#Ejecución de los constructores de la estructura de datos.
exe_contructor(ataques, tipos, pokes, rutas, pubs, tra)
exe_db_structure(ataques, pokes, rutas, pubs, tra)
    
    
    
    






