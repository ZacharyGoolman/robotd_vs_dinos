from weapon import Weapon
from robot import Robot


class Fleet:
    
    def __init__(self):
        self.fleet = []
        
    def robot_fleet(self):
        
        robot_weapon = Weapon("Stun Gun", 30)
        robot_1 = Robot("Brave litle Toaster", 130, robot_weapon)
       
        robot_weapon = Weapon("Beam Rifle", 45)
        robot_2 = Robot("The Iron Giant", 100, robot_weapon)

        robot_weapon = Weapon("Rocket", 55)
        robot_3 = Robot("Bender", 75, robot_weapon)
      
        self.fleet.append(robot_1)
        self.fleet.append(robot_2)
        self.fleet.append(robot_3)







# I know I will need to import my robots then append them to my fleet class in the robots instance variables. 
