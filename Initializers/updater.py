'''
Este modulo tiene como finalidad realizar el proceso de óctualizacion de datos cada que cerremos la partida.
'''
       
def db_user_updater(user):
    with open('Db//db_user.txt', 'w', encoding= 'UTF-8') as data:
        data.write(f'{user.nombre};{user.genero};{user.region_dor};{user.get_pokes()};{user.pokemones[0].get_ataques()};{user.get_medallas()};{user.liga};{user.get_objetos()};{user.pokecoins};{user.final_position};\n')

