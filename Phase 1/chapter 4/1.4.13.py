import random

money = 10000

for i in range(1, 9):
    score = random.randint(1, 10)

    if money >= 3000:
        if score < 5:
            print(f"Employee No.{i} Performance points({score}) less than 5, no salary, next!")
            print()
            continue
        else:
            money -= 3000
            print(f"Employee No.{i} satisfy the condition, give salary, Company account balance: {money}")
            print()

        
    else:
        print("No balance... Good luck next time :)")
        # break end salary disbursement
        break
