# 中断所在循环的当次执行，直接进入下一次
for i in range(5):
    print(i)
    continue
    print("Second sentence.")

print()

# 直接结束所在的循环
for i in range(7):
    print(i)
    break
    
    for j in range(2):
        print()

print("Hi!")