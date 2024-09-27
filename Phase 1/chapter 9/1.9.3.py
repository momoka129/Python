
# error function
def func1():
    print("Func1 executes")
    num = 1 / 0
    print("Func1 ends")

# call the error function
def func2():
    print("Func 2 starts")
    func1()
    print("Func2 ends")

# error can be caught in the high layer
def main():
    try:
        func2()
    except Exception as e:
        print(f"Error occurs: {e}")

main()