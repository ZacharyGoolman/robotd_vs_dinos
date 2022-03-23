from dinosaur import Dinosaur



class Herd:

    def __init__(self):
        self.herd = []
    
    def dino_herd(self):
        
        dino_1 = Dinosaur("Reptar", 30, 120)
        
        dino_2 = Dinosaur("Chomp", 55, 70)
        
        dino_3 = Dinosaur("The push up King AKA Trex", 45, 100)
        
        self.herd.append(dino_1)
        self.herd.append(dino_2)
        self.herd.append(dino_3)
        
        print(self.herd)

