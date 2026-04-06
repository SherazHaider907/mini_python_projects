from Enemy import *
import random 
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Grrr... I am an ogre! I will crush you!")

    def smash(self):
        print("The ogre smashes the ground with its fists, causing a shockwave!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print('Ogre gets angry and increases its attack damage by 4!')