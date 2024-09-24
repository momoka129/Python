my_str = "kinoko"

value = my_str[2]
print(value)

# search
index = my_str.index("k")
print(index)

# replace
new_str = my_str.replace("k", "y")
print(my_str)
print(new_str)

# split
str = "i admire losing heroines"
str_list = str.split(" ")
print(type(str_list))
print(str_list)

# strip
str_1 = "      cho         "
print(str_1)
new_str = str_1.strip() # 不传入参数 默认去除首尾空格
print(new_str)

str_1 = "120345183321"
print(str_1)
new_str = str_1.strip("12") # 去除'1' & '2'
print(new_str)

# count
count = str_1.count("3")
print(count)

# len
print(len(str_1))

# string features
# 可以容纳多个元素
# 只可以存储字符串
# 数据是有序存储的（有下标编号）
# 允许重复数据存在
# 不可以修改