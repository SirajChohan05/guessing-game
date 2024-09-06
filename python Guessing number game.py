# This is a guess the number game .
import random

name = input("Enter your name: ")

print("Well" ,name, "I am thinking of a number between 1 and 20")

secretnumber = random.randint(1,20)

for guessestaken in range(1, 7):
    print("Enter a number to guess the secret number")
    guess = int(input("Take a guess: "))

    if guess < secretnumber:
        print("Your guess is too low")

    elif guess > secretnumber:
        print("Your guess is to high")

    else:
        break  #this condition is for the correct guess!

if guess == secretnumber:
    print("Good job you guessed my number in", str(guessestaken) + "guesses")

else:
    print("Nope the number i was thinking of was", str(secretnumber))

    

    


        
