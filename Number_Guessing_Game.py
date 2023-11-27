# Project 1
# Project name : Number_Guessing_Game
# Import random module to guess a random number , which enbles users to find that number 

import random
def number_guess():
    #assign total number of chances which users allowed to play
    chances = 0
    while chances < d :  
        chances +=1
        guess = int(input("Enter your guessing : "))
        if guess<0:
            print("Enter the positive numbers")
        #Give hint about players choice , like , higher or lower then a actual number !
        elif guess>num:
            print('The computer gussed number is lower then your guess ,\nRemainder ! Remaining chances = ',d - chances)
        elif guess<num:
            print("The computer gussed number is higher then your guess ,\nRemainder ! Remaining chances = ", d - chances)
        else:
            return 'Good job..! you got the correct answer in your {} chances out of {}'.format(d - chances,d)
    #eliminate players when they are out of chances       
    else:
        return 'Sorry you are out of chances'

#collect user name
a = input('Enter Your Name : ')
print('Hi...{} you need to find the number which computer guesses'.format(a) )
# user needs to set the limit of maximum chances
d = int(input('Enter the Number of maximum chances(times) : '))
print("Enter the starting limit and ending limits of you are going to guess between ,\n Like , 0 to 100")
b = int(input('Enter the Lower limit which you want to start your number guess from : '))
c = int(input('Enter the Higher limit which you want to be the End of your guess  :  '))
#computer guesses the random number
num = random.randint(b,c)
print(number_guess())