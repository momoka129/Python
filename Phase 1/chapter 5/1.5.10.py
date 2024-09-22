def test():
    num = 1
    print(num)

test()

# print(num)

num = 2000

def test_a():
    print(f"test_a: {num}")

def test_b():
    global num  # set to global
    num = 20001   # still a local variable if not set to global variable; not the same with global 'num'
    print(f"test_b: {num}")

test_a()
test_b()
print(num)