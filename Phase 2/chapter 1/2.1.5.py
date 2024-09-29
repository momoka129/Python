class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student class created an object!")

    # magic methods
    # address to string
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    
    # below: operator overloading
    # < or > comparison
    # other: another class object 
    # return bool
    def __lt__(self, other):
        return self.age < other.age
    
    # <= or >=
    def __le__(self, other):
        return self.age <= other.age
    
    # ==
    def __eq__(self, value: object) -> bool:
        return self.age == value.age

stu1 = Student("Yui", 25)
stu2 = Student("Sally", 23)
stu3 = Student("Shelly", 23)

print(stu1)
print(str(stu2))
print(stu3)
print(stu1 <= stu2)
print(stu1 > stu2)
print(stu1 == stu3)