from exceptions import GameOver
from exceptions import EnemyDown
from settings import COMMANDS
from models import Player
from models import Enemy

def menu(name):
    """
    Suggest different branches of menu
    :param name: get player name from user input
    """
    command = input("Type START to begin or HELP to see other commands: ")
    while command.lower() not in COMMANDS:
        command = input("Type START to begin or HELP to see other commands: ")
    if command.lower() == 'start':
        player = Player(name)
        enemy = Enemy(1, 1)
        print(f'\nLEVEL {enemy.level}. Your lives: {player.lives}. Your score: {player.score}')
        while True:
            try:
                player.attack(enemy)
                player.defence(enemy)
            except EnemyDown:
                player.score += 5
                enemy.level += 1
                enemy.lives = enemy.level
                print(f'\nLEVEL {enemy.level}. Your lives: {player.lives}. Your score: {player.score}')
                pass
    elif command.lower() == 'help':
        for command_name in COMMANDS:
            print(command_name)
        menu(name)
    elif command.lower() == 'show scores':
        file = open('scores.txt', 'r')
        for row in file:
            print(row)
        menu(name)
    else:
        raise GameOver


def play():
    """
    Initial the game function
    """
    name = input("Hi!\nPlease enter your name: ")
    menu(name)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Goodbye")
