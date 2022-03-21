class Dinosaur:
    
    def __init__(self, name, power, health):
        self.dino_name = name
        self.attack_power = power
        self.dino_health = health
       

dino_1 = Dinosaur("Reptar", 55, 120)
print(dino_1.dino_name)
print(dino_1.attack_power)
print(dino_1.dino_health)

dino_2 = Dinosaur("Chomp", 30, 70)
print(dino_2.dino_name)
print(dino_2.attack_power)
print(dino_2.dino_health)

dino_3 = Dinosaur("The push up King AKA Trex", 45, 100)
print(dino_3.dino_name)
print(dino_3.attack_power)
print(dino_3.dino_health)

# Need to create a function to have a dino attack a robot
