import random
number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Insane guess!")
else:
    if guess > number:
        print("Greater.")
    else:
        print("Lesser.")

    guess = int(input("Guess again: "))

    if guess == number:
        print("Congratulations!")
    else:
        if guess > number:
            print("Greater.")
        else:
            print("Lesser.")
        
        guess = int(input("Last chance: "))
        
        if guess == number:
            print("Bingo!")
        else:
            print("GAME OVER!")