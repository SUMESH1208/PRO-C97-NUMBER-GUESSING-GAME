import random 

print("Welcome To Number Guessing Game!")
print("Guess a number(between 1 and 9):")
print("You have 5 Chances to guess the Number! Good Luck! ")
Number = random.randint(1,9)


chances = 0

while chances<5:

    guessingNumber = int(input("Guess the Number:- ")) 

    if(guessingNumber == Number):
        print("Congratulations You Are Right! You Won!!!")
        break

    elif guessingNumber < Number:
        print("Your Guess is too low: Guess a number higher than ", guessingNumber)

    else:
        print("Your Guess is too high: Guess a number lower than ", guessingNumber)  


    chances += 1


if not chances < 5:
        print("Oh No Chances are over Try Again Next Time! And the Number was ", Number)
       