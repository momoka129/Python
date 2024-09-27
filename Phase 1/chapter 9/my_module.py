
__all__ = ['testA', 'test']

def test(a, b):
    print(a + b)

def testA():
    print("aaa")

def testB():
    print("bbb")

# only True when inside its module
if __name__ == "__main__":
    test(2,4)