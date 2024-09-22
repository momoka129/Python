import random
num = random.randint(1, 100)
count = 0

flag = True
while flag:
    guess = int(input("Your guess: "))
    count += 1
    if guess == num:
        flag = False
        print("Bingo!")
    else:
        if guess > num:
            print("Greater.")
        else:
            print("Lesser.")
print(f"Total guess time: {count}")