import winsound 

class Clock:
    id = None
    price = None

    def ring(self):
        winsound.MessageBeep(9)

clock1 = Clock()
clock1.id = 324902
clock1.price = 30.00
print(f"Clock id: {clock1.id}, price: {clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = 481489
clock2.price = 88
print(f"Clock id: {clock2.id}, price: {clock2.price}")
clock2.ring()