import time
import random


class Character:
    def __init__(self, name, ultimate):
        self.name = name
        self.hp = 100
        self.mana = 0
        self.ultimate = ultimate

    def attack(self, enemy_name, enemy_hp):
        enemy_hp -= random.randint(1, 5)
        self.mana += random.randint(1, 5)
        print(f'{self.name} атакует {enemy_name},у него осталось {enemy_hp} hp')
        return enemy_hp

    def super_attack(self, enemy_name, enemy_hp):
        enemy_hp -= random.randint(6, 10)
        self.mana -= 10
        ulta = random.choice(self.ultimate)
        if self.name == 'Волан де морт':
            enemy_hp -= enemy_hp
            print('Противник морально и физически уничтожен')
        print(
            f'{self.name} атакует {enemy_name} используя {ulta},у него осталось {enemy_hp} hp')
        return enemy_hp


Scorpion = Character(name='Скорпион', ultimate=[
                     'GET OVER HERE!', 'атаку цепью'])
Sub_zero = Character(name='Саб-зиро', ultimate=['ледяные шипы', 'замарозку'])
Gorr = Character(name='Горр', ultimate=[
                 'недружественное рукопожатие', 'суперхват'])
Riptide = Character(name='Рептилия', ultimate=[
                    'кислотный плевок', 'кислотный шар'])
Dart_vader = Character(name='Дарт Вейдер', ultimate=[
                       'удушение силой', 'атаку световым мечом'])
Volan_de_mort = Character(name='Волан де морт', ultimate=[
                          'АВАДА КЕДАВРА!!!!'])
Gendalf = Character(name='Гендальф', ultimate=['атаку посохом', 'орлов'])
Jack = Character(name='Джек воробей', ultimate=['пистолет', 'саблю'])
Enemies = [Scorpion, Sub_zero, Gorr, Riptide,
           Dart_vader, Volan_de_mort, Gendalf, Jack]

def figting():
    enemy1 = random.choice(Enemies)
    Enemies.remove(enemy1)
    enemy2 = random.choice(Enemies)
    print(f'{enemy1.name} VS {enemy2.name}')
    while True:
        if random.randint(1,5) in [1,2,3]:
            enemy2.hp = enemy1.attack(enemy2.name, enemy2.hp)
        else:
            print(f'{enemy1.name} промахнулся')
        if random.randint(1,5) in [1,2,3]:
            enemy1.hp = enemy2.attack(enemy1.name, enemy1.hp)
        else:
            print(f'{enemy2.name} промахнулся')
        time. sleep(2)
        coin = random.randint(1, 2)
        if enemy1. mana > 10:
            if coin == 1:
                enemy2.hp = enemy1.super_attack(enemy2.name, enemy2.hp)
        if enemy2. mana > 10:
            if coin == 1:
                enemy1.hp = enemy2.super_attack(enemy1.name, enemy1.hp)
                enemy2. mana -=10
                enemy1. mana -=10
        if enemy1.hp <= 0 and enemy2.hp <= 0:
            print('Ничья')
            break

        if enemy1.hp <= 0:
            print(f'Победа игрока {enemy2.name}')
            break
        elif enemy2.hp <= 0:
            print(f'Победа игрока {enemy1.name}')
            break
