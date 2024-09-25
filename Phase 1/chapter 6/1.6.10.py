# 序列切片 起始下标 结束下标(not included) 步长
my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[2:4] 
print(result)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:] # 从头到尾
print(result2)

# reverse
new_str = my_list[::-1]
print(new_str)
