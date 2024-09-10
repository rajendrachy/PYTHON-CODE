# __ --->> symbol (__) -->> to make a private 


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   

    def reset_pass(self): # inside the class access the private value
        print(self.__acc_pass)


acc1 = Account("12345", "abcde") # outside the class can't access the value
print(acc1.acc_no)
#print(acc1.__acc_pass) # error
print(acc1.reset_pass) # output is seen in this case by making 1 function above i.e => reset_pass

