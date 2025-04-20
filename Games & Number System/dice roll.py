#dice roll
import random
print('The following program is dice game. ')
print('\nRULES: ')
print('\t> Only two players are allowed to play the game in each turn.')
print('\t> The one who scores more than or equal to 20 first, is the winner.')
print('\t> In case when both the players score more than or equal to 20, it is a tie.')
print('\t> In case of a tie the player whose total score is more is termed as the winner (HSR: High Score Rule).')
print('\t> If the scores are equal in a tied game, there is an option of a tiebreaker.')
print('\t> In the tiebreaker, the player who scores more first is the winner.')
print('\t> You can quit in between the game. The one who quits is the loser.')
print('\t> Player 1 will roll the dice first.')
print('\t> * means any key except "q", start button, etc.')
while True:
      a,b=input('\nEnter Player 1: '),input('Enter Player 2: ')
      c,d=0,0
      while c<20 and d<20:
            print('\n',a,end=', ')
            x=input('Press *any key to roll the dice (press only "q" to quit) : ')
            if x=='q':
                  print(a,'quit, so',b,'is the winner, congratulations!')
                  break
            e=random.randint(1,6)
            c+=e
            print('\t\tYou got',e,'\n\tNow, your total score is',c)
            print('\n',b,end=', ')
            y=input('Press *any key to roll the dice (press only "q" to quit) : ')
            if y=='q':
                  print(b,'quit, so',a,'is the winner, congratulations!')
                  break
            f=random.randint(1,6)
            d+=f
            print('\t\tYou got',f,'\n\tNow, your total score is',d,'\n')
      else:
            if d>19 and c<20:
                  print(b,'is the winner with scoreline',c,'-',d,', congratulations!')
                  print(a,'you lost, try again.')
            elif c>19 and d<20:
                  print(a,'is the winner with scoreline',c,'-',d,', congratulations!')
                  print(b,'you lost, try again.')
            else:
                  print('As both scores exceed 20 in equal number of turns, this is a tie.')
                  if c>d:
                        print('But as',c,'is more than',d,',',a,'is the winner by HSR.')
                  elif d>c:
                        print('But as',d,'is more than',c,',',b,'is the winner by HSR.')
                  else:
                        print('As both scores are equal, it is an absolute tie.')
                        z=input('\nPress "y" to play tiebreaker: ')
                        if z=='y':
                              while c==d:
                                    print('\n',a,end=', ')
                                    w=input('Press *any key to roll the dice (press only "q" to quit) : ')
                                    if w=='q':
                                          print(a,'quit, so',b,'is the winner, congratulations!')
                                          break
                                    g=random.randint(1,6)
                                    c+=g
                                    print('\t\tYou got',g,'\n\tNow, your total score is',c)
                                    print('\n',b,end=', ')
                                    v=input('Press *any key to roll the dice (press only "q" to quit) : ')
                                    if v=='q':
                                          print(b,'quit, so',a,'is the winner, congratulations!')
                                          break
                                    h=random.randint(1,6)
                                    d+=h
                                    print('\t\tYou got',h,'\n\tNow, your total score is',d,'\n')
                              if c>d:
                                    print('Now',c,'is more than',d,', so',a,'is the winner.')
                              else:
                                    print('Now',d,'is more than',c,', so',b,'is the winner.')
                        else:
                              print('\nCongratulations, both are winners.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank You!!!')
