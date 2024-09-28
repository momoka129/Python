my_list = [["a", 33], ["b", 54], ["c", 13]]

# 1
# def choose_sort_key(element):
#     return element[1]

# my_list.sort(key=choose_sort_key, reverse=True)

# 2
my_list.sort(key=lambda element: element[1], reverse=False)

print(my_list)