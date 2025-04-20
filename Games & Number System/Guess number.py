#number guessing game
import random
print('The following program is a number guessing game. ')
print('\nRULES: ')
print('\t> Only one player is allowed to play the game in each turn.')
print('\t> You have infinite chances to guess the correct number.')
print('\t> The number must be a natural number of 2 digits (i.e. between 10 and 99, both inclusive).')
print('\t> You have 10 points, which will get deducted on each successive chance (condition apply).')
print('\t> You can quit in between the game. If you quit, you will get 0 points.')
print('\t> Press non-integer keys to break the loop.')
while True:
      try:
            a=random.randint(10,99)
            c=1
            while True:
                  b=int(input('\nGuess the number: '))
                  if b<10 or b>99:
                        print('Wrong input is given.')
                  elif b>a:
                        print('\tGuess is high!')
                        c+=1
                  elif b<a:
                        print('\tGuess is low!')
                        c+=1
                  elif b==a:
                        print('\nCongratulations, you guessed the correct number in',c,'turns.')
                        if c<10:
                              d=11-c
                        else:
                              d=1
                        print('\tYou have scored',d,'point(s).')
                        break
            choice=input('\nEnter "n" to end the programme: ')
            if choice=='n':
                  break
      except:
            print('\nUndesirable input is given.')
            print('You have scored 0 points.')
            choose=input('\nEnter "n" to end the programme: ')
            if choose=='n':
                  break
print('\nThank You!!!')
            
                  
