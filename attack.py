from classes.enemy import Enemy


enemy = Enemy(200, 60)

print("Hp:", enemy.get_hp())
















'''
import random

#Define class of Enemy, as you can you can create multiple by looking at the code below

class Enemy:
    hp = 200

    def __init__(self, atklow, atkhigh):
        self.atklow = atklow
        self.atkhigh = atkhigh

    def getAtk(self):
        print("atk is", self.atklow)
    
    def getHp(self):
        print("Hp is", self.hp)

#variables here in enemy are the attack powers set by the init on the enemy class

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()



# playerhp = 260
# enemyatklow = 60
# enemyatkhigh = 80

# Loop for for while player is getting attacked by enemy

# while playerhp > 0:
#     dmg = random.randrange(enemyatklow, enemyatkhigh)
#     playerhp = playerhp - dmg

#     if playerhp <= 30:
#         playerhp = 30
#     print("Enemy strikes for", dmg, "points of damage.  Curent Hp is", playerhp)

# continue causes the the loop to continue if argument is still valid

#     if playerhp > 30:
#         continue


# break causes the loop to stop once the argument becomes invalid

#     print("you have low health. you have been teleported to the nearest inn.")
#     break

'''
