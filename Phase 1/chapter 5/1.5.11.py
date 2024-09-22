# 1 select not define inside while loop

# 2 The variables `wallet` and `money` are global, but in `deposit()` and `withdraw()`, 
# Python treats `wallet` as local, so it needs to be declared as global. 

# 3 Additionally, `money` should be regenerated each time the functions are called to get a new random value for every transaction, 
# instead of generating it once at the start.

# video use keyboard_input = main()(return input()) to receive user input

import random

# set global variables
wallet = 20000

def atm_menu():
    global wallet
    select = -1  # 初始化 select

    while select != 0:
        print("\nATM Menu:")
        print("1. Check your account balance")
        print("2. Deposit transaction")
        print("3. Withdrawal transaction")
        print("0. Exit")
        print()

        try:
            select = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if select == 1:
            check_balance()
        elif select == 2:
            deposit()
        elif select == 3:
            withdraw()
        elif select == 0:
            print("Exiting the ATM. Thank you!")
        else:
            print("Invalid choice, please try again.")

def check_balance():
    global wallet
    print(f"Your account balance: {wallet}")

def deposit():
    global wallet
    money = random.randint(300, 2000)  # 每次存款生成一个随机值
    print(f"You made a deposit of {money}.")
    wallet += money
    check_balance()

def withdraw():
    global wallet
    money = random.randint(300, 2000)  # 每次取款生成一个随机值
    if wallet >= money:
        print(f"You took out {money} this time.")
        wallet -= money
    else:
        print("Insufficient balance for this withdrawal.")
    check_balance()

# Run the ATM menu
atm_menu()
