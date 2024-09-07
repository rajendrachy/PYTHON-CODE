# functions in the python 

#1. ..........endswith()..........

# str = "I am studying python from Apnacollege"
# print(str.endswith("ege")) # True
# print(str.endswith("app")) # False


# 2. capitalize - >> capitalize 1st character
# str = "i am studying python from Apnacollege"
# print(str.capitalize()) # i --> capital first character
# print(str) # in second time the first character will be not capitalized


# str = "I am studying python from Apnacollege"
# str = str.capitalize()
# print(str) # in this case all time capatilized
# print(str)




# 3. Replace -- >> replace(old, new)

# str = "I am studying python from Apnacollege"
# print(str.replace("o", "a"))
# print(str.replace("python", "JavaScript"))



# 4. find -->> find(word)

# str = "I am studying python from Apnacollege"
# print(str.find("o")) # return the index of the first occurance
# # starting from 0 index 
# print(str.find("from"))
# # negative indexing valid for the slicing 
# print(str.find("U")) # not exist so output --->> -1


# 5. count -->>  count("da")
str = "I am from studying python from Apnacollege" # case sensitive
print(str.count("from")) # how many times exists
print(str.count("a")) # 2 ->> case sensitive
print(str.count("A")) # 1 -->> case sensitive

