# 传入的是代码逻辑 logic
# 解耦逻辑

# def test_func():
def test_func(compute, x, y):
    result = compute(x, y)
    print(f"type of compute(): {type(compute)}")
    print(f"result: {result}")

# 加法函数
def compute_add(a, b):
    return a + b

# 乘法函数
def compute_multiply(a, b):
    return a * b

# 分别传入加法和乘法函数
test_func(compute_add,1,2)       # 输出：result: 3
test_func(compute_multiply,1,2)  # 输出：result: 2
