if int(input("Do you want a gift? (1/0)")) == 1:
    print("Answer me a question then you will get it.")
    print("What walks on four legs in the morning, two legs at noon, and three legs in the evening? ")
    print("1 - a human")
    print("2 - a spider")

    if int(input("Your answer: ")) == 1:
        print("Correct!")
        print("You are the 99th person to answer my question correctly!")
        print("So i will eat you.")
    else:
        print("I will eat you.")
        
else:
    print("Alright.")