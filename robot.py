from weapon import Weapon


class Robot:

    def __init__(self, name, health, robot_weapon):
        self.robot_name = name
        self.robot_health = health
        self.robot_weapon = robot_weapon

    def robot_attack(self,dino):
        self.dino_health -= self.robot_weapon.attack_power



#These were created to ensure that my init was functional but wont the Init will be the only thing used when importing. Can also use this as quick reference. 
robot_weapon = Weapon("Stun Gun", 30)
robot_1 = Robot("Brave litle Toaster", 130, robot_weapon)

robot_weapon = Weapon("Beam Rifle", 45)
robot_2 = Robot("The Iron Giant", 100, robot_weapon)

robot_weapon = Weapon("Rocket", 55)
robot_3 = Robot("Bender", 75, robot_weapon)



# copy and bring over to the fleet for the list that you want created. Going to need to append to add to the list. 
# if not sure about . notation throw a breakpoint and watch where it runs too