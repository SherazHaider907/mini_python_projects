from Enemy import *
from Ogre import *
from Zombie import *
from Hero import *
from Weapon import *

def battle(e1: Enemy,e2: Enemy):
    e1.talk()
    e2.talk()
    
    while e1.health_points > 0 and e2.health_points > 0:
        print('-------------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()} has {e1.health_points} health Left')
        print(f'{e2.get_type_of_enemy()} has {e2.health_points} health Left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('-------------------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins the battle!')
    else:
        print(f'{e2.get_type_of_enemy()} wins the battle!')


def hero_battle(hero: Hero, enemy: Enemy):
    
    while hero.health_points > 0 and enemy.health_points > 0:
        print('-------------------')
        print(f'{hero.get_type_of_enemy()} has {hero.health_points} health Left')
        print(f'{enemy.get_type_of_enemy()} has {enemy.health_points} health Left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('-------------------')

    if hero.health_points > 0:
        print(f"Hero wins")
    else:
        print(f'{enemy.get_type_of_enemy()} wins the battle!')



zombie  = Zombie(100,10)
ogre = Ogre(150,20)
hero = Hero(120,15)

hero_battle(hero, zombie)




# print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage.')
# print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage.')

# zombie.talk()
# ogre.talk()