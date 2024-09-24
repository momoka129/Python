tuple_1 = (1, 2, 3)

# define empty tuple
t2 = ()
t3 = tuple()

# define tuple with single element
t4 = ("helo", )
print(type(t4))

ss = ("helo")
print(type(ss))

# tuple nesting
t5 = ((1, 2, 3), (1, 3, 4))

# index to pop element
print(t5[1][2])

# tuple operations

# 查找嵌套元组中3的索引
for i, sub_tuple in enumerate(t5):
    if 3 in sub_tuple:
        index_in_tuple = sub_tuple.index(3)
        print(f"3 is found in tuple {i} at index {index_in_tuple}")

print(tuple_1.count(1))

print(len(t5))

# traverse tuple
index = 0
while index < len(tuple_1):
    print(tuple_1[index], end=' ')
    index += 1
print()

for x in tuple_1:
    print(x, end=' ')

# tuple_1[0] = 2
t1 = (1, 2, ['d', 'dd'])
t1[2][1] = 'ddd'
print(t1)

# tuple features
# 可以容纳多个元素
# 可以容纳不同类型的元素（混装）
# 数据是有序存储的（有下标编号）
# 允许重复数据存在
# 不可以修改