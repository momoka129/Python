def user_info(name, age):
    print(name, age)

# 位置参数
user_info('Moon', 100)

# 关键字参数
user_info(name='River', age=99)

# 缺省参数
def user_info(name, age, gender='male'):
    print(name, age, gender)

user_info(name='Pika',age=22)

#
# 不定长参数 - 位置不定长 * tuple
def info(*args):
    print(f"args type: {type(args)}, contents: {args}")    

info('queen', 30, 'Tifa', 000)

# 关键字不定长 ** dictionary  
def info(**kwargs):
    print(f"args type: {type(kwargs)}, contents: {kwargs}")

info(name = 'Xia', age = 10, gender = 'female') # limited format