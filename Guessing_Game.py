from random import randint

for i in range(1, 10):
    guessNumber = int(input("Enter a number between 1 to 10: "))
    randomNumber = randint(1, 10)
    
    if guessNumber == randomNumber:
        print("Congratulations!! You are correct.")
    else:
        print("Sorry!! You aren't correct.")
        print(f"The correct number was {randomNumber}")
