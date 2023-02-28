
cheese = ["camembert", "gouda", "cheddar"]



def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1



def summon_captain_planet(planeteers):
    return [f'{planet.title()}!' for planet in planeteers]
   


def long_planeteer_calls(list):
    for word in list:
        if len(word) >= 4:
            return False
        else:
            if len(word) < 4:
                return True
        


def find_the_cheese(is_cheese):
    for item in is_cheese:
        if item in cheese:
            return item
    return None
