from weapon import Weapon
from robot import Robot

class Dinosaur:
    
    def __init__(self, name, power, health):
        self.dino_name = name
        self.attack_power = power
        self.dino_health = health

    # This is attack function to show decrement of health vs opponent
    def attack(self, robot):
        robot.robot_health -= self.attack_power
  
#
dino_1 = Dinosaur("Reptar", 30, 120)
print(dino_1.dino_name, + dino_1.attack_power, + dino_1.dino_health)

dino_2 = Dinosaur("Chomp", 55, 70)
print(dino_2.dino_name, + dino_2.attack_power, + dino_2.dino_health)

dino_3 = Dinosaur("The push up King AKA Trex", 45, 100)
print(dino_3.dino_name, + dino_3.attack_power, + dino_3.dino_health)


# created this just to see if code was working with attack function.
# Also note that I needed to import other modules to ensure this was working but wont need this again until the battlefield module
# dino_1.attack(robot_2)

