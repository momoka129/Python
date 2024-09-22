def say_hi():
    print("Hi yanami!")
    return None

say_hi()

# none to compare
def check_age(age):
    if age > 18:
        return "Welcome!"
    else:
        return

res = check_age(20)
if not res:
    print("No entry for minors!")