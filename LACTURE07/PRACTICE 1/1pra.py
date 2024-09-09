#Qn. 1-->>

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file i/o\n")
#     f.write("Using a Javascript\ni like programming in the jave")



#Qn. 2
# with open("demo.txt", "r") as f:
#     data = f.read()
    
#     newdata = data.replace("Java", "Python")
#     print(newdata)


# with open("demo.txt", "w") as f:
#     f.write(newdata)    




#3. 
# word = "learning"
# # word = "Xlearning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#        print("found")
#     else:
#        print("Not found")




       #............. Using a function...............

def check_for_word():
   word = "learning"
# word = "Xlearning"
   with open("practice.txt", "r") as f:
     data = f.read()
     if(data.find(word) != -1):
        print("found")
     else:
        print("Not found")

check_for_word()        