from Class.pokeclases import Pokemon, Trainer, Ataque, Objeto, Type, Lucha, Normal, Volador, Veneno, Tierra, Roca, Bicho, Fantasma, Acero, Fuego, Agua, Planta, Electrico, Psiquico, Hielo, Dragon, Siniestro, Pokeusuario
import random
#To-Do función combate

def get_STAB(Pokemon, Attack_type):
    for type in Pokemon.tipos:
        if type.show(type) == Attack_type.show(Attack_type):
            return 1.5
    return 1

def get_crit():
    if random.randint(1,16) == 1:
        print("Es un golpe crítico!")
        return 2
    return 1

def use_item(Pokemon, item):
    print("Ha usado su objeto {}".format(item.get_name()))
    Pokemon.Update_hp(item.get_life())
    Pokemon.Update_attack(item.get_attack())
    Pokemon.Update_defense(item.get_defense())

def select_player_attack(Pokemon):
    while True:
        count = 1
        possible_attacks = Pokemon.get_attacks()
        for attack in possible_attacks:
            print("{}. {}".format(count, attack.get_name()))
            count += 1
        print("0. Para salir")
        try:
            answer = int(input(""))
            if answer == 0:
                return None
            elif answer <= len(possible_attacks):
                print(possible_attacks[answer-1].get_type_object())
                return possible_attacks[answer-1]
        except:
            print("Respuesta Invalida")

def select_player_item(Trainer):
    while True:
        count = 1
        possible_items = Trainer.get_objects()
        for objeto in possible_items:
            print("{}. {}".format(count, objeto.get_name()))
            count += 1
        print("0. para salir")
        try:
            answer = int(input(""))
            if answer == 0:
                return None
            elif answer <= len(possible_items) and answer > 0:
                return possible_items[answer-1]
        except:
            print("Respuesta invalida")

def calculate_damage(Receiving_Pokemon, Giving_Pokemon, attack):
    stab_bonus = get_STAB(Giving_Pokemon, attack.get_type_object())
    crit_bonus = get_crit()
    if attack.get_attack_type() == "Fisico":
        index = 0
    elif attack.get_attack_type() == "Especial":
        index = 1
    attack_stat = Giving_Pokemon.Get_attack_stat()
    defense_stat = Receiving_Pokemon.Get_defense_stat()
    attack_power = attack.get_damage()
    type_multiplier = 1
    attack_type = attack.get_type_object()
    attack_type_string = attack_type.show(attack_type)
    for type in Receiving_Pokemon.get_types_object():
        type_relation = type.type_multiplier(type, attack_type_string)
        type_multiplier = type_multiplier*type_relation
    if type_multiplier >= 2:
        print("Es super eficaz!")
    elif type_multiplier > 0 and type_multiplier < 1:
        print("Es poco eficaz")
    elif type_multiplier == 0:
        print("No ha hecho daño! Es inmune")
    
    damage = (((20+2)*attack_power*(attack_stat[index]/defense_stat[index]))/50) * stab_bonus * crit_bonus * type_multiplier
    return int(damage)

def use_attack(Receiving_Pokemon, Giving_Pokemon, attack):
    damage = calculate_damage(Receiving_Pokemon, Giving_Pokemon, attack)
    print("{} ha usado {}".format(Giving_Pokemon.get_name(), attack.get_name()))
    Receiving_Pokemon.Update_hp(-damage)
    print("Ha hecho {} de daño".format(damage))

def compare_speed(Player_Pokemon, Enemy_Pokemon):
    user_speed = Player_Pokemon.get_speed()
    enemy_Pokemon = Enemy_Pokemon.get_speed()
    if user_speed >= enemy_Pokemon:
        return True
    return False

def Enemy_move(Enemy_Trainer, current_pokemon, user_pokemon):
    choice = random.randint(1, 8)
    if choice == 1 and len(Enemy_Trainer.get_objects()) > 0:
        Enemy_items = Enemy_Trainer.get_objects()
        use_item(current_pokemon, Enemy_items[0])
        Enemy_Trainer.get_objects().remove(Enemy_items[0])
    else:
        possible_attacks = current_pokemon.get_attacks()
        attack_choice = possible_attacks[random.randint(0, len(possible_attacks)-1)]
        use_attack(user_pokemon, current_pokemon, attack_choice)

def Player_move(current_pkmn_user, current_pkmn_enemy, current_attack, current_item, Player_Trainer):
    if current_attack is not None:
        use_attack(current_pkmn_enemy, current_pkmn_user, current_attack)
    else:
        use_item(current_pkmn_user, current_item)
        Player_Trainer.get_objects().remove(current_item)
        

def check_status(Player_Trainer, Enemy_Trainer):
    if Player_Trainer.get_available_pokemon() > 0 and Enemy_Trainer.get_available_pokemon() > 0:
        return True
    return False
        
def Pokemon_Combat(Player_Trainer, Enemy_Trainer):
    current_pkmn_user = Player_Trainer.get_next_pokemon()
    current_pkmn_enemy = Enemy_Trainer.get_next_pokemon()
    print("Combate versus {}!".format(Enemy_Trainer.get_name()))
    while Player_Trainer.get_available_pokemon() > 0 and Enemy_Trainer.get_available_pokemon() > 0:
        print("""Tu pokémon: {}, {}/{} ps
Pokemon enemigo; {}, {}/{} ps""".format(current_pkmn_user.get_name(), current_pkmn_user.Get_ps(), current_pkmn_user.Get_ps_max(), current_pkmn_enemy.get_name(), current_pkmn_enemy.Get_ps(), current_pkmn_enemy.Get_ps_max()))
        current_attack = None
        current_item = None
        while True:
            print("""1. Usar un ataque
2. Usar un objeto""")
            answer = input("")
            if answer == "1":
                current_attack = select_player_attack(current_pkmn_user)
                if current_attack is None:
                    continue
                break
            elif answer == "2":
                current_item = select_player_item(Player_Trainer)
                if current_item is None:
                    continue
                break
            else:
                print("Valor Inválido")

        if compare_speed(current_pkmn_user, current_pkmn_enemy) is True:
            Player_move(current_pkmn_user, current_pkmn_enemy, current_attack, current_item, Player_Trainer)
            if current_pkmn_enemy.Is_Alive() is False:
                print("{} ha sido derrotado".format(current_pkmn_enemy.get_name()))
                current_pkmn_enemy = Enemy_Trainer.get_next_pokemon()
                continue
            Enemy_move(Enemy_Trainer, current_pkmn_enemy, current_pkmn_user)
            if current_pkmn_user.Is_Alive() is False:
                print("{} ha sido derrotado".format(current_pkmn_user.get_name()))
                continue
        else:
            Enemy_move(Enemy_Trainer, current_pkmn_enemy, current_pkmn_user)
            if current_pkmn_user.Is_Alive() is False:
                print("{} ha sido derrotado".format(current_pkmn_user.get_name()))
                continue
            Player_move(current_pkmn_user, current_pkmn_enemy, current_attack, current_item, Player_Trainer)
            if current_pkmn_enemy.Is_Alive() is False:
                print("{} ha sido derrotado".format(current_pkmn_enemy.get_name()))
                current_pkmn_enemy = Enemy_Trainer.get_next_pokemon()
                continue
    Player_Trainer.reset_stats_pkmn()
    if Player_Trainer.get_available_pokemon() > 0:
        print("Ganaste!")
        Player_Trainer.add_win()
        return True
    print("Perdiste")
    return False