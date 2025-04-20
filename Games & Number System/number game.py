# number game (can handle exceptions)
import random
def game (number, guessed_num, level=2) :
      number = str (number)
      guessed_num = str (guessed_num)
      correct_digit = ''
      correct_digit_count = 0
      correct_place_count = 0

      # correct places
      for i in range (0,4) :
            if guessed_num [i] == number [i] :
                  correct_place_count += 1

      # correct digits
      for i in range (0,4) :
            if guessed_num [i] in number :
                  correct_digit += guessed_num [i] + ','
                  correct_digit_count += 1
                  number = number.replace (guessed_num [i], '')

      if level == 1 : 
            return [correct_digit, correct_place_count] # easy
      return [correct_digit_count, correct_place_count] # hard

# general rules
print ('GUESS THE NUMBER')
print ('\nRULES: ')
print ('\t> You have infinite turns to guess; maximum point is 10.')
print ('\t> The number must be in range [1000, 9999].')
print ('\n\t> There are two levels; easy & hard.')
print ('\t> Easy: correct digits & number of correct places are shown.')
print ('\t> Hard: number of correct digits & number of correct places are shown.')

# loop for playing more than once
while True :
      level = input ('\nPress "1" for easy (else hard): ')
      if level == '1' : 
            level = 1
      else : 
            level = 2
      number = random.randint (1000,9999)
      turns = 0
      guessed_num = 0

      # loop for guessing more than once
      while number != guessed_num :
            try :
                  guessed_num = int (input ('Guess the number: '))
                  turns += 1
                  print ('Turn', turns, ':-', end='\t')
                  if 10000 > guessed_num > 999 :
                        correct = game (number, guessed_num, level)
                        
                        # easy
                        if level == 1 :
                              if len (correct [0]) == 0 : 
                                    correct [0] = None
                              else : 
                                    correct [0] = correct [0] [:-1]
                              print ('Correct digits =', correct [0], '\t&', end='\t')
                              print ('Correct place count =', correct [1])
                              
                        # hard
                        else :
                              print ('Correct digit count =', correct [0], '\t&', end='\t')
                              print ('Correct place count =', correct [1])
                  else : 
                        print ('Input is not in range.')
                        
            # this EXCEPT part executes if any ERROR OCCURS in TRY part
            # example: user gives any other datatype instead of int (or convertable to int)
            except :
                  print ('Undesirable input is given.')
                  option1 = input ('Press 1 to continue this game: ')
                  if option1 != '1' :
                        point = 0
                        break

      # this ELSE part executes if break is NOT encountered in the previous loop (loop for guessing more than once)
      # point calculation
      else :
            point = 10.5 - turns * 0.5
            if point < 0.5 : 
                  point = 0.5
      print ('You scored', point)
      option2 = input ('\nPress 1 to replay: ')
      if option2 != '1' : 
            break
print ('\nThank You for playing. \nSee You Again!')