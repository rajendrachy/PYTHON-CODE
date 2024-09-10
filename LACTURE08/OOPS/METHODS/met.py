
class Student:
     college_name = "ABC College"

     def __init__(self, name, marks): # self is necessary to write
       self.name = name
       self.marks = marks
       

     def welcome(self):
       print("Welcome Student", self.name)


     def get_marks(self):
         return self.marks

s1 = Student("Karan", "100") # () --> is used to call the constructors
print(s1.name, s1.marks)
print(s1.get_marks())
