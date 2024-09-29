class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student class created an object!")

stu = Student("Yui", 25, 48239582)
print(stu.tel)