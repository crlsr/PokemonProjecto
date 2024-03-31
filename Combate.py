from Class.pokeclases import Pokemon, Trainer, Ataque, Objeto, Type, Lucha, Normal, Volador, Veneno, Tierra, Roca, Bicho, Fantasma, Acero, Fuego, Agua, Planta, Electrico, Psiquico, Hielo, Dragon, Siniestro
import random
#To-Do función combate

def get_STAB(Pokemon, Attack_type):
    for type in Pokemon.tipos:
        if type.show() == Attack_type.show():
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
        answer = int(input(""))
        if answer <= len(possible_attacks):
            return possible_attacks[answer-1]
        elif answer == 0:
            return None
        else:
            print("Respuesta Invalida")

def select_player_item(Trainer):
    while True:
        count = 1
        possible_items = Trainer.get_objects()
        for objeto in possible_items:
            print("{}. {}".format(count, objeto.get_name()))
            count += 1
        print("0. para salir")
        answer = int(input(""))
        if answer <= len(possible_items):
            return possible_items[answer-1]
        elif answer == 0:
            return None
        else:
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
    attack_type_string = attack_type.show()
    for type in Receiving_Pokemon.get_types_object():
        type_relation = type.type_multiplier(attack_type_string)
        type_multiplier = type_multiplier*type_relation
    
    damage = (((20+2)*attack_power*(attack_stat[index]/defense_stat[index]))/50) * stab_bonus * crit_bonus
    return damage
    
def compare_speed(Player_Pokemon, Enemy_Pokemon):
    pass

def Pokemon_Combat(Player_Trainer, Enemy_Trainer):
    print("Batalla Contra {}".format(Enemy_Trainer.get_name()))
    current_pkmn_user = Player_Trainer.get_next_pokemon()
    current_pkmn_enemy = Enemy_Trainer.get_next_pokemon()
    print("Combate versus {}!".format(Enemy_Trainer.get_name()))
    while Player_Trainer.get_available_pokemon() > 0 and Enemy_Trainer.get_available_pokemon() > 0:
        current_attack = None
        while True:
            print("""1. Usar un ataque
2. Usar un objeto""")
            answer = input("")
            if answer == "1":
                current_attack = select_player_attack(current_pkmn_user)
                break
            elif answer == "2":
                current_item = select_player_item(Player_Trainer)