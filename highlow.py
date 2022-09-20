'''
Create a random number

Have user guess the number

Identify if the guess is too high or too low

Finish when number is guessed right

Count how many guesses were needed

'''

#Import Random
import random

#Generate a random number
randomNum = random.randint(1,100)

#Ask for User's guess
print("I am thinking of a number between 1 and 100. \n")

print("Guess the number, and I will tell you if you are \ntoo high, too low, or got it right.\n")

print("Good Luck!")

#variables
CountOfTries = 0

guess = int(input("Please enter a number: "))


#While Loop
while True:

    #Counter and Loops with High/Low Conditionals

    CountOfTries +=1
    if (guess < randomNum):
        print("Too Low!")
        guess = int(input("Please enter a number: "))
    elif (guess > randomNum):
        print("Too High!")
        guess = int(input("Please enter a number: "))
    elif (guess == randomNum):
        #Stop Loop if correct guess
        print("You Guessed The Right Number!")
        break
print("No. of tries: ", CountOfTries)
