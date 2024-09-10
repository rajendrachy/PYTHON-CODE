class Student:

    #default costructors
    def __init__(self):
        pass

  # parameterized constructors
    def __init__ (self, name, marks):
        self.name = name # self is obj reference
                         # it is write due to the name & marks of the student is different
        self.marks = marks    
        print("adding new students")

s1 = Student("karam", 99)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)