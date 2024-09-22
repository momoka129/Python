global money 
money = 20000

def atm_menu():
    while select != 0:
        print("1. Check your account balance")
        print("2. Deposit transaction")
        print("3. Withdrawal transaction")
        print("0. Exit")
        print()
        select = int(input("Please enter your choice: "))
