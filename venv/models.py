from random import randint

from exceptions import EnemyDown
from exceptions import GameOver
from settings import LIVES


class Enemy:
    '''
    Class of enemy.
    '''

    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        '''
        Function witch choose an attack
        return: a random number (from 1 to 3)
        '''
        return randint(1, 3)

    def decrease_lives(self):
        '''
        Decrease the lives from enemy
        '''
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    '''
    Make player for game
    '''

    def __init__(self, name):
        self.name = name
        self.lives = LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        '''
        Defines the result of fight.
        Wizard(1) wins warrior(2). Warrior(2) wins robber(3). Robber(3) wins wizard(1)
        :return: 1(win), -1(lose), 0(draw)
        '''
        if attack == defense:
            return 0
        elif attack == 1 and defense == 2 \
                or attack == 2 and defense == 3 \
                or attack == 3 and defense == 1:
            return 1
        else:
            return -1

    def decrease_lives(self):
        '''
        Decrease number of lives
        '''
        self.lives -= 1
        if self.lives == 0:
            print(f'Your score: {self.score}')
            GameOver.save_score(self)
            raise GameOver(self)

    def attack(self, enemy_obj):
        '''
        Ask character(1 or 2 or 3) and print the result of the attack
        '''

        choice = None
        while choice not in (1, 2, 3):
            try:
                choice = int(input('Input a character to attack: (wizard - 1, warrior - 2, robber - 3)\n'))
                if choice not in (1, 2, 3):
                    raise ValueError
            except ValueError:
                print('Incorrect input')
        computer = enemy_obj.select_attack()
        result = self.fight(choice, computer)
        if result == 0:
            print("It's a draw")
        if result == 1:
            print('You attacked successfully')
            self.score += 1
            enemy_obj.decrease_lives()
        if result == -1:
            print('You missed')

    def defence(self, enemy_obj):
        '''
        Ask character(1 or 2 or 3) and print the result of the defence
        '''
        choice = int(input('Input a character to defence: (wizard - 1, warrior - 2, robber - 3)\n'))
        computer = enemy_obj.select_attack()
        result = self.fight(computer, choice)
        if result == 0:
            print("It's a draw")
        if result == -1:
            print('You defenced successfully')
        if result == 1:
            print('You missed')
            self.decrease_lives()
