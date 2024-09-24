my_list = [1, 2, 3, 5, 73, 2, 9]

def list_while_func(list):
    index = 0
    while index < len(list):
        element = list[index]
        print(element)
        index += 1
    print()

def list_for_func(list):
    for x in list:
        print(x, end = ' ')
    print()
    
list_while_func(my_list)
list_for_func(my_list)
