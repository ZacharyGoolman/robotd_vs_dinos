from weapon import Weapon
from robot import Robot

class Dinosaur:
    
    def __init__(self, name, power, health):
        self.dino_name = name
        self.attack_power = power
        self.dino_health = health

    # This is attack function to show decrement of health vs opponent
    def dino_attack(self, robot):
        robot.robot_health -= self.attack_power
  
dino_1 = Dinosaur("Reptar", 30, 120)

dino_2 = Dinosaur("Chomp", 55, 70)

dino_3 = Dinosaur("The push up King AKA Trex", 45, 100)



# created this just to see if code was working with attack function.
# Also note that I needed to import other modules to ensure this was working but wont need this again until the battlefield module
# dino_1.attack(robot_2)

