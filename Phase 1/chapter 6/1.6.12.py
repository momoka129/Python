my_set = {"Tuzi", "YUyuan","Zhenzhu","YUyuan","YUyuan"}

# define empty set
my_set_empty = set()

print(my_set)

# 不能重复
# 乱序存储（不支持下标索引）

# add
my_set.add("OOO")
print(my_set)

# remove 
my_set.remove("OOO")
print(my_set)

# random access an element
value = my_set.pop()
print(value)
print(my_set)

# clear
my_set.clear()
print(my_set)

# 取两个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
set3 = set1.difference(set2)
print(set3)
print(set1)
print(set2)

# 消除两个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
set1.difference_update(set2)
print(set1)
print(set2)

# two sets union
set3 = set1.union(set2)
print(set3)

# count
count = len(set3)
print(count)

# 集合的遍历
# 集合不支持下标索引
# 不能用while循环
for x in set3:
    print(x, end=' ')