#!/usr/bin/python3
# Credits: Emmanouil Sarris
# This is my first complete application written in python.
# Its only purpose is to test my python skills after a course and a half of udemy python courses ;)
# Please be kind to your comments!

# This is a game simulating a two dice game
import random

# Create the bank for the game to begin
bank = 1000000000.00

# Create the display for the game output
def print_dice(dice):
    patterns={'a':' ----- ','b':'|*    |','c':'|  *  |','d':'|    *|','e':'| * * |','f':'|     |'}
    dice_side={1:['a','f','c','f','a'], 2:['a','b','f','d','a'], 3:['a','b','c','d','a'], 4:['a','e','f','e','a'], 5:['a','e','c','e','a'], 6:['a','e','e','e','a']}
    for pattern in dice_side[dice]:
        print(patterns[pattern])


bank = 1000000000.00

print('Welcome to AssoDyo Game [ver1.0]\n\nIn real life such games can result risks of addiction and fortune loss.\nHere you can play as much as you want, as long as the bank holds or you press "y"!')
# Ask the user if he wants to continue
while True:
    k = ['y', "yes"]
    q = input('Do you want to play "Y/N"')
    # Ask the user if he wants to play
    if q.lower() in k:
        # Create the user's bank
        user_bank = 0
        # Ask the user for money to bet
        user_bet = float(input(('Show me the money... ')))
        # Gameplay
        a = random.randint(1,6)
        b = random.randint(1,6)
        # If player gets two fours or ace and two wins 50% of his bet, if two fives 75% if two sixes 100%.On any other case player loses all the money he bets
        # Depending on the result return money 
        
        # exares
        if a ==6 and b == 6:
            user_bank += user_bet*2
            bank -= user_bet*2
            print ('Exares!')
            print_dice(a)
            print_dice(b)
            print ("Your Balance: ", user_bank)
            print ("Bank Balance: ", bank)
            if bank == 0:
                break
            else:
                continue

        # pentares
        elif a == 5 and b == 5:
            user_bank += user_bet*1.75
            bank -= user_bet*1.75
            print ('Pentares!')
            print_dice(a)
            print_dice(b)
            print ("Your Balance: ", user_bank)
            print ("Bank Balance: ", bank)
            if bank == 0:
                break
            else:
                continue
        
        # ntortia
        elif a == 4 and b == 4:
            user_bank += user_bet*1.4
            bank -= user_bet*1.4
            print ('Dortia!')
            print_dice(a)
            print_dice(b)
            print ("Your Balance: ", user_bank)
            print ("Bank Balance: ", bank)
            if bank == 0:
                break
            else:
                continue
        
        # assodyo
        elif (a == 1 and b == 2) or (a == 2 and b == 1):
            user_bank += user_bet*2
            bank -= user_bet*2
            print ('AssoDyo..!')
            print_dice(a)
            print_dice(b)
            print ("Your Balance: ", user_bank)
            print ("Bank Balance: ", bank)
            if bank == 0:
                break
            else:
                continue
       
       # all other cases
        else:
            bank += user_bet
            if user_bank<=0:
                user_bank = 0
            else:
                user_bank -= user_bet
            print (a)
            print (b)
            print_dice(a)
            print_dice(b)
            print ("Your Balance: ", user_bank)
            print ("Bank Balance: ", bank)
    
    # exit from game
    else:
        print('Life is out there! Get out and play...')
        break

