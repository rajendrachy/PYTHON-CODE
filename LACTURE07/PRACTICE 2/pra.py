# previous

# def check_for_word():
#    word = "learning"
# # word = "Xlearning"
#    with open("practice.txt", "r") as f:
#      data = f.read()
#      if(data.find(word) != -1): # or if(word in data):
#         print("found")
#      else:
#         print("Not found")

# check_for_word()  


# Qn 1.

# def check_for_line():
#    word = "Javascript"
#    data = True
#    line_no = 1
#    with open("demo.txt", "r") as f:
#       while data:
#          data = f.readline()
#          if(word in data):
#             print(line_no)
#             line_no = line_no + 1

#    return -1  
  
# check_for_line()    



# qn. 2

# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num)) # typecast to int --->> to do this we can remove the space while printing
#             num = ""
#         else:
#             num += data[i]




# or,
count = 0
with open("sample.txt", "r") as f:
    data = f.read()
   
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)            
