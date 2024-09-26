# file operations: open, close, read, write

# write content to a file, if the file does not exist, will create it automatically.
f = open("Phase 1/chapter 8/new_file.txt", "w", encoding="UTF-8")

# write operation
f.write("This is a newly created file.\n")
f.write("We are writing some text into it.\n")

# close the file
f.close()

f = open("Phase 1/chapter 8/new_file.txt", "r", encoding="UTF-8")
print(type(f))

# 1.1 read operation
# print(f.read())

# this 'read' will do job start from last 'read' achieved place
# The 'read' operation will resume from where the last 'read' left off

# 2
# print(f.readlines())    # read all lines of the file, and encapsulate into a list

# 1.2
# print(f.read(10))

# 3
# print(f.readline()) # every time read one line

# 4
for line in f:
    print(f"Every line: {line}")

f.close()

# close file automatically
with open("Phase 1/chapter 8/new_file.txt", "r", encoding="UTF-8") as f:
    print(f.read())