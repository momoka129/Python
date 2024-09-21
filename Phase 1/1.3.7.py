num = 8

if int(input("Guess a number: ")) == num:
    print("Insane guess!")
elif int(input("Guess again: ")) == num:
    print("Congratulations!")
elif int(input("Last chance: ")) == num:
    print("Bingo!")
else:
    print("Game over.")