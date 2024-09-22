str3 = "python"

count = 0
for i in str3:
    count += 1
print(f"The length of the string: {count}")

# use function
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"The length of {data}: {count} ")

my_len("Yanami san")