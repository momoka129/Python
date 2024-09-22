height = int(input("Please enter your height: "))

if height < 120:
    print("Free.")
elif int(input("Please enter your vip level(1-5): ")) > 3:
    print("Vip level greater than 3, free.")
else:
    print("U need a ticket.") 

print("Enjoy yourself!")

