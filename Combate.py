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
            return 0
        else:
            print("Respuesta Invalida")

def calculate_damage(Receiving_Pokemon, Giving_Pokemon, attack):
    stab_bonus = get_STAB(Giving_Pokemon, attack.get_type_object())
    crit_bonus = get_crit()
    if attack.get_attack_type() == "Fisico":
        index = 0
    elif attack.get_attack_type() == "Especial":
        index = 1
    attack_stat = Giving_Pokemon.
    type_multiplier = 1
    attack_type = attack.get_type_object()
    attack_type_string = attack_type.show()
    for type in Receiving_Pokemon.get_types_object():
        type_relation = type.type_multiplier(attack_type_string)
        type_multiplier = type_multiplier*type_relation
    
    damage = ()
    


def Pokemon_Combat(Player_Trainer, Enemy_Trainer):
    print("Batalla Contra {}".format(Enemy_Trainer.get_name()))
    current_pkmn_user = Player_Trainer.get_next_pokemon()
    current_pkmn_enemy = Enemy_Trainer.get_next_pokemon()
    print("Combate versus {}!".format(Enemy_Trainer.get_name()))
    while Player_Trainer.get_available_pokemon() > 0 and Enemy_Trainer.get_available_pokemon() > 0:
        while True:
            print("""""")
print(get_crit())