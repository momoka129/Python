# single inheritance
class Phone:
    IMEI = None
    producer = "HM"

    def call_4G(self):
        print("4G calling")

class Phone2022(Phone):
    face_id = "48935"

    def call_5G(self):
        print("5g calling")

p = Phone2022()
print(p.producer)
p.call_4G()
p.call_5G()


# multiple inheritance
class NFCReader:
    nfc_type = "nfc-5"

# if parents classes have attributes with the same name, priority is given from left to right 
class Mi_Phone(Phone, NFCReader):
    producer = "Mi"

mp = Mi_Phone()
print(mp.producer)
print(mp.nfc_type)