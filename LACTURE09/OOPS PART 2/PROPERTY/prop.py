# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math ) / 3) + "%"


#     def calcPercentage (self):   # changing percentage
#                 self.percentage = str((self.phy + self.chem + self.math ) / 3) + "%"


# stu1 = Student(98, 97, 99)        
# print(stu1.percentage)


# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)





#----------------Using property----------------


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)        
print(stu1.percentage)  # prints: 98.0%

stu1.phy = 86 # change the physics marks]
print(stu1.percentage)  # prints: 94.0%