import time

# "w" way: if already exist, will clear original content and rewrite a new file
f = open("Phase 1/chapter 8/write_test.txt", "w", encoding="UTF-8")

# write 
f.write("Running is good!") # write into the memory

# flush 
f.flush()

#time.sleep(1000)

# close file
f.close()