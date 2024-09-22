def func_a():
    print("a")
    
def func_b():
    func_a()
    print("b")

func_b()