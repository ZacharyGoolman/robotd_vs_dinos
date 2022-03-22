class Weapon:

    def __init__(self, name, attack_power):
        self.weapon_name = name
        self.attack_power = attack_power

#These were created to ensure that my init was functional but wont the Init will be the only thing used when importing. Can also use this as quick reference. 
weapon_1 = Weapon("stun gun", 30)
print(weapon_1.weapon_name, + weapon_1.attack_power)

weapon_2 = Weapon("Beam Rifle", 45)
print(weapon_2.weapon_name, + weapon_1.attack_power)

weapon_3 = Weapon("Rocket", 55)
print(weapon_3.weapon_name, + weapon_1.attack_power)

