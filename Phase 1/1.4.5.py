i = 1
while i < 10:

    j = 1
    while j <= i:
        print(f"{i} x {j} = {j * i}\t", end = '')
        j += 1
    
    i += 1
    print()     # print spare: new line