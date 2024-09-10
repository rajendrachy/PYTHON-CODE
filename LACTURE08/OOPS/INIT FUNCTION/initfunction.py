#1.

# class Student:
#      name = "karan"
#      def __init__(self): # self is necessary to write
#        #print(self)
#        print("creating new student in database")

# s1 = Student() # () --> is used to call the constructors
# #print(s1) #s1 and self is same while print
# print(s1.name)





# #2.

# class Student:
     
#      def __init__(self, fullname): # self is necessary to write
#        self.name = fullname
#        #print(self)
#        print("adding new student in database")

# s1 = Student("Karan") # () --> is used to call the constructors
# #print(s1) #s1 and self is same while print
# print(s1.name)






#2.

class Student:
     
     def __init__(self, name, marks): # self is necessary to write
       self.name = name
       self.marks = marks
       
       print("adding new student in database")

s1 = Student("Karan", "100") # () --> is used to call the constructors
print(s1.name, s1.marks)

