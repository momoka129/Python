
# read file
f_read = open("Phase 1/chapter 8/bill.txt", "r", encoding="UTF-8")

# make a backup
f_write = open("Phase 1/chapter 8/bill.txt.bak", "w", encoding="UTF-8")

line_count = 0 # record the line to be backup

for line in f_read:
    # # 1
    # line = line.strip()  # Remove any extra spaces or newlines
    
    # # WuW Each element may still have spaces: " Test" - still need strip()
    # if line.split(",")[-1].strip() == "Test": 
    #     continue
    
    # f_write.write(line + "\n")
    # line_count += 1

    # 2
    if "Official" in line:  # check if "Official" is in this line
        f_write.write(line)
        # f_write.write(line + "\n")  
        line_count += 1  

print(f"Total lines written to backup: {line_count}")

f_read.close()
f_write.close()


