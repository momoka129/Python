my_dit = {7: "Se", 9: "Nine"}
print(my_dit)

# add new element
my_dit[6] = "SIx"
print(my_dit)

# update element
my_dit[9] = "DDio"
print(my_dit)

# delete
ele = my_dit.pop(6)
print(my_dit)
print(ele)

# clear 
# my_dit.clear()
# print(my_dit)

keys = my_dit.keys()
print(keys)

# traverse dictionary
for key in keys:
    print(f"key: {key}",end=' ')
    print(f"value: {my_dit[key]}")

print()

for key in my_dit:
    print(f"key: {key}",end=' ')
    print(f"value: {my_dit[key]}")

# count
length = len(my_dit)
print(length)