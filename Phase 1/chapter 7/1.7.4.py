# def - have name function - multiple use available
# lambda - no name - use once only

def test_func(compute, a, b):
    result = compute(a,b)
    print(result)

a = 2
b = 8

test_func(lambda x, y: x - y, a, b)
test_func(lambda x, y: x + y, a, b)
