# use set to Deduplicate
my_list = [1,1,2,3,4,5,5,5,8,8,]

my_set = set()

for x in my_list:
    my_set.add(x)

print(my_list)
print(my_set)