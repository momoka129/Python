
# basic 
try:
    f = open("Phase 1/chapter 9/linux.txt", "r", encoding="UTF-8")
except:
    print("Error occurs since the file does not exist, open with 'w'.")
    open("Phase 1/chapter 9/linux.txt", "w", encoding="UTF-8")


# catch a specific exception 
try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
except ValueError as e:
    # This block will only run if a ValueError occurs
    print("This is not a valid number.")
    print(f"The error message: {e}")


# catch multiple exception
try:
    print(name)
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print(f"The error message: {e}")


# catch all exception
try:
    print(name)
except Exception as e:
    print(f"Error occurs! {e}")

    
# else - execute when no error 
# finally - execute whatever
try:
    x = int(input("Enter a number: "))
except ValueError as e:
    print("This is not a valid number.")
    print(f"The error message: {e}")
else:
    print("You are a good boy!")
finally:
    print("See you next time.")