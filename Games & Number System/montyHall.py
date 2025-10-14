# Monty Hall Problem
import random


def message():
    print('Game Rules & How to play:')
    print('1.\tThere are three doors.')
    print('2.\tPrize is present only behind one of the doors.')
    print('3.\tYou have to choose one of the doors, numbered (1, 2, 3).')
    print('4.\tThen the host will open one of the empty doors (excluding your choice).')
    print('5.\tAfter that you will be asked again for your choice.')
    print('6.\tIf your final choice is same as door hiding prize, you win.')
    print('\n')

def initPrize():
    return random.randint(1, 3)


def hostOpens(prize, choice):
    door = []

    for i in range(1, 4):
        if i not in (prize, choice):
            door.append(i)

    k = random.randint(0, len(door) - 1)
    return door[k]


def montyHallGame():
    print('\n\nStarting new game...\n')

    prize = initPrize()
    choice = int(input('Enter door to open\t: '))
    if choice not in range(1, 4):
        raise ValueError
    
    open = hostOpens(prize, choice)
    print('Host opened door\t:', open)

    choice = int(input('\nOpen door\t: '))
    if choice not in range(1, 4):
        raise ValueError

    print('Prize at\t:', prize)
    if choice == prize:
        return 1
    return 0
        

def main():
    message()

    while True:
        try:
            i = montyHallGame()
            if i:
                print('Congratulations, You won the prize!!!')
            else:
                print('Oops, You lost the prize...')

            exit = input('\nPress "1" to exit: ')
            if exit == '1':
                break

        except:
            print('\nWrong input, exiting...')
            break
    
    print('\n---Thank You for playing---\n')


main()
