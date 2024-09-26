# multiple return value: no data type limited
def test():
    return 1,2,'d'

x,y,z = test()
print(x,y,z)