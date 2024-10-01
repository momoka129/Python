class Phone:
    IMEI = None
    producer = "IT"

    def call_5g(self):
        print("parents 5g")

class MyPhone(Phone):
    producer = "Yn"

    def call_5g(self):
        print("Subclass 5g calling")
        # way 1
        print(f"parent class producer: {Phone.producer}")
        Phone.call_5g(self)

        # way 2
        super().call_5g()   # no need self argument

phone = MyPhone()
print(phone.producer)
phone.call_5g()