class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def  hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:", sum / len(self.marks))   # or sum / 3  


s1 = Student("Tony Stark", [99, 98, 97])        
#s1.get_avg() # average marks
s1.hello() # hello
