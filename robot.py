from weapon import Weapon


class Robot:

    def __init__(self, name, health):
        self.robot_name = name
        self.robot_health = health
        
        

robot_1 = Robot("Bumblebee", 100)
robot_1_weapon = Weapon(self