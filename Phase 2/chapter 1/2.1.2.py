# self must be inside the parameter list of member methods

class Student:
    name = None

    def say_hi1(self):
        print(f"Hi, my name is {self.name}")

    def say_hi2(self, msg):
        print(msg)

stu_1 = Student()
stu_1.name = "Ali"

stu_1.say_hi1()
stu_1.say_hi2("Good morning!")