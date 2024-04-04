'''
Este modulo tiene como finalidad realizar el proceso de óctualizacion de datos cada que cerremos la partida.
'''

'''
def db_pokes_updater(pokes):
    with open('Db//db_poke.txt', 'w', encoding= 'UTF-8') as data:
        for i in pokes:
            data.write(f'{i.nombre};{i.ps_max};{i.ps_actuales};{i.defensa_stats};{i.ataque_stats};{i.velocidad};{i.get_types()};{[]};{i.batallas_ganadas};\n')

def db_pueblos_updater(pueblos):
    with open('Db//db_pub.txt', 'w', encoding= 'UTF-8') as data:
        for i in pueblos:
            data.write(f'{i.name};None;None;None;pub;\n')
            data.write(f'{i.gym.pueblo};{[]};gym;\n')
            data.write(f'{i.medcenter.pueblo};med;\n')
            data.write(f'{i.pokeshop.pueblo};shop;\n')
    
def db_trainers_updater(trainers):
    with open('Db//db_trainers.txt', 'w', encoding= 'UTF-8') as data:
        for i in trainers:
            data.write(f'{i.nombre};{i.get_pokes()};{[]};{i.ubicacion};\n')
            
def db_atq_updater(ataques):
    with open('Db//db_atq.txt', 'w', encoding= 'UTF-8') as data:
        for i in ataques:
            data.write(f'{i.name};{i.type.show(i.type)};{i.damage};{i.damage_type};\n')
            
def db_rut_updater(rutas):
    with open('Db//db_rutas.txt', 'w', encoding= 'UTF-8') as data:
        for i in rutas:
            data.write(f'{i.get_trainers()};{i.nro};\n')
'''
       
def db_user_updater(user):
    with open('Db//db_user.txt', 'w', encoding= 'UTF-8') as data:
        data.write(f'{user.nombre};{user.genero};{user.region_dor};{user.get_pokes()};{user.get_medallas()};{user.liga};{user.get_objetos()};{user.pokecoins};{user.final_position};\n')

'''
#Paquete de ejecución
def db_updater(ataques, pokemons, rutas, pueblos, trainers, user):
    db_atq_updater(ataques)
    db_pokes_updater(pokemons)
    db_rut_updater(rutas)
    db_pueblos_updater(pueblos)
    db_trainers_updater(trainers)
    db_user_updater(user)
'''