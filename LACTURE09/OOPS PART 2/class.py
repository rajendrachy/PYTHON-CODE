class Person:
    __name = "Rajendra"  # making private by using a symbol ( __ )

    # 1#
    def __hello(self):  # removed the name parameter
        print("hello user!")

    def welcome(self):
        self.__hello()  # corrected the method call

p1 = Person()  
p1.welcome()  # call the welcome method to print the message