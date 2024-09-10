# class Person:
#     name = "Rajendra"

#     def changeName (self, name):
#         self.name = name
#         #Person.name = name ==>> this change in the both while printing 
#         # or, self.__class__.name = "Rajendra"
#                              # both the output will be same -->> Rajendra Chaudhary
# p1 = Person()        
# p1.changeName("Rajendra Chauhary")
# print(p1.name) # Rajendra Chaudhary
# print(Person.name) # Rajendra










#-----------using Class Method -----------------

class Person:
    name = "Rajendra"

    @classmethod
    def changeName(cls, name):
        cls.name = name
      


p1 = Person()        
p1.changeName("Rajendra Chauhary")
print(p1.name) # Rajendra Chaudhary
print(Person.name) # Rajendra















