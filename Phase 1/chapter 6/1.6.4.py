# 1 search 
my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)

# index = my_list.index(6)
# print(index)

# 2 modify
my_list[4] = 1
print(my_list)

# 3 insert
my_list.insert(2, "Kinoko")
print(my_list)

# 4 append
my_list.append(8)
print(my_list)

# 5 extend
my_list.extend(["Love", 520])
print(my_list)

# 6 delete: del
del my_list[0]
print(my_list)

# 6.2 delete: pop
element = my_list.pop(0)
print(my_list)

# 6.3 remove: delete the first element found
my_list.remove(3)
print(my_list)

# 6.4 clear
my_list.clear()
print(my_list)

# 7 count
count = my_list.count(1)
print(count)

# 8 list total number
count = len(my_list)
print(count)

# list features
# 可以容纳多个元素
# 可以容纳不同类型的元素（混装）
# 数据是有序存储的（有下标编号）
# 允许重复数据存在
# 可以修改